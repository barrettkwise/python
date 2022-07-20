import rpstournament
import random

#Your class must be called GamePlayer, and it must have these functions
class GamePlayer:
    #Give your AI a name. You can put your name in it or not, depending on whether you want to be anonymous.
    #You can submit multiple AI's with different names for the tournament
    name = "Barrett"
    last3 = []
    allchoices = ["rock", "paper", "scissors"]
    losecount = 0
    prev_user = ""

    def get_win_choice(choice):
        if choice == "rock" : return "paper"
        if choice == "paper" : return "scissors"
        else : return "rock"

    def make_choice(self):
        ##check patterns
        if len(self.last3) == 3:
            choice = self.check_for_patterns()
            if choice != "no pattern":
                self.prev_user = choice
                return choice

        ##if no patterns, go back to basic tactics
        if self.losecount >= 3:
            if self.losecount > 3:
                self.losecount = 0

            else:
                return self.predictive_guess()

        return self.probability_guess()
        
    def view_opponent_choice(self, opponent_choice):
        ##count loses
        if self.prev_user != "" and opponent_choice != self.prev_user:
            if opponent_choice == "rock" and self.prev_user != "paper":
                self.losecount += 1
            elif opponent_choice == "paper" and self.prev_user != "scissors":
                self.losecount += 1
            elif opponent_choice == "scissors" and self.prev_user != "rock":
                self.losecount += 1
                
        ##track opponents moves
        self.allchoices.append(opponent_choice)
        self.last3.append(opponent_choice)

        ##update opponents moves as
        ##more moves come in
        if len(self.last3) > 3:
            del self.last3[0]
        
    def check_for_patterns(self):
        ##check all common patterns
        if ["scissors", "scissors", "scissors"] == self.last3:
            return "rock"
        elif ["rock", "rock", "rock"] == self.last3:
            return "paper"
        elif ["paper", "paper", "paper"] == self.last3:
            return "scissors"

        else:
            ##if not common, guess next move
            ##in pattern cycle and find win move
            if "rock" in self.last3 and "paper" in self.last3 and "scissors" in self.last3:
                return GamePlayer.get_win_choice(self.last3[0])
            
        return "no pattern"

    def predictive_guess(self):
        ##pick move to force win or lose
        new_choices = [i for i in self.allchoices if i != self.last3[0]]
        self.prev_user = random.choice(new_choices)

        return self.prev_user

    def probability_guess(self):
        ##pick random move from all of opp. choices
        self.prev_user = random.choice(self.allchoices)

        return self.prev_user
        
    def new_player(self):
        self.losecount = 0
        self.prev_user = ""
        self.allchoices = ["rock", "paper", "scissors"]
        self.last3.clear()
        return

##run against other bots
tournament_manager = rpstournament.TournamentManager()
example_game_player = GamePlayer()
tournament_manager.run_tournament(example_game_player)

