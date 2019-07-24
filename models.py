
##########################
# Generic Models to keep type safety
##########################


class Question:
    def __init__(self, q_id, difficulty, marks):
        self.id = q_id
        self.difficulty = difficulty
        self.marks = marks


class Requirements:
    def __init__(self, total, easy, medium, hard):
        self.total = total
        self.easy = int(easy)
        self.medium = int(medium)
        self.hard = int(hard)


class QuestionSet:
    def __init__(self, size, questions):
        self.size = size
        self.questions = questions


class LoadedModel:
    def __init__(self, question_set: QuestionSet = None, requirements: Requirements = None):
        self.question_set = question_set
        self.requirements = requirements

    @classmethod
    def __init_subclass__(cls):
        cls(QuestionSet(0, []), Requirements(0, 0, 0, 0))
