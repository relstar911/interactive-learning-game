class Quiz:
    def __init__(self):
        self.questions = []
        self.current_question = None
    
    def add_question(self, question, options, correct_answer):
        self.questions.append({
            'question': question,
            'options': options,
            'correct_answer': correct_answer
        })
    
    def start_quiz(self):
        if self.questions:
            self.current_question = self.questions[0]
        else:
            print("No questions available in the quiz.")
    
    def answer_question(self, answer):
        if self.current_question and answer == self.current_question['correct_answer']:
            print("Correct!")
            return True
        else:
            print("Incorrect.")
            return False
