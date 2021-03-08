#! /bin/bash

DATE_TODAY=$(date +"%d")
MONTH_NOW=$(date +"%m")

if [[ $DATE_TODAY -eq 20 ]] && [[ $MONTH_NOW -eq 10 ]]
then
	echo -e "\n" | mailx -s "Happy birthday!" -A images.jpeg <mail-id>
fi				#bday	also attaching a image 
