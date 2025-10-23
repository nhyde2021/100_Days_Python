from multiprocessing.connection import answer_challenge


class Question:

    def __init__(self, text, answer):
        self.text = text
        self.answer = answer
