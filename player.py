class Player:

    # Create variables to use in this
    player_name = ''
    player_points = 0

    def __init__(self, player_name):
        """
    Initializes the player state.

    Parameters:
    - player_name (str): The player name.

    Returns:
    - None

    The function initializes the player state, including the player name and points.
    """ 
        self.player_name = player_name
        self.player_points = 0