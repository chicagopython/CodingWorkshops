The organizers of Project Nights need your help! Grouping people for project night team project is a manual task. Why do it manually, when we can automate it? We open the problem to you.

We want a person to record this data as people walk through the door so they can ask two simple questions in order to assign people into groups. We want to take the output of this program and drop the text into Slack to alert everyone that they have been assigned a group. This is the general way a user would interact with the tool:

- The program asks if we want to record a new person.
- If answer is Yes,
  - It asks for the slack handle of the attendee
- Next the program asks “Give us a ballpark number of how many lines of Python (or similar) code have you written in your lifetime? Just looking for a rough estimate!”
The program records the slack handle and the number (LINECOUNT).
  - Handle if LINECOUNT is not a number.
  - Go back to step 1
- If the answer is No (after you have recorded enough to create a few groups of 4)  
    - find the median of the LINECOUNTs for all the persons recorded
- Output groups of four such that each group contains
  - 2 person who have written less than median lines of code
  - 2 person who has written more than written more than median

### Bonus:
* Add a step to check if the total number of persons recorded has reached 48. On reaching 48 it stops taking further input and creates the final groups.
* Add unit tests
* Use the cmd library and textwrap library for cleaner input output
* Whiteboard your design on what will it take to make this into a slack bot that automatically creates the group. Take a picture of your design and tweet  solution to @chicagopython with twitter handles of all your teammates.
* Make up a set of conference room names and assign each group to a random room
