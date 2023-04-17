def todo(Lesson, lesson_list):
    people = ["Sophia", "Mark", "Ahmed", "Normen", "Noor"]
    for p in people:
        lesson_list.append(Lesson(len(lesson_list), "Lunch", p, "LUNCH"))
    pass