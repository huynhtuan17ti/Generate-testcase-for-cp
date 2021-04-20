# Generate-testcase-for-cp
A simple project for generating testcases for competitive programming problem  
## File description  
**GenerateTestcase.py** -- generate testcase and run solution file    
**main.py** -- main file to design random generative function  
**convert_and_trimming.py** -- convert crlf to lf and trimming whitespace, tab, downline  
**GenerativeFunction.py** -- include all random function to generate a numbers, graph, tree ...  
**checking_testcasse.py** -- compare output files between a solution and in testcase folder    
## How to use checking
Folder tree for checking testcases  
<pre>
|___ CHECKING_FOLDER  
|    |___ SOLUTION.cpp  
|    |___ SOLUTION.inp  
|    |___ SOLUTION.out  
|    |___ TESTCASE_FOLDER  
|         |___ 0.in  
|         |___ 0.ans  
|         |___ 1.in  
|         |___ 1.ans  
|         |___ ...  
</pre>
