import game

game = game.Game

print('Welcome to who wanna be a millonarie!!')
name_of_player = input('What\'s your name?\n')
game = game(name_of_player)

print(f'''Well {name_of_player} let\'s start with the game!
Your first question is:''')

game.ask_question()