import getData #previously test.py

def todo(Lesson, lesson_list):
    people = ['Sophie', 'Mark', 'Ahmad', 'Normen', 'Noor']
    for p in people:
        TotalSteps_1, TotalDistance_1, Calories_1, TotalMinutesAsleep_1 = getData.get_data_byname(p, '4/29/2016') 
        TotalSteps_2, TotalDistance_2, Calories_2, TotalMinutesAsleep_2 = getData.get_data_byname(p, '4/30/2016') 
        #lesson_list.append(Lesson(len(lesson_list), "Study", p, "Study"))
        if (Calories_1 < 1000):
            lesson_list.append(Lesson(len(lesson_list), "Meal_1", p, "MEAL_1")) #combine lunch/dinner/breakfast
        if ((TotalSteps_1 < 5000) or (TotalDistance_1 < 5)): 
            lesson_list.append(Lesson(len(lesson_list), "Exercise_1", p, "EXERCISE_1"))
        if ((TotalMinutesAsleep_1 < 240) or (TotalSteps_1 > 25000) or (TotalDistance_1 > 15 )): #or 360 mins of sleep 
            lesson_list.append(Lesson(len(lesson_list), "Sleep_1", p, "SLEEP_1"))
        #same thing but day 2
        if (Calories_2 < 1000):
            lesson_list.append(Lesson(len(lesson_list), "Meal_2", p, "MEAL_2")) 
        if ((TotalSteps_2 < 5000) or (TotalDistance_2 < 5)): 
            lesson_list.append(Lesson(len(lesson_list), "Exercise_2", p, "EXERCISE_2"))
        if ((TotalMinutesAsleep_2 < 240)  or (TotalSteps_2 > 25000) or (TotalDistance_2 > 15 )):
            lesson_list.append(Lesson(len(lesson_list), "Sleep_2", p, "SLEEP_2")) 
    pass
