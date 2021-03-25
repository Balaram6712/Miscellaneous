#!/bin/bash

HOST='ip/domain'
USER='user_name'
PASSWD='passwd'
FILE='aa'

#-n does not collect password
#if u want to upload a file using script

ftp -n $HOST <<END_SCRIPT
quote USER $USER
quote PASS $PASSWD
ls 
quit
END_SCRIPT


