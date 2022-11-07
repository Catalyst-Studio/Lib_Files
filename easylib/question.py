import random


class question_asker:
    questions = []
    answers = []

    def __init__(self, *args):
        """Initializes the Question Asker"""
        for questionn in args:
            self.questions.append(questionn)

    def ask(self, index: int = 0, keep: bool = False):
        """Asks a specific question and gives back the answer and question"""
        answer = input(self.questions[index])
        self.answers.append({"answer": answer, "question": self.questions[index]})
        if not keep:
            self.questions.pop(index)
        return {"answer": answer, "question": self.questions[index]}

    def append(self, *args):
        """Adds a question to the questions to be asked"""
        for questionn in args:
            self.questions.append(questionn)

    def remove(self, item: str):
        """Removes a question from the questions to be asked"""
        self.questions.remove(item)

    def ask_all(self):
        """Asks all the questions added to the Question List"""
        answers = []
        for questionn in self.questions:
            answer = input(questionn)
            answers.append({"question": questionn, "answer": answer})
            self.answers.append({"question": questionn, "answer": answer})
        return answers

    def get_answer(self, index: int):
        """Gets a specific answer"""
        return self.answers[index]

    def get_all_answers(self):
        """Returns a list of all answers"""
        return self.answers

    def ask_random(self, append: bool = False):
        """Asks a random question from the list of questions to be asked"""
        question = random.choice(self.questions)
        answer = input(question)
        if append:
            self.answers.append(answer)
        return {"question": question, "answer": answer}
