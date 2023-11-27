import random

class Questions:

    questions = {}
    used_questions = []

    def __init__(self, file_path):
        self.questions = self.read_questions_from_file(file_path)

    def read_questions_from_file(self, file_path):
        list_questions = []
        with open(file_path) as file:
            lines = file.readlines()

            for line in lines:
                list_questions.append(line.strip("\n"))

        questions = {}
        question_count = 1
        for i in range(0, len(list_questions), 4):
            question = list_questions[i]
            options = list_questions[i + 1].split(',')
            answer = list_questions[i + 2]
            explanation = list_questions[i + 3]

            questions[question_count] = {
                "question": question,
                "options": options,
                "answer": answer,
                "explanation": explanation,
            }
            question_count += 1

        return questions
    
    def throw_random_question(self):
        unused_questions = [question for question in self.questions.keys() if question not in self.used_questions]

        random_question = random.choice(unused_questions)
        self.used_questions.append(random_question)

        return self.questions[random_question]


# Example usage:
questions_instance = Questions("questions.txt")
random_question = questions_instance.throw_random_question()
print(random_question['question'])