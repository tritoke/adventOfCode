#!/usr/bin/python3.7
import sys
from time import time
write = sys.stdout.write
flush = sys.stdout.flush
lastMarble = 72019
numPlayers = 458

class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

def game(lastMarble, numPlayers):
    t0 = time()
    head = Node(0)
    n1, n2 = Node(1), Node(2)
    head.right = n1.left = n2
    head.left = n2.right = n1
    n1.right = n2.left = head
    currentNode = n2

    marbles = list(range(3, lastMarble + 1))
    players = [0] * numPlayers


    def printNodes(headNode, currentNode):
        current = headNode.right
        write("HEAD :: ")
        write(str(headNode.val) + ", ")
        while headNode is not current:
            if current is currentNode:
                write("(")
            write(str(current.val))
            if currentNode is current:
                write(")")
            if headNode is not current.right:
                write(", ")
            current = current.right
        write(" :: TAIL\n")

    percentNum = lastMarble // 100

    write("[")
    flush()
    #print("[", end="")
    for marble in marbles:
        if marble % percentNum == 0:
            #print("#",end="")
            write("#")
            flush()
        if marble % 23 == 0:
            currentPlayer = (marble - 1) % numPlayers
            currentNode = currentNode.left.left.left.left.left.left
            players[currentPlayer] += (marble + currentNode.left.val)
            currentNode.left = currentNode.left.left
            currentNode.left.right = currentNode

        else:
            newNode = Node(marble)
            newNode.right = currentNode.right.right
            newNode.left = currentNode.right
            currentNode.right.right.left = newNode
            currentNode.right.right = newNode
            currentNode = newNode
    #print("]")
    write("]\n")
    flush()
    return max(players), (time()-t0)


print("part 1: [{}] :: [{:.5f}] seconds".format(*game(lastMarble, numPlayers)))
print("part 2: [{}] :: [{:.5f}] seconds".format(*game(lastMarble*100, numPlayers)))
