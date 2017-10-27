#!/bin/sh

# Time in minutes
TIME_LIMIT=$((60*60))

# State file for updating last touch
STATE_FILE=deadman.dat

# Last access time of the state file (in epoch)
last_touch=$(stat -c %Y $STATE_FILE)

# Current time (in epoch)
current_time=$(date +%s)

# How much time is remaining before the switch fires
timeleft=$((current_time - last_touch))

if [ $timeleft -gt $TIME_LIMIT ]; then
  echo "Dead man's switch activated: job failed!"
fi
