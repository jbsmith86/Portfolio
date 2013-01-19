# Imagine you have standardized test scores for 1000 students in 4 different regions. You
# would expect that in the top 100 scores each region would at least have 25 students 
# statistically in the top 100. What are the odds by sheer chances one of the countries has
# 30 out of the top 100? This code runs the simulation for a specified number of trials and 
# returns the probability of one of the countries having 30 of the top 100 test scores.


import random


def test(numTrials):
    """
    Uses a full simulation to compute and return an estimate of
    the probability of at least 30 of the top 100 grades
    coming from a single geographical area purely by chance
    numTrials: the number of simulations to run in order to calculate the problem
    """
    wins = 0.0
    for i in range(numTrials):
        afr = 0
        eu = 0
        sa = 0
        asi = 0
        trial = []
        for _ in range(250):
            trial.append(scores(random.randrange(0,101),'Africa'))
        for _ in range(250):
            trial.append(scores(random.randrange(0,101),'Europe'))
        for _ in range(250):
            trial.append(scores(random.randrange(0,101),'SAmerica')) 
        for _ in range(250):
            trial.append(scores(random.randrange(0,101),'Asia'))
        trial.sort(key=lambda x: x.score, reverse=True)
        for j in trial[0:100]:
            if j.region == 'Africa':
                afr += 1
            if j.region == 'Europe':
                eu += 1
            if j.region == 'SAmerica':
                sa += 1
            if j.region == 'Asia':
                asi += 1
        if afr >= 30:
            wins += 1
        elif eu >= 30:
            wins += 1
        elif sa >= 30:
            wins += 1
        elif asi >= 30:
            wins += 1
        else:
            pass

    return wins/numTrials
    
    
class scores(object):
    def __init__(self, score, region):
        self.score = score
        self.region = region
