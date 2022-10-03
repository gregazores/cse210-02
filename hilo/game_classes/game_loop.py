from game_classes.player import Player
from game_classes.card import Card

class Game_loop:
    """The main game play loop.

        responsibility: to control the order of game play.

        attributes:
            cards (list of integers[Card]):  a list of two card instances
            player (Player): instance of a player

    """
    def __init__(self):
        """Constructs an new game loop.
        
        args: self (Game_loop): an instance of Game_loop.
        """
        self.cards = []
        self.player = Player()

        for i in range(2):
            card = Card()
            self.cards.append(card)

    def start_game(self):
        play = "y" #establishes a variable to track the game loop iterations

        self.player.display_points() #displays player's starting points

        while play == "y":
            

            print (f"The card is: {self.cards[0].get_value()}") # displays first card value, possibly replace with self.cards[0].display1() Card class method

            self.player.input() #Player class method asking for player input

            print (f"Next card was: {self.cards[1].get_value()}") # displays first card value, possibly replace with self.cards[0].display2() Card class method

            self.player.point_update(self.cards) #Player class method to update points based on player guess
            
            self.player.display_points() #player method to display player's updated points
            
            ####These two functions can be combined into a single function defined as a Game_loop class method -- it updates the cards list to prepare for the next games round
            card = Card() #establishes a new card value for the next game loop
            self.cards.pop(0) #removes first card in Cards list
            self.cards.append(card) #adds a new card to the end of the list

            if self.player.points <= 0:
                print ("I'm sorry you're out of points")
                play = "n"
            else:
                play = input("Play again? [y/n]")

        print("Thanks for Playing!")