import questions
import player
from prettytable import PrettyTable
import time
import os
import platform
import sys

class Game:

    question = questions
    prizes = PrettyTable()
    player = player.Player
    language = ''

    def __init__(self):
        # Ask the player for the language and validate the input
        self.display_with_transition('Please select your language | Porfavor elige tu idioma\nA) English\nB) Español')
        language = input().upper()
        while(language != 'A' and language != 'B'):
            self.display_with_transition('Invalid option | Opcion invalida\nPlease enter A or B | Porfavor ingresa A o B')
            language = input().upper()
        self.language = language
        self.clear_console()
        # Run game with selected language
        if(language == 'A'):
            self.question = questions.Questions('questions.txt')
            self.display_with_transition("""
░█░█░█░█░█▀█░░░█░█░█▀█░█▀█░▀█▀░█▀▀░░░▀█▀░█▀█░░░█▀▄░█▀▀░░░█▀█░░░█▄█░▀█▀░█░░░█░░░▀█▀░█▀█░█▀█░█▀█░▀█▀░█▀▄░█▀▀░▀▀█
░█▄█░█▀█░█░█░░░█▄█░█▀█░█░█░░█░░▀▀█░░░░█░░█░█░░░█▀▄░█▀▀░░░█▀█░░░█░█░░█░░█░░░█░░░░█░░█░█░█░█░█▀█░░█░░█▀▄░█▀▀░░▀░
░▀░▀░▀░▀░▀▀▀░░░▀░▀░▀░▀░▀░▀░░▀░░▀▀▀░░░░▀░░▀▀▀░░░▀▀░░▀▀▀░░░▀░▀░░░▀░▀░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀░▀░▀░▀░▀▀▀░▀░▀░▀▀▀░░▀░
""", 0.001)

            self.display_with_transition('''Welcome to who wanna be a millonarie!!\nWhat\'s your name?''')
            player_name = input()
            self.player.player_name = player_name
            self.clear_console()

            self.display_with_transition(f'''Well {player_name} let\'s start with the game!\nYour first question is:''')
            self.ask_question()
        else:
            self.question = questions.Questions('preguntas.txt')
            self.display_with_transition("""
░▄▀▄░█░█░▀█▀░█▀▀░█▀█░░░▄▀▄░█░█░▀█▀░█▀▀░█▀▄░█▀▀░░░█▀▀░█▀▀░█▀▄░░░█▄█░▀█▀░█░░░█░░░█▀█░█▀█░█▀█░█▀▄░▀█▀░█▀█░▀▀█
░█\█░█░█░░█░░█▀▀░█░█░░░█\█░█░█░░█░░█▀▀░█▀▄░█▀▀░░░▀▀█░█▀▀░█▀▄░░░█░█░░█░░█░░░█░░░█░█░█░█░█▀█░█▀▄░░█░░█░█░░▀░
░░▀\░▀▀▀░▀▀▀░▀▀▀░▀░▀░░░░▀\░▀▀▀░▀▀▀░▀▀▀░▀░▀░▀▀▀░░░▀▀▀░▀▀▀░▀░▀░░░▀░▀░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀░▀░▀░▀░▀░▀░▀▀▀░▀▀▀░░▀░
""", 0.001)

            self.display_with_transition('Bienvenido a quien quiere ser millonario!!\n¿Como te llamas?')
            player_name = input()
            self.player.player_name = player_name
            self.clear_console()

            self.display_with_transition(f'Bueno {player_name} empecemos con el juego!\nTu primera pregunta es:')
            self.ask_question()

    def ask_question(self):
        # Get the question and print it
        question = self.question.throw_random_question()
        self.display_with_transition(f'{question['question']}')

        # Parse the options and print it
        if(self.language == 'A'):
            self.display_with_transition('Your options are:')
            options = question['options']
            self.sleep
            self.display_with_transition(f'A) {options[0]}\nB) {options[1]}\nC) {options[2]}\nD) {options[3]}')
        
            # Call the answer_question method to handle the user input
            self.answer_question(question)
        else:
            self.display_with_transition('Tus opciones son:')
            options = question['options']
            self.sleep
            self.display_with_transition(f'A) {options[0]}\nB) {options[1]}\nC) {options[2]}\nD) {options[3]}')
        
            # Call the answer_question method to handle the user input
            self.answer_question(question)

    def answer_question(self, question):
        # Create variables with the questions options and answer to compare later with the user input
        options = question['options']
        answer = question['answer']

        # Get the player input and check if is valid with the while statement
        if (self.language == 'A'):
            player_asnwer = input(f'{self.player.player_name} What\'s your answer:\n').upper()
            while(player_asnwer != 'A' 
                and player_asnwer != 'B'
                and player_asnwer != 'D'
                and player_asnwer != 'C'):
        
                print('Invalid option, please enter a valid option (A, B, C ,D)')
                player_asnwer = input(f'{self.player.player_name} What\'s your answer:\n').upper
        
            # Match the player input with the available options
            match player_asnwer:
                case 'A':
                    player_asnwer = options[0]
                case 'B':
                    player_asnwer = options[1]
                case 'C':
                    player_asnwer = options[2]
                case 'D':
                 player_asnwer = options[3]

            # Check if the player answer if rigth or wrong
            if (player_asnwer == answer):
                # If rigth the games continues
                self.display_with_transition(f'Congrat\'s {self.player.player_name} you got it rigth!!\n{question['explanation']}')
                self.sleep(3)
                self.clear_console()
                self.display_with_transition('Your next question is:')
                self.ask_question()
            else:
                # If wrong the player is ask to restar the game or close the app
                self.display_with_transition(f'''Sorry {self.player.player_name} but you got it wrong\n
The rigth answer was "{question['explanation']}"\nGood luck next time!!''')
                self.sleep(3)
                self.clear_console()
                self.display_with_transition(f'{self.player.player_name} would you like to play again? (Yes/No)')
                yes_no = self.yes_no()
                if (yes_no == 'YES'):
                    self.clear_console()
                    self.__init__()
                else:
                    self.display_with_transition("""
░▀█▀░█░█░█▀█░█▀█░█░█░█▀▀░░░█▀▀░█▀█░█▀▄░░░█▀█░█░░░█▀█░█░█░▀█▀░█▀█░█▀▀░█░█
░░█░░█▀█░█▀█░█░█░█▀▄░▀▀█░░░█▀▀░█░█░█▀▄░░░█▀▀░█░░░█▀█░░█░░░█░░█░█░█░█░▀░▀
░░▀░░▀░▀░▀░▀░▀░▀░▀░▀░▀▀▀░░░▀░░░▀▀▀░▀░▀░░░▀░░░▀▀▀░▀░▀░░▀░░▀▀▀░▀░▀░▀▀▀░▀░▀
""")
                    self.sleep()
                    sys.exit()
        else:
            player_asnwer = input(f'{self.player.player_name} ¿Cual es tu respuesta?:\n').upper()
            while(player_asnwer != 'A' 
                and player_asnwer != 'B'
                and player_asnwer != 'D'
                and player_asnwer != 'C'):
        
                print('Opcion invalida, porfavor ingresa una opcion valida (A, B, C ,D)')
                player_asnwer = input(f'{self.player.player_name} ¿Cual es tu respuesta?:\n').upper
        
            # Match the player input with the available options
            match player_asnwer:
                case 'A':
                    player_asnwer = options[0]
                case 'B':
                    player_asnwer = options[1]
                case 'C':
                    player_asnwer = options[2]
                case 'D':
                 player_asnwer = options[3]

            # Check if the player answer if rigth or wrong
            if (player_asnwer == answer):
                # If rigth the games continues
                self.display_with_transition(f'Felicidades {self.player.player_name} tu respuesta es correcta!!\n{question['explanation']}')
                self.sleep(3)
                self.clear_console()
                self.display_with_transition('Tu siguiente pregunta es:')
                self.ask_question()
            else:
                # If wrong the player is ask to restar the game or close the app
                self.display_with_transition(f'''Lo siento {self.player.player_name} pero es incorrecto\n
La respuesta correcta era {answer}\n{question['explanation']}\nBuena suerte la proxima vez!!''')
                self.sleep(3)
                self.clear_console()
                self.display_with_transition(f'{self.player.player_name} ¿Te gustaria jugar otra vez? (Si/No)')
                yes_no = self.yes_no()
                if (yes_no == 'SI'):
                    self.clear_console()
                    self.__init__()
                else:
                    self.display_with_transition("""
░█▀▀░█▀▄░█▀█░█▀▀░▀█▀░█▀█░█▀▀░░░█▀█░█▀█░█▀▄░░░▀▀█░█░█░█▀▀░█▀█░█▀▄░█░█
░█░█░█▀▄░█▀█░█░░░░█░░█▀█░▀▀█░░░█▀▀░█░█░█▀▄░░░░░█░█░█░█░█░█▀█░█▀▄░▀░▀
░▀▀▀░▀░▀░▀░▀░▀▀▀░▀▀▀░▀░▀░▀▀▀░░░▀░░░▀▀▀░▀░▀░░░▀▀░░▀▀▀░▀▀▀░▀░▀░▀░▀░▀░▀
""")
                    self.sleep()
                    sys.exit()

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

    def prizes(self):
        if (self.language == 'A'):
            prize  = 0
            if (self.player.player_points == 5):
                prize = 5000
            elif (self.player.player_points == 10):
                prize = 50000
            elif (self.player.player_points == 15):
                prize = 1000000
            if (self.player.player_points == 5 or self.player.player_points == 10):
                self.display_with_transition(f'''{self.player.player_name} you have reach {self.player.player_points} points\n
                Would you like to retire with your prize?''')
                player_input = self.yes_no()
                if (player_input == 'A'):
                    self.display_with_transition(f'Congrat\'s you won ${prize}!!!!')
                    self.display_with_transition("""
░▀█▀░█░█░█▀█░█▀█░█░█░█▀▀░░░█▀▀░█▀█░█▀▄░░░█▀█░█░░░█▀█░█░█░▀█▀░█▀█░█▀▀░█░█
░░█░░█▀█░█▀█░█░█░█▀▄░▀▀█░░░█▀▀░█░█░█▀▄░░░█▀▀░█░░░█▀█░░█░░░█░░█░█░█░█░▀░▀
░░▀░░▀░▀░▀░▀░▀░▀░▀░▀░▀▀▀░░░▀░░░▀▀▀░▀░▀░░░▀░░░▀▀▀░▀░▀░░▀░░▀▀▀░▀░▀░▀▀▀░▀░▀
""")
                    self.sleep()
                    sys.exit()
        else:
            prize  = 0
            if (self.player.player_points == 5):
                prize = 5000
            elif (self.player.player_points == 10):
                prize = 50000
            elif (self.player.player_points == 15):
                prize = 1000000
            if (self.player.player_points == 5 or self.player.player_points == 10):
                self.display_with_transition(f'''{self.player.player_name} alcanzaste los {self.player.player_points} puntos\n
                ¿Te gustaria retirarte con tu premio?''')
                player_input = self.yes_no()
                if (player_input == 'A'):
                    self.display_with_transition(f'Felicidades ganaste ${prize}!!!!')
                    self.display_with_transition("""
░█▀▀░█▀▄░█▀█░█▀▀░▀█▀░█▀█░█▀▀░░░█▀█░█▀█░█▀▄░░░▀▀█░█░█░█▀▀░█▀█░█▀▄░█░█
░█░█░█▀▄░█▀█░█░░░░█░░█▀█░▀▀█░░░█▀▀░█░█░█▀▄░░░░░█░█░█░█░█░█▀█░█▀▄░▀░▀
░▀▀▀░▀░▀░▀░▀░▀▀▀░▀▀▀░▀░▀░▀▀▀░░░▀░░░▀▀▀░▀░▀░░░▀▀░░▀▀▀░▀▀▀░▀░▀░▀░▀░▀░▀
""")
                    self.sleep()
                    sys.exit() 

    def display_with_transition(self, text, delay=0.009):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()

    def yes_no(self):
        player_input = input().upper()
        if (self.language == 'A'):
            while(player_input != 'YES' and player_input != 'NO'):
                self.display_with_transition('Invalid option plese enter: Yes or No')
                player_input = input().upper()
            return player_input
        else:
            while(player_input != 'SI' and player_input != 'NO'):
                self.display_with_transition('Opcion invalida, porfavor escribe: Si o No')
                player_input = input().upper()
            return player_input             

    def clear_console(self):
        system = platform.system()
        if system == 'Windows':
            os.system('cls')
        elif system == 'Linux' or system == 'Darwin':  # Darwin is macOS
            os.system('clear')
    
    def sleep(self, seconds=2):
        time.sleep(seconds)