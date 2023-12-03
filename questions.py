import random

class Questions:

    questions = {}
    used_questions = []

    def __init__(self, file_path):
        """
    Initializes the questions state.

    Parameters:
    - file_path (str): The path to the questions file.

    Returns:
    - None

    The function initializes the questions state, including the questions, options, answers and explanations.
    """
        self.questions = self.read_questions_from_file(file_path)

    def read_questions_from_file(self, file_path):
        """
    Reads the questions from the given file path.

    Parameters:
    - file_path (str): The path to the questions file.

    Returns:
    - questions (dict): The questions, options, answers and explanations.

    The function reads the questions from the given file path and returns a dictionary with the questions, options, answers and explanations.
    """
        list_questions = []
       
        with open(file_path, 'r', encoding='utf-8') as file:
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
        """
    Throws a random question from the questions dictionary.

    Parameters:
    - None

    Returns:
    - question (dict): A dictionary representing the question, including options,the correct answer and the explination.

    The function throws a random question from the questions dictionary.
    """    
        unused_questions = [question for question in self.questions.keys() if question not in self.used_questions]

        random_question = random.choice(unused_questions)
        self.used_questions.append(random_question)

        return self.questions[random_question]