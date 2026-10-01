#!/usr/bin/env python3
"""Turn an ebook (.epub, .azw3 or .mobi) into one plain-text file.

What it does: reads the book's parts in reading order, keeps headings as
lines starting with "#", keeps paragraphs as separate lines, and writes the
result to the output path. The text is for local reading and for
overlap_check.py only. It belongs in sources/raw/, which git ignores, and
must never be committed.

Usage: book_to_text.py BOOK_FILE OUTPUT.txt
"""
import os
import re
import shutil
import sys
import warnings
import zipfile
import xml.etree.ElementTree as element_tree
from urllib.parse import unquote

from bs4 import BeautifulSoup, XMLParsedAsHTMLWarning

# Ebook parts are XHTML; reading them as HTML is intended, so the warning is noise.
warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)

HEADING_TAGS = ["h1", "h2", "h3", "h4", "h5", "h6"]
BLOCK_TAGS = HEADING_TAGS + ["p", "li", "blockquote", "pre", "tr", "div"]


def html_to_lines(html_text):
    """Return the readable lines of one HTML part, headings marked with '#'."""
    soup = BeautifulSoup(html_text, "lxml")
    for unwanted in soup(["script", "style", "head"]):
        unwanted.decompose()
    lines = []
    for block in soup.find_all(BLOCK_TAGS):
        # Skip a block that contains other blocks; its children are read instead.
        if block.name == "div" and block.find(BLOCK_TAGS):
            continue
        if block.find_parent(["p", "li", "blockquote"]) and block.name != "blockquote":
            continue
        text = re.sub(r"\s+", " ", block.get_text(" ")).strip()
        if not text:
            continue
        if block.name in HEADING_TAGS:
            level = int(block.name[1])
            lines.append("#" * level + " " + text)
        else:
            lines.append(text)
    return lines


def epub_reading_order(epub_archive):
    """Return the archive paths of an epub's text parts in reading order."""
    container = element_tree.fromstring(epub_archive.read("META-INF/container.xml"))
    package_path = next(
        element.attrib["full-path"]
        for element in container.iter()
        if element.tag.endswith("rootfile")
    )
    package = element_tree.fromstring(epub_archive.read(package_path))
    package_folder = os.path.dirname(package_path)
    manifest = {}
    for element in package.iter():
        if element.tag.endswith("}item") or element.tag == "item":
            manifest[element.attrib["id"]] = element.attrib["href"]
    reading_order = []
    for element in package.iter():
        if element.tag.endswith("itemref") or element.tag == "itemref":
            relative_path = manifest.get(element.attrib["idref"])
            if relative_path:
                full_path = os.path.normpath(os.path.join(package_folder, relative_path))
                reading_order.append(full_path.replace("\\", "/").split("#")[0])
    return reading_order


def epub_to_lines(epub_path):
    with zipfile.ZipFile(epub_path) as epub_archive:
        names_in_archive = set(epub_archive.namelist())
        lines = []
        for part_path in epub_reading_order(epub_archive):
            if part_path not in names_in_archive:
                part_path = unquote(part_path)
                if part_path not in names_in_archive:
                    continue
            part_html = epub_archive.read(part_path).decode("utf-8", errors="ignore")
            lines.extend(html_to_lines(part_html))
            lines.append("")
    return lines


def kindle_to_lines(kindle_path):
    import mobi

    unpack_folder, unpacked_path = mobi.extract(kindle_path)
    try:
        if unpacked_path.endswith(".epub"):
            return epub_to_lines(unpacked_path)
        with open(unpacked_path, encoding="utf-8", errors="ignore") as unpacked_file:
            return html_to_lines(unpacked_file.read())
    finally:
        shutil.rmtree(unpack_folder, ignore_errors=True)


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    book_path, output_path = sys.argv[1], sys.argv[2]
    extension = os.path.splitext(book_path)[1].lower()
    if extension == ".epub":
        lines = epub_to_lines(book_path)
    elif extension in (".azw3", ".azw", ".mobi"):
        lines = kindle_to_lines(book_path)
    else:
        sys.exit(f"Unsupported book type: {extension}")
    with open(output_path, "w", encoding="utf-8") as output_file:
        output_file.write("\n".join(lines))
    word_count = sum(len(line.split()) for line in lines)
    print(f"{output_path}: {len(lines)} lines, {word_count} words")


if __name__ == "__main__":
    main()
