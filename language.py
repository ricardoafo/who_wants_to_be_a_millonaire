import os
import platform
import sys
import time
import questions
import player
class Language:

    # Create variables to use in the game from other classes
    questions = questions
    player = player.Player

    # Create a variable to store the language
    language = ''

    def __init__(self):
        """
    Initializes the Language class and set the language according to the user input.

    Parameters:
    - None

    Returns:
    - None

    The function initializes the Language class and set the language according to the user input.
    """
        self.display_with_transition('Please select your language | Porfavor elige tu idioma\nA) English\nB) Español')
        user_language = input().upper()
        while(user_language != 'A' and user_language != 'B'):
            self.display_with_transition('Invalid option | Opcion invalida\nPlease enter A or B | Porfavor ingresa A o B')
            user_language = input().upper()
        
        if (user_language == 'A'):
            self.language = 'English'
        elif (user_language == 'B'):
            self.language = 'Spanish'

    def greeting_text(self):
        """
    Displays the greeting text, ask for the player name and open the questions file according to the language.

    Parameters:
    - None

    Returns:
    - Questions (class) instance: The function returns an instance of the Questions class. 

    The function displays the greeting text, set the player name in an instance of the Player class
    and open an instance of the Questions class according to the language. Then returns the Questions instance.
    """
        # Clear the console after
        self.clear_console()
        # Show the greeting text
        if (self.language == 'English'):
            self.display_with_transition("""
░█░█░█░█░█▀█░░░█░█░█▀█░█▀█░▀█▀░█▀▀░░░▀█▀░█▀█░░░█▀▄░█▀▀░░░█▀█░░░█▄█░▀█▀░█░░░█░░░▀█▀░█▀█░█▀█░█▀█░▀█▀░█▀▄░█▀▀░▀▀█
░█▄█░█▀█░█░█░░░█▄█░█▀█░█░█░░█░░▀▀█░░░░█░░█░█░░░█▀▄░█▀▀░░░█▀█░░░█░█░░█░░█░░░█░░░░█░░█░█░█░█░█▀█░░█░░█▀▄░█▀▀░░▀░
░▀░▀░▀░▀░▀▀▀░░░▀░▀░▀░▀░▀░▀░░▀░░▀▀▀░░░░▀░░▀▀▀░░░▀▀░░▀▀▀░░░▀░▀░░░▀░▀░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀░▀░▀░▀░▀▀▀░▀░▀░▀▀▀░░▀░
""", 0.001)

            # Ask for the player name
            self.display_with_transition('''Welcome to who wanna be a millonarie!!\nWhat\'s your name?''')
            player_name = input()
            self.player.player_name = player_name
            self.clear_console()

            self.display_with_transition(f'''Well {player_name} let\'s start with the game!\nYour first question is:''')

            return self.questions.Questions('questions.txt')
        elif (self.language == 'Spanish'):
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

            return self.questions.Questions('preguntas.txt')
        else:
            print('Error')

    def options_text(self, question):
        """
    Displays the question options according to the language.

    Parameters:
    - question (dict): A dictionary representing the question, including options,the correct answer and the explination.

    Returns:
    - None 

    The function takes a dictionary representing the question, including options, the correct answer and the explination.
    Then according to the language displays the question options.
    """
        if (self.language == 'English'):
            self.display_with_transition('Your options are:')
            options = question['options']
            self.display_with_transition(f'A) {options[0]}\nB) {options[1]}\nC) {options[2]}\nD) {options[3]}')
        
        elif (self.language == 'Spanish'):
            self.display_with_transition('Tus opciones son:')
            options = question['options']
            self.display_with_transition(f'A) {options[0]}\nB) {options[1]}\nC) {options[2]}\nD) {options[3]}')
        else:
            print('Error')
    
    def answer_question_input_text(self):
        """
    Handles the player answer input according to the language, validates if the input is valid and returns the player answer.

    Parameters:
    - None

    Returns:
    - player_answer (str): The function returns the player answer. 

    The function handles the player answer input according to the language, validates if the input is valid and returns the player answer.
    """
        # Get the player input and check if is valid with the while statement
        if (self.language == 'English'):
            player_answer = input(f'{self.player.player_name} What\'s your answer:\n').upper()
            while(player_answer != 'A' 
                and player_answer != 'B'
                and player_answer != 'D'
                and player_answer != 'C'):
        
                print('Invalid option, please enter a valid option (A, B, C ,D)')
                player_answer = input(f'{self.player.player_name} What\'s your answer:\n').upper()
        elif (self.language == 'Spanish'):
            player_answer = input(f'{self.player.player_name} ¿Cual es tu respuesta?:\n').upper()
            while(player_answer != 'A' 
                and player_answer != 'B'
                and player_answer != 'D'
                and player_answer != 'C'):
        
                print('Opcion invalida, porfavor ingresa una opcion valida (A, B, C ,D)')
                player_answer = input(f'{self.player.player_name} ¿Cual es tu respuesta?:\n').upper()
        else:
            print('Error')

        return player_answer
    
    def answer_question_result_text(self, question, player_answer, answer):
        """
    Validates if the player answer is right or wrong, displays the result according to the language

    Parameters:
    - question (dict): A dictionary representing the question, including options,the correct answer and the explination.
    - player_answer (str): The player answer.
    - answer (str): The right answer.

    Returns:
    - outcome (str): The function returns the outcome of the player answer. 

    The function validates if the player answer is right or wrong, displays the result according to the language
    If the player answer is right the function returns 'right'
    If the player answer is wrong the function asks the player if he wants to restart the game or close the app
    If the player answer is wrong and he wants to restart the game the function returns 'restart'
    If the player answer is wrong and he doesn't want to restart the game the function closes the app
    """
        if (self.language == 'English'):
            if (player_answer == answer):
            # If right the games continues
                self.display_with_transition(f'Congrat\'s {self.player.player_name} you got it right!!\n{question['explanation']}')
                self.sleep(3)
                self.clear_console()

                return 'right'
            else:
            # If wrong the player is ask to restar the game or close the app
                self.display_with_transition(f'''Sorry {self.player.player_name} but you got it wrong\n
The right answer was "{question['explanation']}"\nGood luck next time!!''')
                self.sleep(3)
                self.clear_console()
                self.display_with_transition(f'{self.player.player_name} would you like to play again? (Yes/No)')
                yes_no = self.yes_no()
            if (yes_no == 'YES'):
                self.clear_console()
                
                return 'restart'
            else:
                self.display_with_transition("""
░▀█▀░█░█░█▀█░█▀█░█░█░█▀▀░░░█▀▀░█▀█░█▀▄░░░█▀█░█░░░█▀█░█░█░▀█▀░█▀█░█▀▀░█░█
░░█░░█▀█░█▀█░█░█░█▀▄░▀▀█░░░█▀▀░█░█░█▀▄░░░█▀▀░█░░░█▀█░░█░░░█░░█░█░█░█░▀░▀
░░▀░░▀░▀░▀░▀░▀░▀░▀░▀░▀▀▀░░░▀░░░▀▀▀░▀░▀░░░▀░░░▀▀▀░▀░▀░░▀░░▀▀▀░▀░▀░▀▀▀░▀░▀
""")
                self.sleep()
                sys.exit()
        elif (self.language == 'Spanish'):
            if (player_answer == answer):
            # If right the games continues
                self.display_with_transition(f'Felicidades {self.player.player_name} lo conseguiste!!\n{question['explanation']}')
                self.sleep(3)
                self.clear_console()
                
                return 'right'
            else:
                # If wrong the player is ask to restar the game or close the app
                self.display_with_transition(f'''Lo siento {self.player.player_name} pero te equivocaste\n
La respuesta correcta era "{question['explanation']}"\nBuena suerte para la proxima!!''')
                self.sleep(3)
                self.clear_console()
                self.display_with_transition(f'{self.player.player_name} ¿Te gustaria jugar de nuevo? (Si/No)')
                yes_no = self.yes_no()
                if (yes_no == 'SI'):
                    self.clear_console()

                    return 'restart'
                else:
                    self.display_with_transition("""
░▀█▀░█░█░█▀█░█▀█░█░█░█▀▀░░░█▀▀░█▀█░█▀▄░░░█▀█░█░░░█▀█░█░█░▀█▀░█▀█░█▀▀░█░█
░░█░░█▀█░█▀█░█░█░█▀▄░▀▀█░░░█▀▀░█░█░█▀▄░░░█▀▀░█░░░█▀█░░█░░░█░░█░█░█░█░▀░▀
░░▀░░▀░▀░▀░▀░▀░▀░▀░▀░▀▀▀░░░▀░░░▀▀▀░▀░▀░░░▀░░░▀▀▀░▀░▀░░▀░░▀▀▀░▀░▀░▀▀▀░▀░▀
""")
                    self.sleep()
                    sys.exit()
        else:
            print('Error')

    def prize_text(self, prize):
        """
    Displays the prize according to the language, asks the player if he wants to retire with his prize and handles the player input.

    Parameters:
    - prize (int): The prize the player has won.

    Returns:
    - None 

    The function displays the prize according to the language, asks the player if he wants to retire with his prize and handles the player input.
    If the player wants to retire the function displays the final message and closes the app.
    If the player doesn't want to retire the function clears the console and continues with the game.
    """
        if (self.language == 'English'):
            self.display_with_transition(f'''{self.player.player_name} you have reach {self.player.player_points} points
Would you like to retire with your prize? ${prize}?
(Yes/No)''')
            player_input = self.yes_no()
            if (player_input == 'YES'):
                if (prize == 5000):
                    self.display_with_transition("""
░█░█░█▀█░█░█░░░█░█░█▀█░█▀█░░░▄█▀░█▀▀░▄▀▄░▄▀▄░▄▀▄░█░█░█
░░█░░█░█░█░█░░░█▄█░█░█░█░█░░░▀██░▀▀▄░█/█░█/█░█/█░▀░▀░▀
░░▀░░▀▀▀░▀▀▀░░░▀░▀░▀▀▀░▀░▀░░░▀▀░░▀▀░░░▀░░░▀░░░▀░░▀░▀░▀
""")
                elif (prize == 50000):
                    self.display_with_transition("""
░█░█░█▀█░█░█░░░█░█░█▀█░█▀█░░░▄█▀░█▀▀░▄▀▄░▄▀▄░▄▀▄░▄▀▄░█░█░█
░░█░░█░█░█░█░░░█▄█░█░█░█░█░░░▀██░▀▀▄░█/█░█/█░█/█░█/█░▀░▀░▀
░░▀░░▀▀▀░▀▀▀░░░▀░▀░▀▀▀░▀░▀░░░▀▀░░▀▀░░░▀░░░▀░░░▀░░░▀░░▀░▀░▀
""")
                self.display_with_transition("""
░▀█▀░█░█░█▀█░█▀█░█░█░█▀▀░░░█▀▀░█▀█░█▀▄░░░█▀█░█░░░█▀█░█░█░▀█▀░█▀█░█▀▀░█░█
░░█░░█▀█░█▀█░█░█░█▀▄░▀▀█░░░█▀▀░█░█░█▀▄░░░█▀▀░█░░░█▀█░░█░░░█░░█░█░█░█░▀░▀
░░▀░░▀░▀░▀░▀░▀░▀░▀░▀░▀▀▀░░░▀░░░▀▀▀░▀░▀░░░▀░░░▀▀▀░▀░▀░░▀░░▀▀▀░▀░▀░▀▀▀░▀░▀
""")
                self.sleep()
                sys.exit()
            else:
                self.clear_console()
        elif (self.language == 'Spanish'):
            self.display_with_transition(f'''{self.player.player_name} alcanzaste los {self.player.player_points} puntos
¿Te gustaria retirarte con tu premio? ${prize}
(Si/No)''')
            player_input = self.yes_no()
            if (player_input == 'SI'):
                if (prize == 5000):
                    self.display_with_transition("""
░█▀▀░█▀█░█▀█░█▀█░█▀▀░▀█▀░█▀▀░░░▄█▀░█▀▀░▄▀▄░▄▀▄░▄▀▄░█░█░█
░█░█░█▀█░█░█░█▀█░▀▀█░░█░░█▀▀░░░▀██░▀▀▄░█/█░█/█░█/█░▀░▀░▀
░▀▀▀░▀░▀░▀░▀░▀░▀░▀▀▀░░▀░░▀▀▀░░░▀▀░░▀▀░░░▀░░░▀░░░▀░░▀░▀░▀
""")
                elif (prize == 50000):
                    self.display_with_transition("""
░█▀▀░█▀█░█▀█░█▀█░█▀▀░▀█▀░█▀▀░░░▄█▀░█▀▀░▄▀▄░▄▀▄░▄▀▄░▄▀▄░█░█░█
░█░█░█▀█░█░█░█▀█░▀▀█░░█░░█▀▀░░░▀██░▀▀▄░█/█░█/█░█/█░█/█░▀░▀░▀
░▀▀▀░▀░▀░▀░▀░▀░▀░▀▀▀░░▀░░▀▀▀░░░▀▀░░▀▀░░░▀░░░▀░░░▀░░░▀░░▀░▀░▀
""")
                self.display_with_transition("""
░█▀▀░█▀▄░█▀█░█▀▀░▀█▀░█▀█░█▀▀░░░█▀█░█▀█░█▀▄░░░▀▀█░█░█░█▀▀░█▀█░█▀▄░█░█
░█░█░█▀▄░█▀█░█░░░░█░░█▀█░▀▀█░░░█▀▀░█░█░█▀▄░░░░░█░█░█░█░█░█▀█░█▀▄░▀░▀
░▀▀▀░▀░▀░▀░▀░▀▀▀░▀▀▀░▀░▀░▀▀▀░░░▀░░░▀▀▀░▀░▀░░░▀▀░░▀▀▀░▀▀▀░▀░▀░▀░▀░▀░▀
""")
                self.sleep()
                sys.exit()
            else:
                self.clear_console()
        else:
            print('Error')

    def final_text(self):
        """
    Displays the final message according to the language and closes the app.

    Parameters:
    - None

    Returns:
    - None

    The function displays the final message according to the language and closes the app.
    """
        if (self.language == 'English'):
            self.display_with_transition("""
░█░█░█▀█░█░█░░░█░█░█▀█░█▀█░░░▄█▀░▀█░░░░░▄▀▄░▄▀▄░▄▀▄░░░░▄▀▄░▄▀▄░▄▀▄░█░█░█
░░█░░█░█░█░█░░░█▄█░█░█░█░█░░░▀██░░█░░░░░█/█░█/█░█/█░░░░█/█░█/█░█/█░▀░▀░▀
░░▀░░▀▀▀░▀▀▀░░░▀░▀░▀▀▀░▀░▀░░░▀▀░░▀▀▀░▀░░░▀░░░▀░░░▀░░▀░░░▀░░░▀░░░▀░░▀░▀░▀
""")
            self.display_with_transition("""
░▀█▀░█░█░█▀█░█▀█░█░█░█▀▀░░░█▀▀░█▀█░█▀▄░░░█▀█░█░░░█▀█░█░█░▀█▀░█▀█░█▀▀░█░█
░░█░░█▀█░█▀█░█░█░█▀▄░▀▀█░░░█▀▀░█░█░█▀▄░░░█▀▀░█░░░█▀█░░█░░░█░░█░█░█░█░▀░▀
░░▀░░▀░▀░▀░▀░▀░▀░▀░▀░▀▀▀░░░▀░░░▀▀▀░▀░▀░░░▀░░░▀▀▀░▀░▀░░▀░░▀▀▀░▀░▀░▀▀▀░▀░▀
""")
            self.sleep()
            sys.exit()
        elif (self.language == 'Spanish'):
            self.display_with_transition("""
░█▀▀░█▀█░█▀█░█▀█░█▀▀░▀█▀░█▀▀░░░▄█▀░▀█░░░░░▄▀▄░▄▀▄░▄▀▄░░░░▄▀▄░▄▀▄░▄▀▄░█░█░█
░█░█░█▀█░█░█░█▀█░▀▀█░░█░░█▀▀░░░▀██░░█░░░░░█/█░█/█░█/█░░░░█/█░█/█░█/█░▀░▀░▀
░▀▀▀░▀░▀░▀░▀░▀░▀░▀▀▀░░▀░░▀▀▀░░░▀▀░░▀▀▀░▀░░░▀░░░▀░░░▀░░▀░░░▀░░░▀░░░▀░░▀░▀░▀
""")
            self.display_with_transition("""
░█▀▀░█▀▄░█▀█░█▀▀░▀█▀░█▀█░█▀▀░░░█▀█░█▀█░█▀▄░░░▀▀█░█░█░█▀▀░█▀█░█▀▄░█░█
░█░█░█▀▄░█▀█░█░░░░█░░█▀█░▀▀█░░░█▀▀░█░█░█▀▄░░░░░█░█░█░█░█░█▀█░█▀▄░▀░▀
░▀▀▀░▀░▀░▀░▀░▀▀▀░▀▀▀░▀░▀░▀▀▀░░░▀░░░▀▀▀░▀░▀░░░▀▀░░▀▀▀░▀▀▀░▀░▀░▀░▀░▀░▀
""")
            self.sleep()
            sys.exit()
        else:
            print('Error')

    def display_with_transition(self, text, delay=0.009):
        """
    Prints a text with a transition effect.

    Parameters:
    - text (str): The text to print.
    - delay (float): The delay between each character set to 0.009 by default.

    Returns:
    - None

    The function prints a text with a transition effect, character by character.
    """
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()

    def clear_console(self):
        """
    Clears the console.

    Parameters:
    - None

    Returns:
    - None

    The function checks the system and clears the console.
    """
        system = platform.system()
        if system == 'Windows':
            os.system('cls')
        elif system == 'Linux' or system == 'Darwin':
            os.system('clear')

    def sleep(self, seconds=2):
        """
    Makes the program sleep for a number of seconds.

    Parameters:
    - seconds (int): The number of seconds to sleep set to 2 by default.

    Returns:
    - None

    The function makes the program sleep for a number of seconds.
    """
        time.sleep(seconds)

    def yes_no(self): 
        """
    Checks if the player input is yes or no.

    Parameters:
    - None

    Returns:
    - player_input (str): The player input.

    The function ensures that the player input is yes or no and returns it.
    """
        player_input = input().upper()
        if (self.language == 'English'):
            while(player_input != 'YES' and player_input != 'NO'):
                self.display_with_transition('Invalid option plese enter: Yes or No')
                player_input = input().upper()
            
            return player_input
        elif (self.language == 'Spanish'):
            while(player_input != 'SI' and player_input != 'NO'):
                self.display_with_transition('Opcion invalida, porfavor escribe: Si o No')
                player_input = input().upper()
            
            return player_input
        else:
            print('Error')