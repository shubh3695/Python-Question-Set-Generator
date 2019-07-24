from json import load
from models import Question, QuestionSet, Requirements, LoadedModel


##########################
# Generic Input Mapper from JSon to RequiredModel
##########################

class InputHandler:

    def __init__(self):
        with open('input4.json') as json_file:
            self.data = load(json_file)
            self.loaded_model: LoadedModel = LoadedModel()
            self.map_json()

    def map_json(self):
        questions = []
        for question in self.data["questions"]:
            questions.append(Question(question["id"], question["difficulty"], question["marks"]))
        question_set = QuestionSet(self.data["questionsSize"], questions)
        requirements = self.map_total_marks(self.data["requirements"])
        self.loaded_model = LoadedModel(question_set, requirements)

    def get_loaded_results(self) -> LoadedModel:
        return self.loaded_model

    @staticmethod
    def map_total_marks(requirement) -> Requirements:
        total = requirement["total"]
        return Requirements(total, requirement["easy"] * 0.01 * total, requirement["medium"] * 0.01 * total,
                            requirement["hard"] * total * 0.01)



