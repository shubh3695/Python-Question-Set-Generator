from input_analyser import InputHandler
from models import LoadedModel
from utils import generate_dp


##########################
# Core Controller for Generating Functions
##########################

class Generator:
    def __init__(self):
        self.model: LoadedModel = InputHandler().get_loaded_results()

    def resolve_question_by_type(self, level: str, limit: int) -> []:
        questions = [question for question in self.model.question_set.questions if
                     question.difficulty == level]
        if len(questions) == 0:
            raise Exception("No Question Set Available for "+level.capitalize()+". Please Review.")
        return generate_dp(questions, limit)

    def analyse_results(self) -> []:
        """
        :return: list of combinations of Easy, Medium, Hard Question for given Sum
        """
        list_easy = self.resolve_question_by_type('easy', self.model.requirements.easy)
        if len(list_easy) == 0:
            raise Exception("No Combination could be found for Easy Questions.")
        list_medium = self.resolve_question_by_type('medium', self.model.requirements.medium)
        if len(list_medium) == 0:
            raise Exception("No Combination could be found for Medium Questions.")
        list_hard = self.resolve_question_by_type('hard', self.model.requirements.hard)
        if len(list_hard) == 0:
            raise Exception("No Combination could be found for Hard Questions.")
        return [list_easy, list_medium, list_hard]
