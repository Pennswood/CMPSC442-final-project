# **Smart Planner**
By Normen Yu, Kiernan Lavelle, Ahmad Bakar, Mark Vernachio, Noor Sanusi, and Sophie Newlin

---

The Smart Planner was created to help students who have overwhelming schedules. The goal was to create an optimized schedule for students, by prioritizing classes and health. 

---
# **Goals, Environment, and Adaptation**

### Goals
- Create a schedule that maximizes productivity, given a to-do list and a person's health/mood.
  - Health and mood will be based on things like heart rate, amount of sleep, etc.
- Define the exact objective function.
- Identify good data and strategies, to find the best possible schedule.

### Environment
- It would be a Smart Planner App, that could be used on a phone, computer, etc.
- Be able to access and process fitbit data.
- Be able to set priority levels on tasks.
- Be able to receive updates from the user regarding changes in emotions or moods.
- Be able to reschedule tasks in the schedule accordingly, based on data received and priority levels. 

### Adaptation
- In the future, we seek to design data collection strategies to identify how productive users while using the schedule our planner creates.
- Once a week (or at the command of an administrator), the pipeline will cycle through data and make adjustments to training weights or RBES logic to deal with temporal difference and societal changes that may affect the schedule.

---
# **Design and Implementation**
![diagram](readmeDiagram.png)
This is a diagram of our system design implementation.
### Methods Used:
- We used both OptaPy and RBES to generate the schedule.
  - OptaPy uses constraints to solve optimization problems, like scheduling.
  - RBES creates recommendations based on a set of rules, which can be updated.
- We created a set of constraints for OptaPy, including hard constraints and soft constraints.
  - Hard constraints (must be inforced):
    - Two students cannot use the same room at the same time
    - Rooms must be used for the appropriate tasks
    - A teacher cannot teach two classes at the same time
  - Soft constraints (do not necessarily have to be enforced):
    - Students of the class can study together
    - Teachers can choose to be in the same room for multiple classes
    - Students may prefer not to study back-to-back in their schedule

### Data Used:
- We used Fitbit data (from Kaggle) to source data for many different things, like:
  - Steps walked, active minutes, calories, minutes asleep, and more.
- We also used data from some group members, of their class schedules for a week.

---
# Instructions For Using Program
- For OptaPy:
  - [Install Python 3.9 or later.](https://www.python.org/downloads/)
  - [Install JDK 11 or later](https://adoptium.net/) with the environment variable `JAVA_HOME` configured to the JDK installation directory.
- Add/edit any constraints for OptaPy in constraints.py.
- Add/edit any rules for RBES in additional_todo.py
