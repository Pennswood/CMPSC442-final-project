import datetime

import optapy
from optapy import problem_fact, planning_id, planning_entity, planning_variable, \
    planning_solution, planning_entity_collection_property, \
    problem_fact_collection_property, \
    value_range_provider, planning_score
from optapy.types import HardSoftScore
from datetime import time
from additional_todo import todo

@problem_fact
class Room:
    id: int
    name: str

    def __init__(self, id, name):
        self.id = id
        self.name = name

    @planning_id
    def get_id(self):
        return self.id

    def __str__(self):
        return f"Room(id={self.id}, name={self.name})"


@problem_fact
class Timeslot:
    id: int
    day_of_week: str
    start_time: datetime.time
    end_time: datetime.time

    def __init__(self, id, day_of_week, start_time, end_time):
        self.id = id
        self.day_of_week = day_of_week
        self.start_time = start_time
        self.end_time = end_time

    @planning_id
    def get_id(self):
        return self.id

    def __str__(self):
        return (
                f"Timeslot("
                f"id={self.id}, "
                f"day_of_week={self.day_of_week}, "
                f"start_time={self.start_time}, "
                f"end_time={self.end_time})"
        )


@planning_entity
class Lesson:
    id: int
    subject: str
    teacher: str
    student_group: str
    timeslot: Timeslot
    room: Room

    def __init__(self, id, subject, teacher, student_group, timeslot=None, room=None):
        self.id = id
        self.subject = subject
        self.teacher = teacher
        self.student_group = student_group
        self.timeslot = timeslot
        self.room = room

    @planning_id
    def get_id(self):
        return self.id

    @planning_variable(Timeslot, ["timeslotRange"])
    def get_timeslot(self):
        return self.timeslot

    def set_timeslot(self, new_timeslot):
        self.timeslot = new_timeslot

    @planning_variable(Room, ["roomRange"])
    def get_room(self):
        return self.room

    def set_room(self, new_room):
        self.room = new_room

    def __str__(self):
        return (
            f"Lesson("
            f"id={self.id}, "
            f"timeslot={self.timeslot}, "
            f"room={self.room}, "
            f"teacher={self.teacher}, "
            f"subject={self.subject}, "
            f"student_group={self.student_group}"
            f")"
        )


def format_list(a_list):
    return ',\n'.join(map(str, a_list))


@planning_solution
class TimeTable:
    timeslot_list: list[Timeslot]
    room_list: list[Room]
    lesson_list: list[Lesson]
    score: HardSoftScore

    def __init__(self, timeslot_list, room_list, lesson_list, score=None):
        self.timeslot_list = timeslot_list
        self.room_list = room_list
        self.lesson_list = lesson_list
        self.score = score

    @problem_fact_collection_property(Timeslot)
    @value_range_provider("timeslotRange")
    def get_timeslot_list(self):
        return self.timeslot_list

    @problem_fact_collection_property(Room)
    @value_range_provider("roomRange")
    def get_room_list(self):
        return self.room_list

    @planning_entity_collection_property(Lesson)
    def get_lesson_list(self):
        return self.lesson_list

    @planning_score(HardSoftScore)
    def get_score(self):
        return self.score

    def set_score(self, score):
        self.score = score
    
    def __str__(self):
        return (
            f"TimeTable("
            f"timeslot_list={format_list(self.timeslot_list)},\n"
            f"room_list={format_list(self.room_list)},\n"
            f"lesson_list={format_list(self.lesson_list)},\n"
            f"score={str(self.score.toString()) if self.score is not None else 'None'}"
            f")"
        )

import pandas as pd
def generate_problem():
    our_schedule = pd.read_csv("./schedule.csv")

    lesson_list = []
    for index, row in our_schedule.iterrows():
        lesson_list.append(Lesson(index, row["item"], row["person"], row["location"]))

    # Adds things to the lesson list
    todo(Lesson, lesson_list)

    timeslot_list = [
        Timeslot(1, "SATURDAY", time(hour=8, minute=30), time(hour=9, minute=30)),
        Timeslot(2, "SATURDAY", time(hour=9, minute=30), time(hour=10, minute=30)),
        Timeslot(3, "SATURDAY", time(hour=10, minute=30), time(hour=11, minute=30)),
        Timeslot(4, "SATURDAY", time(hour=11, minute=30), time(hour=12, minute=30)),
        Timeslot(5, "SATURDAY", time(hour=12, minute=30), time(hour=13, minute=30)),
        Timeslot(6, "SATURDAY", time(hour=13, minute=30), time(hour=14, minute=30)),
        Timeslot(7, "SATURDAY", time(hour=14, minute=30), time(hour=15, minute=30)),
        Timeslot(8, "SATURDAY", time(hour=15, minute=30), time(hour=16, minute=30)),
        Timeslot(9, "SATURDAY", time(hour=16, minute=30), time(hour=17, minute=30)),
        Timeslot(10, "SUNDAY", time(hour=8, minute=30), time(hour=9, minute=30)),
        Timeslot(11, "SUNDAY", time(hour=9, minute=30), time(hour=10, minute=30)),
        Timeslot(12, "SUNDAY", time(hour=10, minute=30), time(hour=11, minute=30)),
        Timeslot(13, "SUNDAY", time(hour=11, minute=30), time(hour=12, minute=30)),
        Timeslot(14, "SUNDAY", time(hour=12, minute=30), time(hour=13, minute=30)),
        Timeslot(15, "SUNDAY", time(hour=13, minute=30), time(hour=14, minute=30)),
        Timeslot(16, "SUNDAY", time(hour=14, minute=30), time(hour=15, minute=30)),
        Timeslot(17, "SUNDAY", time(hour=15, minute=30), time(hour=16, minute=30)),
        Timeslot(18, "SUNDAY", time(hour=16, minute=30), time(hour=17, minute=30)),
    ]
    room_list = [
        Room(1, "Compute_1"),
        Room(2, "Compute_2"),
        Room(3, "Compute_3"),
        Room(4, "General_1"),
        Room(5, "General_2"),
        Room(6, "Cafe_1"),
        Room(7, "Cafe_2"),
        Room(8, "Cafe_3")
    ]
    lesson = lesson_list[0]
    lesson.set_timeslot(timeslot_list[0])
    lesson.set_room(room_list[0])

    return TimeTable(timeslot_list, room_list, lesson_list)
