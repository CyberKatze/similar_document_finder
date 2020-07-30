# Find Similar Documents (using LCS) 
### Phases
- [x] Implementing LCS
- [x] Similarity and Dependency Score
- [ ] Scrape specific website documents and compare to a given document
- [ ] Find similar codes to the given code in Geekforgeeks website
- [ ] General approach of finding similar documents on Google
### Requirement
Install Python3 on your machine.
By the following command install required packages from the requirement file:
``` bash
$ pip install -r requirement.txt
```
### executing
Specify your documents in the text files and use the [main.py](main.py)
program to compare those files. Consider these files:
#### text 1
```
Both rest of know draw fond post as.  
It agreement defective to excellent. Feebly 
do engage of narrow. Extensive repulsive belonging 
depending if promotion be zealously as.
Preference inquietude asknow 
are dispatched led appearance. Small meantin so doubt 
hopes. Me smallness is existence at-tending he enjoyment 
favourite affection. Deliv-ered is to ye belonging enjoyment 
preferred. As-tonished and acceptance men two discretion. 
Laweducation recommend did objection how old.
To sure calm much most long me mean. 
Able rent long in do we. Uncommonly no it 
announcingmelancholy an in. Mirth learn it he 
given. Secureshy favour length all twenty denote. 
He felicity noan at packages answered opinions juvenile.
```
#### text 2
```
Both rest of know draw fond post as.  
It agreement defective to excellent. Feebly 
do engage of narrow. Extensive repulsive belonging 
depending if promotion be zealously as.
Performed suspicionin certainty so frankness by attention 
pretended.Newspaper or in tolerably education enjoyment.
Extremity excellent certainty discourse sincerityno he so 
resembled. Joy house worse arise totalboy but. Elderly up 
chicken do at feeling is. Likeseen drew no make fond at on 
rent.  Behaviourextremely her explained situation yet 
septembergentleman are who. Is thought or pointed 
hearinghe.
To sure calm much most long me mean. 
Able rent long in do we. Uncommonly no it 
announcingmelancholy an in. Mirth learn it he 
given. Secureshy favour length all twenty denote. 
He felicity noan at packages answered opinions juvenile.
```
``` 
$ ./main.py text1.txt text2.txt
Similarity Score: 42.77%  
Dependency Score of text1 on text2: 64.15%  
Dependency Score of text2 on text1: 56.20%

LCS Words: 
Both rest of know draw fond post as. It agreement defective to
excellent. Feebly do engage of narrow. Extensive repulsive belonging depending if promotion be zealously as. so he To sure
calm much most long me mean. Able rent long in do we. Uncommonly
no it announcingmelancholy an in. Mirth learn it he given.
Secureshy favour length all twenty denote. He felicity noan at
packages answered opinions juvenile.
```
