def canCompleteCircuit( gas, cost):
    """
    leeCode 134. Gas Station
    https://leetcode.com/problems/gas-station/
    difficulty: medium

    There are N gas stations along a circular route, where the amount of gas at station i is gas[i].
    You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1).
    You begin the journey with an empty tank at one of the gas stations.
    Return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1.
    Note: If there exists a solution, it is guaranteed to be unique.

    """
    if sum(gas)<sum(cost):
        return -1
    
    total = 0
    k=0
    for i in range(len(gas)):
        total += gas[i]-cost[i]
        if total < 0:
            total=0
            k=i+1
        # print(total)
    return k

print(canCompleteCircuit([1,2,3,4],[1,2,3,4]))
print(canCompleteCircuit([1,2,3,4],[4,3,2,1]))
print(canCompleteCircuit([2,3,4],[3,4,3]))

