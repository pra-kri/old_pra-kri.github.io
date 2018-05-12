# Writing a K-Nearest Neighbours classifier function from scratch (using the reference mentioned below)
# Used pythonprogramming.net's tutorials + guides for this.
# References: 
# https://www.youtube.com/watch?v=GWHG3cS2PKc&index=16&list=PLQVvvaa0QuDfKTOs3Keq_kaG2P55YRn5v
# https://pythonprogramming.net/machine-learning-tutorial-python-introduction/



import numpy as np
import math
import matplotlib.pyplot as plt
from collections import Counter



dataset = {'k':[[1,2],[2,3],[3,1], [3,3]], 
           'r':[[6,5],[7,7],[8,6], [7,3]], 
           'g':[[2,5],[3,8],[3,6],[1,4]]}
# dataset contains 2 classes, and their features

new_features = [4,4]
# this is the new one we want to classify


for i in dataset:
    for ii in dataset[i]:
        plt.scatter(ii[0], ii[1], s=100, color = i)
        
plt.scatter(new_features[0], new_features[1], s=200)
plt.show()


def k_nearest_neighbours(data, predict, k = 3):
    if len(data) >= k:
        raise Exception('K is set to a value less than total voting groups!!!!')
        # if length of dictionary is bigger than k
        # run: knnalgos
        
    distances = []
    for group in data:
        for features in data[group]:
            # euc_dist = math.sqrt((features[0] - predict[0])**2 + (features[1] - predict[1])**2)
            euc_dist1 = np.linalg.norm(np.array(features) - np.array(predict))
            distances.append([euc_dist1, group])
    votes = [i[1] for i in sorted(distances) [:k]]
    vote_result = Counter(votes).most_common(1)[0][0]
        
    print(votes)
        
    return vote_result
    
# TODO: if there is a tie for the most popular vote...
# separate the euclidean distance function -> write it out yourself instead of using np.linalg.norm()




result = k_nearest_neighbours(dataset, new_features, k=5)
print(result)

