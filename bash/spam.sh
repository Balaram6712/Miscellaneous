#! /bin/bash
: '
this is multi
line commenting in bash script
:<space>apotrophe to end just keep '

: 'to comment out something in and ypu want to print it to the user then 
cat << <name>
text you want to print
<name>

this helps like a comment to the user who is executing and will get to know the printed'

for i in {1..10}
do
echo -e "\n" | mailx -s "Please tell for whom marks given" <maild id>
done 
