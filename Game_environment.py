import pygame
from Snake import Snake
from Food import Food


class GameEnvironment:
    """
        Class that models the environment in which the game is played.
        instance variables: screen : the pygame display
                            surface : the pygame surface
                            snake : A list of Snake objects
                            fps : The speed of the game
                            dir_change_location : A dictionary of coordinates
                             pointing to directions to be followed at those
                             coordinates
                            food : A Food object
                            status : States whether the game is running or over
                            It is 1 if game is running, 0 if game is over.
        """
    def __init__(self):
        pygame.init()
        self.status = 1
        self.screen = pygame.display
        self.surface = self.screen.set_mode((800, 600))
        self.snake = [Snake(200, 200, 'r')]
        self.fps = 60
        self.dir_change_location = {}
        self.food = Food()
        self.food.generate_food()

    def events(self):
        """
                Contains the event loop for the pygame window.Rectangle
                images for the snake and the Circle images for food are created
                in this event loop. Calls to other GameEnvironment methods are
                made from here.
                :return: None
        """
        done = False
        clock = pygame.time.Clock()
        while not done:  # start of the event loop
            for event in pygame.event.get():  # piping out the events
                if event.type == pygame.QUIT:
                    self.status = 0
                    done = True
            self.food.set_level()  # getting the food level set for the game
            self.fps = (self.food.level * 10) + 50
            # setting the speed of the game according the food level
            self.check_wall()  # checking if the snake has banged into the wall
            self.check_suicide()  # checking if the snake has turned into itself
            if self.status == 0:  # checking if the snake is supposed to dead.
                done = True
            self.check_food()  # checking if the snake has eaten food.
            pressed = pygame.key.get_pressed()
            self.update_position(pressed, self.snake[0].x_coord,
                                 self.snake[0].y_coord)
            # updating the position of the snake according to input direction
            self.surface.fill((0, 0, 0))
            for i in range(len(self.food.x)):  # loop to display all food.
                pygame.draw.circle(self.surface, (255, 255, 255),
                                   (self.food.x[i], self.food.y[i]), 10)
            for i in range(len(self.snake)):  # loop to display entire snake
                pygame.draw.rect(self.surface, (0, 128, 255),
                                 pygame.Rect(self.snake[i].get_position()[0],
                                             self.snake[i].get_position()[1],
                                             20, 20))

            self.screen.flip()
            clock.tick(self.fps)

    def update_position(self, pressed, x_coord, y_coord):
        """
        Method to make sure that all snake objects change direction at given
        point
        :param pressed: A pygame key object
        :param x_coord: The x coordinate where the change in direction happens
        :param y_coord: The y coordinate where the change in direction happens
        :return: None
        """


    def check_wall(self):
        """
        Method to check if the snake's head has hit the wall. Ends the game if
        this happens.
        :return: None
        """


    def check_food(self):
        """
        Checks if the snake has passed a food object. The length of the snake
        increases if this happens. Makes appropriate changes to the food object
        too.
        :return:
        """

    def check_suicide(self):
        """
        Checks if the snake turns into itself. Ends the game if this happens
        :return: None
        """

