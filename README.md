# IGCSE Computer Science Feb/Mar 2018 Practicals Solution in Python 3
This is a python program I built according to the specifications of the pre-release material provided by CIE for the IGCSE Computer Science Feb/March 2018 Practical paper.

# The problem given in the pre-release material

In preparation for the examination candidates should attempt the following practical tasks by writing and testing a program or programs.

Students in a school are allowed to choose extra subjects each year. Students provide the school administrator with their names and their subject choices. Places in subject groups are allocated on a `first come, first served' basis. There are two classes of 30 students and they can each choose two extra subjects from:

• Physics

• Chemistry

• History

• Geography

• Computer Science 

The maximum group size for each subject choice is 20 students and the minimum group size is 10 students. If more than 20 students choose a subject then that subject can be split into two groups. Each subject can have no more than two groups. If less than 10 students choose a subject then it is not available that year. A program is required to show a summary of the number of students who have chosen each subject, identify subject group sizes, produce subject group lists and identify problems. 

Write and test a program or programs for the school administrator.

• Your program or programs must include appropriate prompts for the entry of data.

• Error messages and other output need to be set out clearly and understandably.

• All variables, constants and other identifiers must have meaningful names.

You will need to complete these three tasks. Each task must be fully tested.

TASK 1 — Data entry and number of students who have chosen each subject.
The school administrator enters the data for each student. Write a program for TASK 1 to store this data then calculate and output the number of students who have chosen each subject.

TASK 2 — Output subject group lists and identify problems. 
Using your results from TASK 1, allocate students to subject groups. Print out list(s) of student names for each viable subject group. Identify any subjects that are over or undersubscribed, identify the students who have been allocated to one subject group only and those who have not been allocated to any group. Print out this information. 

TASK 3 — Identify spare places in subject groups. 
Using your results from TASK 2, print out the number of spare places for each subject. Any group that has fewer than 20 students has spare places. Calculate the total number of spare places and the total number of unallocated student choices. Show whether the number of spare places available is enough to cover the unallocated choices.

# Guide to understanding the program
The code has been separated into 3 sections using docstrings, each corresponding to a task outlined by the pre-release material. The comments in the code further divide it into the outlined sub-tasks.

The only potentially confusing part (to me currently) is usage of the nested WHILE loop in task 1. I have added it there to deal with the possibility of people entering wrong data as their subject choices. More error checks could have been done...but there's 18 hours left till the exam so I don't have time :P. Maybe I'll update this later, who knows?

Let me know if there are any issues in the relevant tab on the repo main page. Feel free to make commits if I'm unable to reply at that point of time.
