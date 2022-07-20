import random
import operator





RPS_WIN_LOGIC = {'rock':'scissors', 'paper':'rock', 'scissors':'paper'}
RPS_LOSE_LOGIC = {'scissors':'rock', 'paper':'scissors', 'rock':'paper'}
ROUNDS_PER_MATCH = 1000




########

class AIGamePlayer:
    name = "Pure Random Choice"

    def make_choice(self):
        return random.choice(['rock', 'paper', 'scissors'])

    def view_opponent_choice(self, opponent_choice):
        return

    def new_player(self):
        return

class GamePlayer_Scissors(AIGamePlayer):
    name = "Always Pick Scissors"

    def make_choice(self):
        return 'scissors'

class GamePlayer_PickToBeatAllChoicesRandom(AIGamePlayer):
    name = "Learn and then Random"

    def __init__(self):
        self.choice_list = ['rock', 'paper', 'scissors']

    def make_choice(self):
        return random.choice(self.choice_list)

    def view_opponent_choice(self, opponent_choice):
        self.choice_list.append(RPS_LOSE_LOGIC[opponent_choice])

    def new_player(self):
        self.choice_list = ['rock', 'paper', 'scissors']

class GamePlayer_PickToBeatMostChosen(AIGamePlayer):
    name = "Learn and pick most likely to beat opponent's choices"

    def __init__(self):
        self.choice_list = ['rock', 'paper', 'scissors']

    def make_choice(self):
        rocks = self.choice_list.count('rock')
        papers = self.choice_list.count('paper')
        scissors = self.choice_list.count('scissors')
        if (rocks > papers and rocks > scissors):
            return 'rock'
        elif (scissors > rocks and scissors > papers):
            return 'scissors'
        else:
            return 'paper'

    def view_opponent_choice(self, opponent_choice):
        self.choice_list.append(RPS_LOSE_LOGIC[opponent_choice])

    def new_player(self):
        self.choice_list = ['rock', 'paper', 'scissors']



class GamePlayer_LoopThreeChoices(AIGamePlayer):
    name = "Loop Three Choices"

    def __init__(self):
        self.initial_list = ['rock', 'paper', 'scissors']
        self.index = 0

    def make_choice(self):
        choice = self.initial_list[self.index]
        self.index += 1
        if self.index > 2:
            self.index = 0
        return choice

class GamePlayer_TripleLoopThreeChoices(AIGamePlayer):
    name = "Triple Loop Three Choices"

    def __init__(self):
        self.initial_list = ['rock', 'rock', 'rock', 'paper', 'paper', 'paper', 'scissors','scissors', 'scissors']
        self.index = 0

    def make_choice(self):
        choice = self.initial_list[self.index]
        self.index += 1
        if self.index > 8:
            self.index = 0
        return choice
    

class GamePlayer_BeatLast(AIGamePlayer):
    name = "Pick to beat last"

    def __init__(self):
        self.last_opponent_pick = 'scissors'

    def make_choice(self):
        return RPS_LOSE_LOGIC[self.last_opponent_pick]

    def view_opponent_choice(self, opponent_choice):
        self.last_opponent_pick = opponent_choice

class GamePlayer_SwitchEvery(AIGamePlayer):
    name = "Switch Every Round"


    def __init__(self):
        self.last_self_pick = random.choice(['rock', 'paper', 'scissors'])

    def make_choice(self):
        new_list = ['rock', 'paper', 'scissors']
        new_list.remove(self.last_self_pick)
        new_pick = random.choice(new_list)
        self.last_self_pick = new_pick
        return new_pick

    def view_opponent_choice(self, opponent_choice):
        return

class GamePlayer_StayIfWin(AIGamePlayer):
    name = "Repeat Choice if Win"

    def __init__(self):
        self.last_self_pick = 'paper'
        self.won_last_round = True

    def make_choice(self):
        if self.won_last_round:
            return self.last_self_pick
        else:
            new_list = ['rock', 'paper', 'scissors']
            new_list.remove(self.last_self_pick)
            new_pick = random.choice(new_list)
            self.last_self_pick = new_pick
            return new_pick

    def view_opponent_choice(self, opponent_choice):
        if RPS_WIN_LOGIC[self.last_self_pick] == opponent_choice:
            self.won_last_round = True
        else:
            self.won_last_round = False

class GamePlayer_SabotageLearningAlgorithms(AIGamePlayer):
    name = "Sabotage Learning AIs"
    RPS_WIN_LOGIC = {'rock':'scissors', 'paper':'rock', 'scissors':'paper'}
    RPS_LOSE_LOGIC = {'scissors':'rock', 'rock':'paper', 'paper':'scissors'}

    def __init__(self):
        self.last_choice = random.choice(['rock', 'paper', 'scissors'])
        self.all_opponent_choices = []
        self.all_my_choices = []

    def make_choice(self):
        current_pick = self.pick_sabotage_choice()
        self.last_choice = current_pick
        self.all_my_choices.append(current_pick)
        return current_pick

    def pick_sabotage_choice(self):
        #This AI will look at the choice I made last round, and all our compared choices
        #It will try to pick a choice based on what it most expects the opponent to pick this round
        #From that data

        # Example: my choices = ['rock', 'rock', 'paper']
        # opponent choices = ['scissors', 'paper', 'scissors']
        # dictionary: {"rock:paper": 1, "rock:scissors": 1}

        #If I haven't seen any of the opponent's choices yet, just pick scissors
        if len(self.all_opponent_choices) == 0:
            return random.choice(['rock', 'paper', 'scissors'])
        reactions_dictionary = {}

        #Loop over all the opponents choices...
        for reaction_index in range(1, len(self.all_opponent_choices[1:])):
            #...create strings that are a combination of the choice I made and the next choice the opponent made...
            reaction_string = self.all_my_choices[reaction_index - 1] + ":" + self.all_opponent_choices[reaction_index]
            #Add these combinations to a dictionary to count the most frequent occurances...
            if reaction_string in reactions_dictionary:
                reactions_dictionary[reaction_string] = reactions_dictionary[reaction_string] + 1
            else:
                reactions_dictionary[reaction_string] = 1
        #Go through all the different reaction types
        for key in reactions_dictionary.keys():
            #If I've seen an opponent reaction to my choice
            if self.last_choice in key:
                #Find the reaction they made to my choice the most often
                likely_reaction = max(reactions_dictionary.items(), key=operator.itemgetter(1))[0]
                #Split the combination in two
                likely_reaction_from_opponent = likely_reaction.split(':')[1]
                #Return what's going to beat THEIR choice
                return self.RPS_LOSE_LOGIC[likely_reaction_from_opponent]
            else:
                return random.choice(['rock', 'paper', 'scissors'])
        return random.choice(['rock', 'paper', 'scissors'])

    def view_opponent_choice(self, opponent_choice):
        #print("Win Rate: ", self.list_of_results)
        self.all_opponent_choices.append(opponent_choice)

class GamePlayer_Barrett(AIGamePlayer):
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
                return GamePlayer_Barrett.get_win_choice(self.last3[0])
            
        return "no pattern"

    def predictive_guess(self):
        ##pick move to force win or lose
        choices = ["rock", "paper", "scissors"]
        new_choices = [i for i in choices if i != self.last3[1]]
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

#Your class must be called GamePlayer, and it must have these functions
class GamePlayer_Pierce(AIGamePlayer):
    #Give your AI a name. You can put your name in it or not, depending on whether you want to be anonymous.
    #You can submit multiple AI's with different names for the tournament
    name = "KingBob"

    def __init__(self):
        self.choice_list = ['rock', 'paper' , 'scissors']
        self.rockCount=0
        self.paperCount=0
        self.scissorsCount=0
        self.rock_percentage=0
        self.paper_percentage=0
        self.scissors_percentage=0
        self.choices=[]
        self.loop = ["rock", "paper", "scissors", "rock", "paper", "scissors",
                "rock", "paper", "scissors", "rock", "paper", "scissors"]
        self.triple_loop = ["rock", "rock", 'rock', 'paper', 'paper', 'paper','scissors','scissors','scissors']
        self.past_opponent_choice="rock"
        self.opponent_list=[]
        self.loopai=False
        self.output=""
        self.loopIndex=0
        self.loopTripIndex=0
        self.scissorsFor=False
        self.loopList = []
        self.loopListTrip=[]
    
    def make_choice(self):
        return "banana"

    def view_opponent_choice(self, opponent_choice):
        if opponent_choice == "rock":
            self.rockCount+=1
        if opponent_choice == "paper":
            self.paperCount+=1
        if opponent_choice == "scissors":
            self.scissorsCount+=1
        self.past_opponent_choice= opponent_choice
        self.opponent_list.append(opponent_choice)

        if self.rockCount>0:    
            self.rock_percentage = (self.rockCount/(self.rockCount+self.scissorsCount+self.paperCount))*100
        if self.paperCount>0:
            self.paper_percentage = (self.paperCount/(self.rockCount+self.scissorsCount+self.paperCount))*100
        if self.scissorsCount>0:
            self.scissors_percentage = (self.scissorsCount/(self.rockCount+self.scissorsCount+self.paperCount))*100
        
            
        if self.rockCount + self.scissorsCount +self.paperCount>10 and self.scissors_percentage == 100:
            self.scissorsFor=True
        if self.rock_percentage == self.paper_percentage and ( self.paper_percentage == self.scissors_percentage and len(self.opponent_list) == 12):
            self.loopai=True
       # print(self.loopai)

    def new_player(self):
       self.scissorsCount =0
       self.paperCount = 0
       self.rockCount =0
       self.rock_percentage=0
       self.paper_percentage=0
       self.scissors_percentage=0
       self.loopIndex=0
       self.loopTripIndex=0
       self.loopai=False
       self.scissorsFor=False

RPS_WIN_LOGIC = {'rock':'scissors', 'paper':'rock', 'scissors':'paper'}
RPS_LOSE_LOGIC = {'scissors':'rock', 'rock':'paper', 'paper':'scissors'}

#Your class must be called GamePlayer, and it must have these functions
class BFJJ(AIGamePlayer):
    #Give your AI a name. You can put your name in it or not, depending on whether you want to be anonymous.
    #You can submit multiple AI's with different names for the tournament
    name = "Barry from jetpack joyride(Pierson)"

    

    def __init__(self):
        self.choice_list = ['rock', 'paper' , 'scissors']
        self.rockCount=0
        self.paperCount=0
        self.scissorsCount=0
        self.rock_percentage=0
        self.paper_percentage=0
        self.scissors_percentage=0
        self.choices=[]
        self.loop = ["rock", "paper", "scissors", "rock", "paper", "scissors",
                "rock", "paper", "scissors", "rock", "paper", "scissors"]
        self.triple_loop = ["rock", "rock", 'rock', 'paper', 'paper', 'paper','scissors','scissors','scissors']
        self.past_opponent_choice="rock"
        self.opponent_list=[]
        self.loopai=False
        self.output=""
        self.loopIndex=0
        self.loopTripIndex=0
        self.scissorsFor=False
        self.loopList = []
        self.loopListTrip=[]
        self.initial_list = ['scissors', 'paper', 'rock']
        self.index = 0
    
    def make_choice(self):
       
        if self.rockCount+self.scissorsCount+self.paperCount>2:
            if self.opponent_list[1:4]==['rock','paper','scissors']:
                
                self.index = 0
                self.choice = self.initial_list[self.index]
       # print(self.choice)
                self.index += 1
                self.output= self.choice

        
        if self.scissorsFor:
            self.output = "rock"
        elif self.loopai:
            self.loopList=["paper","scissors","rock"]
            self.output=self.loopList[self.loopIndex]
            self.loopIndex+=1
            if self.loopIndex>2:
                self.loopIndex=0

        else:
            self.output= random.choice(self.choice_list)
        if (self.rockCount+self.scissorsCount+self.paperCount)==0:
            self.output="scissors"
            
            
            
        

        return self.output
    
       
       
        

    def view_opponent_choice(self, opponent_choice):
        if opponent_choice == "rock":
            self.rockCount+=1
        if opponent_choice == "paper":
           self.paperCount+=1
        if opponent_choice == "scissors":
           self.scissorsCount+=1
        self.past_opponent_choice= opponent_choice
        self.opponent_list.append(opponent_choice)

        if self.rockCount>0:    
            self.rock_percentage = (self.rockCount/(self.rockCount+self.scissorsCount+self.paperCount))*100
        if self.paperCount>0:
            self.paper_percentage = (self.paperCount/(self.rockCount+self.scissorsCount+self.paperCount))*100
        if self.scissorsCount>0:
            self.scissors_percentage = (self.scissorsCount/(self.rockCount+self.scissorsCount+self.paperCount))*100
        
            
        if self.rockCount + self.scissorsCount +self.paperCount>10 and self.scissors_percentage == 100:
            self.scissorsFor=True
        if self.rock_percentage == self.paper_percentage and ( self.paper_percentage == self.scissors_percentage and len(self.opponent_list) == 12):
            self.loopai=True
        return

    def new_player(self):
       self.scissorsCount =0
       self.paperCount = 0
       self.rockCount =0
       self.rock_percentage=0
       self.paper_percentage=0
       self.scissors_percentage=0
       self.loopIndex=0
       self.loopTripIndex=0
       self.loopai=False
       self.scissorsFor=False
       self.index =0
       self.opponent_list=[]

class TournamentManager:

    def __init__(self, players_to_play_against):
        self.players_to_play_against = players_to_play_against
        self.tournament_results = {}

    def __init__(self):
        self.players_to_play_against = opponents_list
        self.tournament_results = {}

    def run_tournament(self, main_player):
        self.tournament_results = {}
        print("AI Name:" + main_player.name)
        for player in self.players_to_play_against:
            rounds_to_play = ROUNDS_PER_MATCH
            match_result = self.play_match(main_player, player, rounds_to_play)
            if (match_result[0] > 0 or match_result[1] > 0):
                win_percentage = match_result[0]/(match_result[0] + match_result[1])
            else:
                win_percentage = 0
            self.tournament_results[player.name] = win_percentage
            main_player.new_player()
        return self.print_all_results(main_player)

    def play_match(self,main_player, player,rounds):
        match_wins = 0
        match_losses = 0
        total_rounds_left = rounds
        failsafe_rounds = 100000
        while (total_rounds_left > 0 and failsafe_rounds > 0):
            main_player_choice = main_player.make_choice()
            opponent_choice = player.make_choice()
            round_result = self.determine_round_result(main_player_choice, opponent_choice)
            if round_result == "Win":
                match_wins += 1
                total_rounds_left -= 1
            elif round_result == "Lose":
                match_losses += 1
                total_rounds_left -= 1
            elif round_result == "FAIL":
                return (0, ROUNDS_PER_MATCH)
            main_player.view_opponent_choice(opponent_choice)
            player.view_opponent_choice(main_player_choice)
            failsafe_rounds -= 1
        return (match_wins, match_losses)
            

    def determine_round_result(self, player_choice, opponent_choice):
        if(player_choice not in RPS_WIN_LOGIC.keys()):
            return "FAIL"
        if player_choice == opponent_choice:
            return "Tie"
        elif RPS_WIN_LOGIC[player_choice] == opponent_choice:
            return "Win"
        else:
            return "Lose"


    def print_all_results(self, main_player):
        for opponent in self.tournament_results.keys():
            print("Opponent: " + opponent + "|Win Percentage: " + str(self.tournament_results[opponent]))

        print("Total score: " + str(sum(self.tournament_results.values()) / len(self.tournament_results.values())))
        return {}


test_player = AIGamePlayer()
test_player_2 = GamePlayer_Scissors()
test_player_3 = GamePlayer_LoopThreeChoices()
test_player_4 = GamePlayer_BeatLast()
test_player_5 = GamePlayer_SwitchEvery()
test_player_6 = GamePlayer_TripleLoopThreeChoices()
test_player_7 = GamePlayer_PickToBeatAllChoicesRandom()
test_player_8 = GamePlayer_PickToBeatMostChosen()
test_player_9 = GamePlayer_StayIfWin()
test_player_10 = GamePlayer_SabotageLearningAlgorithms()
test_player_11 = GamePlayer_Barrett()
test_player_12 = GamePlayer_Pierce()
test_player_13 = BFJJ()


opponents_list = [test_player, test_player_2, test_player_3,
                  test_player_4, test_player_5, test_player_6,
                  test_player_7, test_player_8, test_player_9,
                  test_player_10, test_player_11,
                  test_player_12, test_player_13]

#These are students' custom AIs. After they are all added to the same folder as this file, this code will
#run depending on whether those ais are there or not

try:
    import rpsai_tigershark
    tiger_shark = rpsai_tigershark.GamePlayer()
    opponents_list.append(tiger_shark)
except ImportError:
    pass


try:
    import rpsai_switcharoo
    switcharoo = rpsai_switcharoo.GamePlayer()
    opponents_list.append(switcharoo)
except ImportError:
    pass
    
try:
    import rpsai_shallowblue
    shallowblue = rpsai_shallowblue.GamePlayer()
    opponents_list.append(shallowblue)
except ImportError:
    pass


#random.shuffle(opponents_list)
