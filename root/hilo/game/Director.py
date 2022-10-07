from operator import truediv
from Dealer import Dealer

class Director:


    # A person who directs the game.

    # The responsibility of the director is to control the game.
    
    
    
    def __init__(self):
        self.is_playing = True
        self.score = 300
        self.dealer = Dealer()
        self.card = self.dealer.card

    def start_game(self):
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
        
    def won_round(self):
        #winner gains 100 points.
        
        self.score += 100

    def lost_round(self):

        self.score -= 75

    
    def play_again(self):
        if self.is_playing:
            response = input("would you like to play again")

            if response == "Y" or response =="y":
                self.is_playing = True
            else: 
                self.is_playing = False
        

    def do_updates(self):
        #draws a card
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

           

            

        

