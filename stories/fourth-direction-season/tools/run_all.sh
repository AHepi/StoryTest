#!/bin/bash
# Run the GLM Seconds episodes to the end, restarting after failures (finished steps are skipped),
# then run the revision rounds the same way.
cd "$(dirname "$0")"
for try in 1 2 3 4 5 6 7 8; do
  python3 -u glm_seconds_pipeline.py >> run.log 2>&1 && break
  echo "episode run stopped (try $try); restarting in 5 minutes" >> run.log; sleep 300
done
for try in 1 2 3 4 5 6 7 8; do
  python3 -u glm_seconds_rounds.py >> rounds.log 2>&1 && break
  echo "rounds run stopped (try $try); restarting in 5 minutes" >> rounds.log; sleep 300
done
echo "=== all done ===" >> rounds.log
