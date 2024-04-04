class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        user_guess = input(f"Q.{self.question_number}: {question.text}. (True/False)?: ").lower()
        self.check_answer(question.answer, user_guess)

    def check_answer(self, answer, user_guess):
        if answer.lower() == user_guess:
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {answer}")
        print(f"Your current score is: {self.score}/{self.question_number}. \n\n")
