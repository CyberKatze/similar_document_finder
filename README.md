
<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
<div align="center">
  <a href="https://basu.ac.ir/">
    <img src="https://upload.wikimedia.org/wikipedia/en/thumb/4/49/Bu_Ali_Sina_University.svg/1200px-Bu_Ali_Sina_University.svg.png" alt="Logo" width="100" height="100">
  </a>

  <h3 align="center">Finding Similar Documents</h3>
  <p align="center">
    Algorithm Course Project
    <br />
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>📗 <b>Table of Contents</b></summary>
  <ol>
    <li>
      <a href="#🔰-about-the-project"> About The Project</a>
    </li>
    <li><a href="#⚡-how-it-works">How it Works</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## 🔰 About The Project
Finding Similar documents using LCS algorithm. This project is written for algorithm course. More information [Report.pdf](report.pdf).

<p align="right">(<a href="#top">back to top</a>)</p>

## ⚡ How It Works
Install Python3 on your machine.
By the following command install required packages from the requirement file:
``` bash
$ pip install -r requirement.txt
```
### executing
- Specify your documents in the text files and use the [main.py](main.py)
program to compare those files. Consider these files:
``` bash
$ ./main.py [file1.txt] [file2.txt]
```


<p align="right">(<a href="#top">back to top</a>)</p>

## Example
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
<p align="right">(<a href="#top">back to top</a>)</p>


### Author
- [Mehrdad Shahidi](https://github.com/CyberKatze)
