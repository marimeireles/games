import random

# Payoff matrix
payoffs = {
    ('C', 'C'): (3, 3),
    ('C', 'D'): (0, 5),
    ('D', 'C'): (5, 0),
    ('D', 'D'): (1, 1),
}

def tit_for_tat(history):
    if len(history) == 0:
        return 'C'
    return history[-1][1]  # Return the opponent's last move

def always_defect(history):
    return 'D'

def play_round(agent1, agent2, history):
    action1 = agent1(history)
    action2 = agent2(history)
    payoff1, payoff2 = payoffs[(action1, action2)]
    history.append((action1, action2))
    return payoff1, payoff2

def simulate(agent1, agent2, num_rounds):
    history = []
    scores = [0, 0]

    for _ in range(num_rounds):
        payoff1, payoff2 = play_round(agent1, agent2, history)
        scores[0] += payoff1
        scores[1] += payoff2

    return scores, history

# Simulate the iterated prisoner's dilemma between Tit-for-Tat and Always Defect agents
num_rounds = 100
scores, history = simulate(tit_for_tat, always_defect, num_rounds)
print(f"Scores: {scores}")
print(f"History: {history}")

