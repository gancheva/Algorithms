#!/usr/bin/env python
 
# Implementation of a dynamic algorithm to compute the value
# of an optimal solution of an instance of the knapsack problem.
 
import sys
 
def read():
    
    # Read item values and weights from file.
    #
    # File format:
    # [knapsack size] [number of items]
    # [item 1 value] [item 1 weight]
    # [item 2 value] [item 2 weight]
    # ...

    f = open(sys.argv[1])
    lines = f.readlines()
    f.close()

    # Get only the knapsack size from the first line in file.
    size = int(lines[0].split()[0])

    # Get only the number of items from the first line in file.
    numberItems = int(lines[0].split()[1])
 
    # Get all items from the file.
    items = []
    for i in range(1, len(lines)):
        value, weight = lines[i].split()
        items.append((int(value), int(weight)))
 
    return size, numberItems, items
 
def knapsack(size, numberItems, items):

    # Calculate optimal knapsack solution.
 
    subproblems =[[0 for x in range(size+1)] 
                  for x in range(numberItems)]
 
    for i in range(1, numberItems):
        for j in range(size+1):
            value = items[i][0]
            weight = items[i][1]
            case1 = subproblems[i-1][j]
 
            if weight > j:
                subproblems[i][j] = case1
            else:
                case2 = subproblems[i-1][j-weight] + value
                subproblems[i][j] = max(case1, case2)
 
    return subproblems[numItems-1][size]
 
def main():
    size, numberItems, items = read()
    optimal = knapsack(size, numberItems, items)
    print "Optimal knapsack solution value: ", optimal
 
if __name__ == "__main__":
    main()