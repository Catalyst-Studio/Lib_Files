import random


class question_asker:
    questions = []
    answers = []

    def __init__(self, *args):
        for questionn in args:
            self.questions.append(questionn)

    def ask(self, index: int = 0, keep: bool = False):
        answer = input(self.questions[index])
        self.answers.append({"answer": answer, "question": self.questions[index]})
        if not keep:
            self.questions.pop(index)
        return {"answer": answer, "question": self.questions[index]}

    def append(self, *args):
        for questionn in args:
            self.questions.append(questionn)

    def remove(self, item: str):
        self.questions.remove(item)

    def ask_all(self):
        answers = []
        for questionn in self.questions:
            answer = input(questionn)
            answers.append({"question": questionn, "answer": answer})
            self.answers.append({"question": questionn, "answer": answer})
        return answers

    def get_answer(self, index: int):
        return self.answers[index]

    def get_all_answers(self):
        return self.answers

    def ask_random(self, append: bool = False):
        question = random.choice(self.questions)
        answer = input(question)
        if append:
            self.answers.append(answer)
        return {"question": question, "answer": answer}
