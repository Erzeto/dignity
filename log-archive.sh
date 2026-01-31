#!/bin/bash

# Cek argumen
if [ -z "$1" ]; then
  echo "Usage: $0 <log-directory>"
  exit 1
fi

LOG_DIR="$1"
ARCHIVE_DIR="$HOME/log_archives"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
ARCHIVE_NAME="logs_archive_${TIMESTAMP}.tar.gz"
LOG_FILE="$ARCHIVE_DIR/archive.log"

# Cek apakah folder log ada
if [ ! -d "$LOG_DIR" ]; then
  echo "Error: Directory $LOG_DIR does not exist"
  exit 1
fi

# Buat folder arsip kalau belum ada
mkdir -p "$ARCHIVE_DIR"

# Kompres log
tar -czf "$ARCHIVE_DIR/$ARCHIVE_NAME" "$LOG_DIR" 2>/dev/null

# Catat ke log
echo "$(date +"%Y-%m-%d %H:%M:%S") - Archived $LOG_DIR to $ARCHIVE_NAME" >> "$LOG_FILE"

echo "Archive created: $ARCHIVE_DIR/$ARCHIVE_NAME"

