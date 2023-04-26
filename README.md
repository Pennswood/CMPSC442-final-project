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
- OptaPy
  - OptaPy uses constraints to solve optimization problems, like scheduling.
  - OptaPy has a method called "room assignments," which assigns teachers' classes timeslots to rooms in schools.
    - We updated this method to instead generate a user's schedule based on constraints.
  - We created a set of constraints for OptaPy (which can be seen in `constraints.py`):
    - Hard constraints (must be inforced):
      - Two students cannot use the same room at the same time
      - Rooms must be used for the appropriate tasks
      - A teacher cannot teach two classes at the same time
    - Soft constraints (do not necessarily have to be enforced):
      - Students of the class can study together
      - Teachers can choose to be in the same room for multiple classes
      - Students may prefer not to study back-to-back in their schedule
- RBES (Rule-Based Expert System)
  - RBES creates recommendations based on a set of rules, which can be updated.
  - RBES was tested using merged data to apply rules and generate recommendations.
  - We created a set of rules (which can be seen in additional_todo.py):
    - If calories are less than 1000, add a meal
    - If total steps are less than 5,000 or total distance is less than 5 miles, add exercise
    - If minutes asleep are less than 240, or total steps are greater than 25,000, or total distance is greater than 15 miles, add sleep
- How OptaPy and RBES were brought together:
  - 

### Data Used:
- We used Fitbit data (from Kaggle) to source data for many different things, like:
  - Steps walked, active minutes, calories, minutes asleep, and more.
- We also used data from some group members, of their class schedules for a week.
  - The class schedule data is in the file `schedule.csv`.
- The Fitbit data was merged with the class schedule data.
  - The merged data can be seen in the file `Merged.csv`.

---
# Instructions For Using Program
- For OptaPy:
  - [Install Python 3.9 or later.](https://www.python.org/downloads/)
  - [Install JDK 11 or later](https://adoptium.net/) with the environment variable `JAVA_HOME` configured to the JDK installation directory.
- Add/edit any constraints for OptaPy in `constraints.py`.
- Add/edit any rules for RBES in `additional_todo.py`.
- Add/edit any data in `schedule.csv` and `Merged.csv`.

### Running the Application:
1. Git clone the optapy-quickstarts repo and navigate to this directory:
```
$ git clone https://github.com/optapy/optapy-quickstarts.git
$ cd optapy-quickstarts/school-timetabling
```
2. Activate a virtual environment
```
$ python -m venv venv
$ . venv/bin/activate
```
3. Install the quickstart requirements to the virtual environment
```
$ pip install -r requirements.txt
```
4. Run the application
```
$ python main.py
```
Optapy will solve the schedule and print it when finished:
|------------|------------|------------|------------|
|            | Room A     | Room B     | Room C     |
|------------|------------|------------|------------|
| SAT 08:30: |            | Math       | History    |
|            |            | A. Turing  | I. Jones   | NEED TO EDIT THIS STILL
|            |            | 9th grade  | 10th grade |
|------------|------------|------------|------------|
| SAT 09:30: |            | Math       | History    |
|            |            | A. Turing  | I. Jones   |
|            |            | 10th grade | 9th grade  |
|------------|------------|------------|------------|
| SAT 10:30: |            | Math       | English    |
|            |            | A. Turing  | I. Jones   |
|            |            | 10th grade | 9th grade  |
|------------|------------|------------|------------|
| SAT 11:30: | Math       | Spanish    |            |
|            | A. Turing  | P. Cruz    |            |
|            | 10th grade | 9th grade  |            |
|------------|------------|------------|------------|
| SAT 12:30: | Math       | English    |            |
|            | A. Turing  | P. Cruz    |            |
|            | 9th grade  | 10th grade |            |
|------------|------------|------------|------------|
| SAT 13:30: | Physics    | Spanish    |            |
|            | M. Curie   | P. Cruz    |            |
|            | 9th grade  | 10th grade |            |
|------------|------------|------------|------------|
| SAT 14:30: | Chemistry  |            | English    |
|            | M. Curie   |            | I. Jones   |
|            | 10th grade |            | 9th grade  |
|------------|------------|------------|------------|
| SAT 15:30: | Physics    | Spanish    |            |
|            | M. Curie   | P. Cruz    |            |
|            | 10th grade | 9th grade  |            |
|------------|------------|------------|------------|
| SAT 16:30: | French     |            | Biology    |
|            | M. Curie   |            | C. Darwin  |
|            | 10th grade |            | 9th grade  |
|------------|------------|------------|------------|
| TUE 14:30: | Chemistry  | Geography  |            |
|            | M. Curie   | C. Darwin  |            |
|            | 9th grade  | 10th grade |            |
|------------|------------|------------|------------|
