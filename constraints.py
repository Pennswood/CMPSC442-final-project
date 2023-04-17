from optapy import constraint_provider
from optapy.score import HardSoftScore, HardMediumSoftScore, SimpleScore
from optapy.constraint import ConstraintFactory, Joiners
from domain import Lesson
from datetime import datetime, date, timedelta

# Trick since timedelta only works with datetime instances
today = date.today()


def within_30_minutes(lesson1: Lesson, lesson2: Lesson):
    between = datetime.combine(today, lesson1.timeslot.end_time) - datetime.combine(today, lesson2.timeslot.start_time)
    return timedelta(minutes=0) <= between <= timedelta(minutes=30)


# Type annotation not needed, but allows you to get autocompletion
@constraint_provider
def define_constraints(constraint_factory: ConstraintFactory):
    return [
        # Hard constraints
        room_conflict(constraint_factory),
        neccessary_equipment_conflict(constraint_factory),
        teacher_conflict(constraint_factory),
        # lunch_constraint(constraint_factory),
        # Soft constraints
        student_group_conflict(constraint_factory),
        teacher_room_stability(constraint_factory),

        student_group_subject_variety(constraint_factory)
    ]


def neccessary_equipment_conflict(constraint_factory: ConstraintFactory):
    # A room can accommodate at most one lesson at the same time.
    return constraint_factory \
        .for_each(Lesson) \
        .filter(lambda lesson: (lesson.student_group == "CMPSC" and "Compute" not in lesson.room.name) \
        or ((lesson.student_group != "CMPSC" and lesson.student_group != "LUNCH") and "General" not in lesson.room.name) \
        or (lesson.student_group == "LUNCH" and "Cafe" not in lesson.room.name)) \
        .penalize("Equipment conflict", HardSoftScore.ONE_HARD)

def lunch_constraint(constraint_factory: ConstraintFactory):
    # A room can accommodate at most one lesson at the same time.
    return constraint_factory \
        .for_each(Lesson) \
        .filter(lambda lesson: (lesson.timeslot.start_time<datetime.time(hour=11) or lesson.timeslot.start_time>datetime.time(hour=14)) \
            and  (lesson.student_group == "LUNCH")) \
        .penalize("Lunch conflict", HardSoftScore.ONE_HARD)

def room_conflict(constraint_factory: ConstraintFactory):
    # A room can accommodate at most one lesson at the same time.
    return constraint_factory \
        .for_each(Lesson) \
        .join(Lesson,
              # ... in the same timeslot ...
              Joiners.equal(lambda lesson: lesson.timeslot),
              # ... in the same room ...
              Joiners.equal(lambda lesson: lesson.room),
              # form unique pairs
              Joiners.less_than(lambda lesson: lesson.id)
              ) \
        .penalize("Room conflict", HardSoftScore.ONE_HARD)

def teacher_conflict(constraint_factory: ConstraintFactory):
    # A teacher can teach at most one lesson at the same time.
    return constraint_factory \
        .for_each(Lesson) \
        .join(Lesson,
              Joiners.equal(lambda lesson: lesson.timeslot),
              Joiners.equal(lambda lesson: lesson.teacher),
              Joiners.less_than(lambda lesson: lesson.id)
              ) \
        .penalize("Teacher conflict", HardSoftScore.ONE_HARD)


def student_group_conflict(constraint_factory: ConstraintFactory):
    # Encourage students of the same class to study together
    return constraint_factory \
        .for_each(Lesson) \
        .join(Lesson,
              Joiners.equal(lambda lesson: lesson.timeslot),
              Joiners.equal(lambda lesson: lesson.subject),
              Joiners.less_than(lambda lesson: lesson.id)
              ) \
        .reward("Student group reward", HardSoftScore.ONE_SOFT)


def teacher_room_stability(constraint_factory: ConstraintFactory):
    # A teacher prefers to teach in the same room
    return constraint_factory \
        .for_each(Lesson) \
        .join(Lesson,
              Joiners.equal(lambda lesson: lesson.teacher),
              Joiners.less_than(lambda lesson: lesson.id)
              ) \
        .filter(lambda lesson1, lesson2: lesson1.room != lesson2.room) \
        .penalize("Teacher room stability", HardSoftScore.ONE_SOFT)




def student_group_subject_variety(constraint_factory: ConstraintFactory):
    # A student group dislikes consequtive study sessions.
    return constraint_factory \
        .for_each(Lesson) \
        .join(Lesson,
              Joiners.equal(lambda lesson: lesson.teacher),
              Joiners.equal(lambda lesson: lesson.timeslot.day_of_week)
              ) \
        .filter(within_30_minutes) \
        .penalize("Student group subject variety", HardSoftScore.ONE_SOFT)
