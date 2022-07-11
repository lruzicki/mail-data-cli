# Recruitment-task-2022 ŁUKASZ RUZICKI
This is the task in the recruitment process for the position of Intern Python Developer at Profil Software. 

To run the program, open main.py in IDE that can run Python scripts e.g. Visual Studio Code or you can run the Linux terminal.  </br>

For each task, there is separate command written in parentheses, in VSC:
<b> python main.py [--option] [argument] </b>

1. Show incorrect emails (--incorrect-emails, -ic)
Print the number of invalid emails, then one invalid email per line. </br>
Example: <b> python main.py -ic </b>

2. Search emails by text (--search str, -s str)
The Program should take a string argument and print the number of found emails, then one found email per line. </br>
Example: <b> python main.py --search agustin </b>

3. Group emails by domain (--group-by-domain, -gbd)
Group emails by one domain and order domains and emails alphabetically </br>
Example: <b> python main.py -gbd </b>

4. Find emails that are not in the logs file (--find-emails-not-in-logs path_to_logs_file, -feil path_to_logs_file) </br>
Example: <b> python main.py -feil email-sent.logs </b>

You can set stream to file by typing "> file.txt" while running the script
Example: <b> python main.py -file email-sent.logs > task_4_answer.txt </b>

If you do not provide any arguments while running the script ("python main.py") the main menu will open, you will be ask to chose option from displayed menu:

![image](https://user-images.githubusercontent.com/56487722/178326971-c6c24617-e086-4023-af01-cd29b2607c49.png)

You can use few options at the same time, e.g.: <b> python main.py -s agustin -ic </b>

Compared my output with given:

Task 1# gives: "Invalid emails (8)" not "Invalid emails (10)". Probably there is wrong answer in the "task_1_answer.txt" provided by recruiter because the "com" is there 3 times. It should be there only once. </br>
Task 2# same output. </br>
Task 3# same output. </br>
Task 4# same output. </br>
