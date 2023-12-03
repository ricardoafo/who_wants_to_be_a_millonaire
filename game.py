import questions
import player
import language
import time

class Game:

    # Create variables to use in the game from other classes
    question = questions
    player = player.Player
    language = language

    def __init__(self):
        """
    Initializes the game state.

    Parameters:
    - None

    Returns:
    - None

    The function initializes the game state, including the player name and points, and the language.
    """
        # Ask the player for the language and validate the input
        self.language = language.Language()

        # Run game with selected language
        self.question = self.language.greeting_text()

        # Ask question
        self.ask_question()

    def ask_question(self):
        """
    Calls the question module to get a random question, and then calls the answer_question function.

    Parameters:
    - None

    Returns:
    - None

    The function calls the question module to get a random question, and then calls the answer_question function to handle the user answer.
    """
        # Get the a random question and print it
        question = self.question.throw_random_question()
        self.display_with_transition(f'{question['question']}')

        # Get the question options and print them
        self.language.options_text(question)

        # Get the player answer and compare it with the right answer
        self.answer_question(question)

    def answer_question(self, question):
        """
    Process and evaluate the player's answer for the given question.

    Parameters:
    - question (dict): A dictionary representing the question, including options,the correct answer and the explination.

    Returns:
    - None

    The function prompts the player for an answer, validates it, compares it with the correct answer,
    and updates the game state accordingly.
    """
        # Extract options and answer from the question dictionary to use them in the comparison later
        options = question['options']
        answer = question['answer']

        # Get the player input and check if is valid with the while statement
        player_answer = self.language.answer_question_input_text()
        
        # Match the player input with the available options
        match player_answer:
            case 'A':
                 player_answer = options[0]
            case 'B':
                player_answer = options[1]
            case 'C':
                player_answer = options[2]
            case 'D':
                player_answer = options[3]

        # Compare the player input with the right answer
        outcome = self.language.answer_question_result_text(question, player_answer, answer)

        # If right the games continues, the game ends if the player answer is wrong and doesn't want to restart
        if (outcome == 'right'):
            self.player.player_points += 1
            self.prizes()
            self.ask_question()
        elif (outcome == 'restart'):
            self.player.player_points = 0
            self.__init__()

    def prizes(self):
        """
    Checks if the player has won a prize.

    Parameters:
    - None

    Returns:
    - None

    The function checks if the player has won a prize and, if so, call the prize_text function to display the prize.
    Also, if the player has won the game, the function calls the final_text function to display the final message.
    """
        # Check if the player has won a prize and display it
        prize  = 0
        if (self.player.player_points == 5):
            prize = 5000
            self.language.prize_text(prize)
        elif (self.player.player_points == 10):
            prize = 50000
            self.language.prize_text(prize)
        # Check if the player has won the game and display the final message
        elif (self.player.player_points == 15):
            prize = 1000000
            self.language.final_text()
        
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