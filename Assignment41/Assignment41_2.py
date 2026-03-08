# [A,B,C,D]
#X [1,2,3,6]
#Y [2,3,1,5] 
#[Red ,Red,Blue,Blue]
import numpy as np
import math

def EuclidienDistances(P1,P2):
    Ans = math.sqrt((P1["X"]-P2["X"])**2 +(P1["Y"]-P2["Y"]) **2)
    return Ans

def MarvellousKneighbourClassifer():
    data = [
        {'point':'A','X':1,'Y':2,'label':'Red'},
        {'point':'B','X':2,'Y':3,'label':'Red'},
        {'point':'C','X':3,'Y':1,'label':'Blue'},
        {'point':'D','X':6,'Y':5,'label':'Blue'},
        {'point':'E','X':7,'Y':6,'label':'Blue'}
        ]
    for i in data:
        new_point = {'X':2,'Y':2}
    Result = EuclidienDistances(data[0],new_point)
    print(Result)

    for a in data:
        a['distance']=EuclidienDistances(a,new_point)
    for a in data:
        print(a)
    
    sorted_data = sorted(data,key=lambda item : item['distance'])
    for a in sorted_data:
        print(a)

    K_values =[1,3,5]
    for K in K_values:
        nearest = sorted_data[:K]
        print(K)

        for a in nearest:
            print(a)

    # Voting
        votes = {}
        for neighbour in nearest:
            label = neighbour['label']
            votes[label] = votes.get(label,0) +1
        
        for d in votes:
            print("Name :",d , "Number of votes :",votes[d])

        predicted_class = max(votes , key=votes.get)
        print("Predicted class of (2,2) is :", predicted_class)


def main():
    MarvellousKneighbourClassifer()

if __name__ == "__main__":
    main()