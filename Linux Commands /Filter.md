## Inside the folder 
```
Created a file1:
content: " i love you baby"
         "BABY"

grep baby file1 - returns the line with baby highligthed
grep BABY file1 - returns the line with BABY highligthed
grep -i baby file1 - returns both the line as -i removes the case sensitive
```

## from home path searching using grep
 ```
 grep -R baby * - will get the content from the home path inside any directory
 grep -R -i baby * - will get the content from the home path inside any directory and casesensitive
 grep -Ri baby teju - will get the content from the home path inside teju directory 
 grep -v baby teju - this gets the content other then baby(sentence) its the opposite 
 grep -Rv baby teju - As we are working from the homepath -Rv is mentioned 
 grep -Riv baby teju - in this case nothing will return
```

 ## Other commands to search
 ```
 head <filename> - default it will return 10 lines 
 tail <filename> - default it will return 10 lines 
 head -2 <filename> - returns 1st 2 lines
 tail -15 <filename> - returns last 15 lines 
 tail -f <filename> - this will not exit from the file 
 less <filename> - It will open file in vi mode
 more <filename> - It will return some percentange of file and pressing enter we can see other file content.
 ```


