import questions
import player
from prettytable import PrettyTable
import time

class Game:

    question = questions.Questions('questions.txt')
    prizes = PrettyTable()
    player = player.Player

    def __init__(self):

        self.display_rules()

        self.display_with_transition('''Welcome to who wanna be a millonarie!!\n What\'s your name?\n'''
        )
        player_name = input()
        self.player.player_name = player_name

        self.display_with_transition(f'''Well {player_name} let\'s start with the game!\nYour first question is:''')
        self.ask_question()
    
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
        
        self.answer_question(question)

    def answer_question(self, question):

        options = question['options']
        answer = question['answer']

        player_asnwer = input(f'{self.player.player_name} What\'s your answer:\n').upper()
        while(player_asnwer != 'A' 
              and player_asnwer != 'B'
              and player_asnwer != 'D'
              and player_asnwer != 'C'):
            print('Invalid option please enter your option (A, B, C ,D)')
            player_asnwer = input(f'{self.player.player_name} What\'s your answer:\n').upper
        
        match player_asnwer:
            case 'A':
                player_asnwer = options[0]
            case 'B':
                player_asnwer = options[1]
            case 'C':
                player_asnwer = options[2]
            case 'D':
                player_asnwer = options[3]

        print(player_asnwer)

        if (player_asnwer == answer):
            print(f'''Congrat\'s {self.player.player_name} you got it rigth!!
            Your next question is:\n''')
        else:
            print(f'Sorry {self.player.player_name} but you got it wrong, good luck next time!')
        
        self.ask_question()

    def display_rules(self):

        self.prizes.field_names = ['Question number', 'Question value']
        self.prizes.add_rows(
            [
                ['1', '$500'],
                ['2', '$1,000'],
                ['3', '$2,000'],
                ['4', '$3,000'],
                ['5', '$5,000'],
                ['6', '$7,500'],
                ['7', '$10,000'],
                ['8', '$15,000'],
                ['9', '$25,000'],
                ['10', '$50,000'],
                ['11', '$75,000'],
                ['12', '$100,000'],
                ['13', '$250,000'],
                ['14', '$500,000'],
                ['15', '$1,000,000'],
            ]
        )
        print(self.prizes)


    def display_with_transition(self, text, delay=0.1):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)