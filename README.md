# Cocaine_Stroop_Test
This repository contains an application of a Stroop Test for a future cocaine study. This application is written in Python and uses Psycho Py.
Purpose
The Stroop Task is a widely used cognitive task designed to assess selective attention, cognitive flexibility, and processing speed. In this task, participants are required to respond to the number of words while ignoring conflicting information (e.g., the word's semantic meaning), making it useful for evaluating response accuracy and reaction time (RT) under conditions of cognitive interference.
The Cocaine Stroop Task MRI program will be administered on a study laptop while participants are being scanned in the MRI scanner. Participants must complete the Stroop Task Training Program and the Cocaine Stroop Personalized Word List Interview prior to conducting this procedure.  
The task records the participant’s accuracy and RT in response to congruent versus incongruent word-number stimuli, standard cocaine/crack word-number stimuli, personalized cocaine/crack word-number stimuli, neutral word-number stimuli, and emotion word-number stimuli. Personalized cocaine/crack words will be collected from the participant prior to this procedure via the Cocaine Stroop Personalized Word List Interview.
Participants will be asked to press buttons 1 through 4 on a button-box to indicate how many times a word appears on the screen, regardless of what the word says. For example:

•	Congruent trial: the word “THREE” displayed three times.
•	Incongruent trial: the word “FOUR” displayed three times.
•	Standard Cocaine/Crack word trial: the word “PIPE” displayed two times.
•	Personalized Cocaine/Crack word trial: the word “PLAYSTATION” displayed two times.
•	Neutral word trial: the word “COUCH” displayed one time.
•	Emotion word trial: the word “GUILTY” displayed one time.


Location and Timing
This procedure will take place in an MRI laboratory using a study laptop while the participant is in the MRI scanner. The Cocaine Stroop Personalized Word List Interview and the Stroop Task Training Program must be completed prior to this procedure.
The participant will complete this procedure twice-  at the beginning of the study prior to TMS intervention, and after all TMS sessions are completed. 


Scope
This SOP applies specifically to Protocol #8483. 

Procedures
Requirements – Only follow if using a laptop that does not have the Stroop Task pre-installed 
1.	Laptop (must use Windows 10 or most recent OS, CANNOT use Mac)
2.	The following File Structure inside the computer:
a.	Documents
i.	CoStim
1.	Cocaine_Stroop_Task
2.	Stroop_Task_Training
3.	Python 3.10, or most recent version
4.	PsychoPy v2.4 modern (Python 3.10), or most recent version (https://www.psychopy.org/download.html)
5.	Cocaine Stroop Task Program (https://github.com/vano31/Cocaine_Stroop_Task)
a.	Click Code > Download Zip on the link above to download the zip file if not done so already
b.	Unzip folder, and rename unzipped folder to “Cocaine_Stroop_Task-TEMPLATE”
c.	Move “Cocaine_Stroop_Task-TEMPLATE” to inside Documents > CoStim > Cocaine_Stroop_Task

Session 1
1.	On the laptop meant for the Stroop Test, navigate to Settings > Display > Advanced Display > Choose a Refresh Rate.
2.	Ensure that the Refresh Rate is set to 60 Hz (TASK WILL FAIL IF THIS IS NOT SET).
3.	Navigate to Documents > CoStim > Cocaine_Stroop_Task.
4.	Copy the Folder named “Cocaine_Stroop_Task-TEMPLATE” and paste it in the current folder you are in.
5.	Rename the copied folder to “Cocaine_Stroop_Task_Subject_[INSERT SUBJECT ID NUMBER HERE]”. Enter this folder.
6.	Enter the “personal_words” folder. Open the “list_of_eight_personal_words.xlsx” Excel Sheet.
7.	Remove any words present under the “eight_words” column if they exist. 
8.	Under the “eight_words" column, write all eight words chosen from participant during the Cocaine Stroop Personalized Word List Interview conducted prior to this task. Make sure ALL letters are capitalized. Words should be in rows 2 to 9.
9.	Save the Excel Sheet, then close the Excel Sheet. 
10.	Open PsychoPy. On type right corner of Window, click “Show Coder” Icon (the icon is a striped circle with a white sheet and a red “>” symbol on its bottom right corner). This will open the Coder Window.
11.	If a black window pops up, minimize it.
12.	On top left corner of Coder Window, click “Open” Icon (the icon is an open folder).
13.	In the Open File Window, Navigate to Documents > CoStim > Cocaine_Stroop_Task > Cocaine_Stroop_Task_Subject_[SUBJECT ID]. Within this folder, click the file named “Cocaine_Stroop_Task.py” and press Open.
14.	Code will appear in the Coder Window. DO NOT EDIT CODE IN THE CODER WINDOW- typing code will not be necessary for any part of the task.
15.	On the top of the Coder Window’s Tool Bar, look for the icon that looks like a slider between the words “Pilot” and “Run”. Ensure that the slider is set to “Run.” The “Run” Icon (represented by a play button) should be GREEN. (If “Run” Icon is Orange, the slider is set to “Pilot” and should be changed).
16.	Press the GREEN “Run” Icon. A small window named “Cocaine Study Stroop Task” should appear.
17.	Inside the Cocaine Study Stroop Task Window, type the Subject_ID (should be same ID the folder was named after) and the Session Number (Should be 1). Press OK.
18.	The task will take up the screen. Follow the onscreen instructions.
19.	Whenever the screen is blank, press “b” to move on.
20.	Whenever the screen says “Get Ready,” press “t” to move on.
21.	To quickly close the program, press “q.” This will completely terminate the program and save everything up until the most recent action. Once this is done, the task must be completed all over again.

Session 2
1.	Follow Steps 1-3 in the Session 1 instructions.
2.	Open the Folder named “Cocaine_Stroop_Task_Subject_[SUBJECT ID].”
3.	Follow Steps 10-16 in Session 1 instructions.
4.	Inside the Cocaine Study Stroop Test Window, type the Subject_ID (should be same ID the folder was named after) and the Session Number (Should be 2). Press OK.
5.	Follow Steps 18-21 in Session 1 instructions.




Retrieving Data
1.	To retrieve data for a specific participant, navigate to Documents > CoStim > Cocaine_Stroop_Task > Cocaine_Stroop_Task_Subject_[SUBJECT ID] > data. Enter the “data” folder.
2.	Excel Sheets named “[SUBJECT ID]_[SESSION NUMBER]_Cocaine_Stroop_Task[DATE OF SESSION]” will contain information regarding participant responses to words in show on screen.
3.	Excel Sheets named “[SUBJECT ID]_[SESSION NUMBER]_Intro_Data_Cocaine_Stroop_Task[DATE OF SESSION]” will contain information timestamps for every major on screen event that the participant completes, including when the program was opened.

Sources
1.	https://github.com/vano31/Cocaine_Stroop_Task
2.	https://www.psychopy.org/download.html

