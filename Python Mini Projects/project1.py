import random
def roll():
    min_val = 1
    max_val = 6
    roll = random.randint(min_val,max_val)
    return roll
while True:
    players = input("Enter the number of players(2-4): ")
    if players.isdigit():
        players=int(players)
        if 2<=players<=4:
            break
        else:
            print("Players number must between 2-4")
    else:
        print("Invalid")
max_score = 50
players_score = [0 for _ in range(players)]
while max(players_score)<max_score:
    for player_idx in range(players):
        print("\n Player nunmber",player_idx+1,"turn has just started!")
        print("Your total score is: ",players_score[player_idx],"\n")
        current_score = 0
        while True:
            should_roll = input("Would you like to make roll(y)?")
            if should_roll.lower()!="y":
                break
            value = roll()
            if value==1:
                print("You rolled a 1! Turn done!")
                current_score=0
                break
            else:
                current_score+=value
                print("You rolled a:",value)
            print("Your score is:",current_score)
        players_score[player_idx]+=current_score
        print("Your total score is:",players_score[player_idx])
max_score=max(players_score)
winning_idx=players_score.index(max_score)
print("Player number",winning_idx+1,"is a winner with score of: ",max_score)

