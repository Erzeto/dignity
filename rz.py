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

echo "Total Disk:"
read TOTAL USED FREE PCT <<< $(df -h / | awk 'NR==2 {print $2,$3,$4,$5}')
echo "Total Disk : $TOTAL"
echo "Digunakan : $USED ($PCT)"
echo "Kosong    : $FREE"


echo "Top 5 CPU:"
ps -eo pid,comm,%cpu --sort=-%cpu | head -n 6

echo "Top 5 RAM:"
ps -eo pid,comm,%mem --sort=-%mem | head -n 6

