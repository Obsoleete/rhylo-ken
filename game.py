from Game_environment import GameEnvironment
import pygame


class Game:
    """
       Class to represent a single game.
       instance variables:
       int level = The difficulty level of the game. This is obtained from the
        food in the environment
       int score = The score the user has scored.
       environment = The game environment object in which this game is player
       """

    def __init__(self):

        self.score = 0
        self.environment = GameEnvironment()
        self.level = self.environment.food.level

    def set_level(self, level):
        """
        Sets the initial difficulty level of the game. Changes the food levels
        in the environment accordingly and changes the fps of the environment.
        :param level: The initial level of the game.
        :return: None

        >>> game_object = Game()
        >>> game_object.set_level(3)
        >>> print(game_object.level)
        3
        >>> game_object.set_level(4)
        >>> print(game_object.level)
        4
        """
        self.level = level
        self.environment.food.level = self.level
        self.environment.fps += 5

    def run_game(self):
        """
        Calls the events method on this game's environment and then calls
        end_game_display when the game ends
        :return: None
        """
        # To be implemented
        pass

    def end_game_display(self):
        """
        This method creates and displays a pygame window with the appropriate
        message displayed
        """
        # To be implemented
        pass


def get_score(game_object):
    """
    Returns the score scored in given game. The score is calculated using the
    level and amount eaten.
    :param game_object: Game object
    :return: int
    """
    # To be implemented
    pass


def get_final_score(game_object):
    """
    Implementation yet to decided.
    :param game_object:
    :return:
    """


if __name__ == '__main__':
    game = Game()
    game.run_game()
