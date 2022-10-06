from operator import truediv
from Dealer import Dealer
#self.last_input

win = False
class Director:


    # A person who directs the game.

    # The responsibility of the director is to control the game.
    
    
    
    def __init__(self):
        self.is_playing = True
        self.score = 300
        self.total_score = 0

    def start_game(self):


        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.play_again()
            self.do_outputs()



    def get_inputs(self):
        #asks the user if they choose a higher number or a lower number.


        #Args:
            #self(director):An instance of Director

        num_select=input("High or low? [h/l]")
        self.is_playing = input(num_select == "h")

    def win_condition(self):
        #winner gains 100 points.
        
        self.score += 100

    def lost_round(self):

        self.score -= 75


   
    
    
    def play_again(self):
       response = input("would you like to play again")
       
       if response == "Y":
            self.is_playing = True
        
       else: 
            self.is_playing = False
        

    def do_updates(self):
        #draws a card
        #Args
            #self(Director) An instance of Director

        if not self.is_playing:
            return
        
        for i in range(len(self.card)):
            card = self.card
            card.draw(i)
            self.score += card.points
        self.total_score += self.score
    
    def do_outputs(self):
        #display results

        #Args:
            #self(Director): An instance of Director

            if not self.is_playing:
                return

            values = "" 
            for i in range(len(self.card)):
                card = self.card[i]
                values += f"{card.value}"
            print(f"next card was: {values}")
            print(f"Your score is:; {self.total_score}")
            self.is_playing == (self.score > 0)

           

            

        

