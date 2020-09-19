#! /bin/sh

cd data_system
DATE_TODAY=$(date +"%F")
vnstat -i wlo1 > $DATE_TODAY.txt
echo -e "\n" | mailx -s "Data Usage" -A $DATE_TODAY.txt saibalaram6712@gmail.com

