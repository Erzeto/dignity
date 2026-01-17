#!/bin/bash

# ---------- CPU ----------
CPU_IDLE=$(top -bn1 | grep -i "Cpu(s)" | awk '{for(i=1;i<=NF;i++){if($i ~ /id,/) print $(i-1)}}')
CPU_USED=$(awk "BEGIN {printf \"%.2f\", 100 - $CPU_IDLE}")
echo "Total CPU Usage: $CPU_USED%"

# ---------- RAM ----------
read TOTAL USED FREE <<< $(free -m | awk '/Mem:/ {print $2, $3, $4}')
USED_PCT=$(awk "BEGIN {printf \"%.2f\", ($USED/$TOTAL)*100}")
FREE_PCT=$(awk "BEGIN {printf \"%.2f\", ($FREE/$TOTAL)*100}")
echo "Total RAM : ${TOTAL} MB"
echo "Terpakai  : ${USED} MB (${USED_PCT}%)"
echo "Bebas     : ${FREE} MB (${FREE_PCT}%)"

