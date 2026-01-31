#!/bin/bash

LOGFILE=$1

if [ -z "$LOGFILE" ]; then
  echo "Usage: ./log-analyzer.sh <logfile>"
  exit 1
fi

echo "Top 5 IP addresses with the most requests:"
awk '{print $1}' "$LOGFILE" \
| sort \
| uniq -c \
| sort -nr \
| head -5

echo
echo "Top 5 most requested paths:"
awk '{print $7}' "$LOGFILE" \
| sort \
| uniq -c \
| sort -nr \
| head -5

echo
echo "Top 5 response status codes:"
awk '{print $9}' "$LOGFILE" \
| sort \
| uniq -c \
| sort -nr \
| head -5

echo
echo "Top 5 user agents:"
awk -F\" '{print $6}' "$LOGFILE" \
| sort \
| uniq -c \
| sort -nr \
| head -5
