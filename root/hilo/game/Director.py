from operator import truediv
from Dealer import Dealer

class Director:


    # A person who directs the game.

    # The responsibility of the director is to control the game.
    
    
    
    def __init__(self):
        #sets Director's values to proper defaults.
        self.is_playing = True
        self.score = 300
        self.dealer = Dealer()
        self.card = self.dealer.card

    def start_game(self):
        #starts the main game loop and continues until the user is finished
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
            self.play_again()

    def get_inputs(self):
        #asks the user if they choose a higher number or a lower number.

        #Args:
            #self(director):An instance of Director
        self.choice = input(f"The card is {self.card}.\nHigh or low? [h/l]")
        self.choice = self.choice.lower()
        while self.choice!= "h" and self.choice != "H"and self.choice !="l" and self.choice != "L":
            self.choice = input(f"'{self.choice}' is not an option please type 'H', 'h', 'L' or 'l': ")
        
    def won_round(self):
        #winner gains 100 points.
        
        self.score += 100

    def lost_round(self):
        #loser loses 75 points.

        self.score -= 75

    
    def play_again(self):
        #asks the user if they want to play again
        if self.is_playing:
            response = input("would you like to play again: ")

            if response == "Y" or response =="y":
                self.is_playing = True
            else: 
                self.is_playing = False
                print("Thanks for playing! see you soon pal!")
        

    def do_updates(self):
        #draws a card and determines if player won or lost round
        #Args
            #self(Director) An instance of Director

        self.dealer.deal()

        if self.choice == 'h' and self.dealer.card > self.card:
            self.won_round()
        elif self.choice =='l' and self.dealer.card < self.card:
            self.won_round()
        else:
            self.lost_round()

        self.card = self.dealer.card
        self.is_playing == (self.score > 0)
    
    def do_outputs(self):
        #display results

        #Args:
        #self(Director): An instance of Director

        print(f"next card was: {self.card}")
        print(f"Your score is: {self.score}")

           

            

        

