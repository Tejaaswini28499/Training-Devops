ls -l > /tmp/tejux.txt = Output of ls-l will be stored in tmp directory tejux.txt file
cat /tmp/tejux.txt = printing /tmp/tejux.txt

echo "hii teju" > /tmp/tejux.txt = Output of echo will be stored in tmp directory tejux.txt file
cat /tmp/tejux.txt = printing /tmp/tejux.txt
Note: ">" overides the last output and print new output
      ">>" will not overides all keep all the output


ls -l >> /tmp/tejux.txt = without overiding the last output it will be appended.
cat /tmp/tejux.txt = printing /tmp/tejux.txt
 
echo "hii teju" >> /tmp/tejux.txt = without overiding the last output it will be appended.
cat /tmp/tejux.txt = printing /tmp/tejux.txt
 
uptime =  10:43:45 up 1 day,  5:04,  1 user,  load average: 0.01, 0.02, 0.00
date = Wed Sep  4 10:44:29 UTC 2024
wc -l /tmp/tejux.txt = print the number of lines in the txt file.

note: | command is used to append another command

ls -l | wc -l = give the count of ls-l 
ls  | wc -l  = give the count of ls

ls  | grep yogi = searching "yogi" from home directory
ls | grep Yogi = searching "Yogi" from home directory
ls | grep -i Yogi = case sensitive search


find /home -name file1= from anywhere i need to serach file1
note: need to know where the file is located eg: home, root. 

find / -name file1 = file1 is inside teju.txt so when you are inside the teju directory then no need to specify /home you can directly give / -name file1


find /home -name fi* = this will provide the o/p where we get the files starting from the name "fi"

tail -10 template-1716989177504train.yaml > print.txt = last 10 lines will be o/p for new file print.txt when you cat print.txt you will find the last 10 lines of temp... here

cat print.txtt > sam.txt = here print.txtt doesnt exits but the sam.txt will be created but when you print sam.txt there is no o/p as the file doesnt exists.

cat print.txtt 2> sam.txt = as print.txtt does exists there is an error message printed "2>" when you give this then the error message will be input for sam.txt
i.e,= no such directory/file exists will be printed.
note: 1 will be the default value which will not be seen even if we wont mention its default take as 1 if you give 2 all the errors will be given.

cat print.txtt &> sam.txt = The &> operator in this context ensures that all output from the cat print.txtt command, whether it's normal output or error messages, is captured in the sam.txt file.

cat print.txtt &>> sam.txt = >> will append the new o/p with the old o/p and when you can you will see all the o/p as specified before ">" will overide and ">>" will not overide it will append to existing.

free -m = give the RAM specification / memory available
df -h = disk usuage

