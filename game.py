import questions
import player

class Game:

    question = questions.Questions('questions.txt')
    player = player.Player

    def __init__(self, name_of_player):
        self.player(name_of_player)
    
    def ask_question(self):
        question = self.question.throw_random_question()

        print(question['question'])
        print('Your options are:')
        option_count = 0
        for option in question['options']:
            match option_count:
                case 0:
                    print(f'A) {option}')
                case 1:
                    print(f'B) {option}')
                case 2:
                    print(f'C) {option}')
                case 3:
                    print(f'D) {option}')
            option_count += 1
