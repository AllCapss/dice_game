import random



class DiceGame:
    
    def __init__(self, stategy):
        self.strategy = stategy
        self.rounds_count = None
        self.score: int = None
        self.damage: int = 0
        self.dies: int = 6
        self.number_of_rounds: int = 3
        self.start_hand: list = []
        self.end_hand: list = []

    def roll(self, dices):
        rolls  = []
        for i in range(dices):
            value = random.randint(1,6)
            rolls.append(value)
        #print(rolls)
        return rolls

    def game_round(self, dies, cutoff):
        current_roll = self.roll(dies)
        keep = [item for item in current_roll if item >= cutoff]
        dismiss = [item for item in current_roll if item < cutoff]
        return keep, dismiss

    def game(self):
        dies_left = self.dies
        hand = []

        for i in range(self.number_of_rounds):
            #print(f'Round number: {i+1}')
            keep, dismiss = self.game_round(dies_left, self.strategy)

            hand += keep
            #print(f'Kept: {keep}')
            
            dies_left = self.dies - len(hand)
        
        hand += dismiss
        #print(f'Need to keep: {dismiss}')

        self.final_hand = hand
        self.score = sum(hand)

                





# tewst
import polars as pl
keep_above = []
avg_score = []
share_over_30 = []
number_of_simuls = 10000

for i in range(6):
    game = DiceGame(i+1)
    scores = []

    for i in range(number_of_simuls):
        game.game()
        print(f'Scored {game.score}')
        scores.append(game.score)

    rolls_above_30 = [item for item in scores if item>=30]
    keep_above.append(i+1)
    avg_score.append((sum(scores)/len(scores)))
    share_over_30.append(len(rolls_above_30)/len(scores))




