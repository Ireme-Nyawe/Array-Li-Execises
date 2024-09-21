# Program to represent scores of games in a tournament and find the winner

scores = [
    ["Team A", [15, 10, 29]],
    ["Team B", [7, 15, 20]],
    ["Team C", [6, 10, 32]]
]

winner = None
highest_average = 0

for team, score_list in scores:
    average_score = sum(score_list) / len(score_list)
    if average_score > highest_average:
        highest_average = average_score
        winner = team
print(scores)
print(f"The winner is {winner} with an average score of {highest_average:.2f}.")
