import votes
import operator 

"""
    Sorts a list of string paths based on a learning algorithm 
"""
def sort(repos):
    keypairs = []
    for path in repos:
        keypairs.append([path, votes.get_votes(path)])
    keypairs.sort(key = operator.itemgetter(1), reverse=True)
    return [pair[0] for pair in keypairs]

"""
    This is the feedback loop function used after a sort
"""
def choose(path):
    votes.increment_votes(path)
