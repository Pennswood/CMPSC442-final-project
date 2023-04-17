def todo(Lesson, lesson_list):
    people = ["Sophia", "Mark", "Ahmed", "Normen", "Noor"]
    for p in people:
        lesson_list.append(Lesson(len(lesson_list), "Meal", p, "MEAL")) #combine lunch/dinner/breakfast
        lesson_list.append(Lesson(len(lesson_list), "Sleep", p, "SLEEP")) #or rest
        lesson_list.append(Lesson(len(lesson_list), "Study", p, "STUDY"))
        lesson_list.append(Lesson(len(lesson_list), "Exercise", p, "EXERCISE"))
        lesson_list.append(Lesson(len(lesson_list), "Class", p, "CLASS"))
        lesson_list.append(Lesson(len(lesson_list), "Free Time", p, "FREE TIME")) #lowest priority? 
    pass
