import pygame
import math
import time
import pygame.key
import random
import sys
from pygame.constants import MOUSEMOTION

from node import Node
from maze import Maze
from agent import Agent

sys.setrecursionlimit(2000)
# function definitions

# Variables
# Colors
BLACK   = (   0,   0,   0)
WHITE   = ( 255, 255, 255)
AQUA    = (   0, 255, 255)
BLUE    = (   0,   0, 255)
GREEN   = (   0, 255,   0)
RED     = ( 255,   0,   0)
YELLOW  = ( 255, 255,   0)

# Const Dimensions
WIDTH = 20
HEIGHT = 20
MARGIN = 5
GRIDSIZE = 20


# def getLowestCostNode(nodeArray: list) -> Node:
#     '''
#     Function gets the lowest node in a given array of nodes

#     Parameters:
#     :nodeArray: an array of nodes

#     Raises:
#     :valueError: when the array is empty

#     Returns:
#     :Node: the node with the lowest fCost
#     '''

#     if nodeArray == None or len(nodeArray) == 0:
#         raise ValueError("Node Array is empty")

#     minNode = nodeArray[0]
#     removedIndex = 0
#     for index in range(1,len(nodeArray)):
#         if nodeArray[index].fCost < minNode.fCost:
#             minNode = nodeArray[index]
#             removedIndex = index
#     nodeArray.pop(removedIndex)
#     return minNode

# # Astar Algo
# def updateChildNode(node: Node, parentNode: Node, openNodeArray: list):
#     '''
#     Changes Costs of child node
#     '''
#     if (node.value != 3) and (node.value != 4):
#         newPath = node.updateCosts(parentNode, targetNode)
#         if newPath:
#             openNodeArray.append(node)
#             node.value = 2

# def updateNeighbours(node: Node, openNodeArray: list) -> None:
#     '''
#     Function sets costs of neighbouring nodes and places them in array of open Nodes

#     param:
#     :node: node which neighbours are to be generated
#     :openNodeArray: array of open Nodes

#     raises:
#     :valueError: if no node is given
#     '''

#     if node == None:
#         raise ValueError("Input arguments are incorrect")

#     if node.y > 0 and node.isLinked(grid[node.y-1][node.x]):
#         updateChildNode(grid[node.y-1][node.x], node, openNodeArray)

#     if node.y < GRIDSIZE-1 and node.isLinked(grid[node.y+1][node.x]):
#         updateChildNode(grid[node.y+1][node.x], node, openNodeArray)

#     if node.x > 0 and node.isLinked(grid[node.y][node.x-1]):
#         updateChildNode(grid[node.y][node.x-1], node, openNodeArray)

#     if node.x < GRIDSIZE-1 and node.isLinked(grid[node.y][node.x+1]):
#         updateChildNode(grid[node.y][node.x+1], node, openNodeArray)

# def findPath(finalNode: Node) -> None:
#     list = []
#     if finalNode != None:
#         findPathAux(list, finalNode)
#         for node in list:
#             node.value = 1

# def findPathAux(list: list, node: Node) -> None:
#     list.append(node)
#     if node.parent != None:
#         findPathAux(list, node.parent)


if __name__ == "__main__":
    pygame.init()
    windowSize = [(WIDTH + MARGIN)*GRIDSIZE + MARGIN,(WIDTH + MARGIN)*GRIDSIZE + MARGIN] # Setting window size
    screen = pygame.display.set_mode(windowSize) # Creating window object
    pygame.display.set_caption("A Star with Maze") # Setting Name of window`
    done = False # used to determine whether done
    finalFound = False
    begin = False
    clock = pygame.time.Clock()

    maze = Maze(GRIDSIZE)
    grid = maze.grid
    startNode = grid[1][1]
    startNode.value = 1
    targetNode = grid[GRIDSIZE-2][GRIDSIZE-2]
    targetNode.value = 1

    agent = Agent(maze, startNode, targetNode)

    while not done:

        if finalFound == False and begin == True:
            currentNode = agent.getLowestCostNode()
            if currentNode == targetNode:
                agent.findPath(currentNode)
                finalFound = True
            elif finalFound == False:
                currentNode.value = 3
                agent.updateNeighbours(currentNode)

        # On Event activations
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicks close
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                column = pos[0] // (WIDTH+MARGIN)
                row = pos[1] // (WIDTH+MARGIN)
                try:
                    grid[row][column].value = 4
                    print(f"Click {pos} Grid Coordinates: {row} {column}")
                except:
                    print(f"Click {pos} Position out of range")
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    begin = True
                    print(begin)

        screen.fill(BLACK) # Sets window background to black

        # Drawing grid
        for row in range(GRIDSIZE):
            for column in range(GRIDSIZE):
                color = WHITE
                if grid[row][column].value == 1:
                    if grid[row][column] == startNode or grid[row][column] == targetNode:
                        color = BLUE
                    else:
                        color = GREEN
                elif grid[row][column].value == 3:
                    if grid[row][column] == startNode or grid[row][column] == targetNode:
                        color = BLUE
                    elif grid[row][column] != currentNode:
                        color = RED
                    else:
                        color = YELLOW
                elif grid[row][column].value == 2:
                    color = AQUA
                elif grid[row][column].value == 4:
                    color = BLACK

                pygame.draw.rect(
                    screen,
                    color,
                    [
                    (MARGIN + WIDTH)*column + MARGIN,
                    (MARGIN + WIDTH)*row + MARGIN,
                    WIDTH, HEIGHT
                    ]
                )

        # Drawing where nodes are linked (no walls)
        for row in range(GRIDSIZE):
            for column in range(GRIDSIZE):
                color = WHITE
                if column < GRIDSIZE-1 and grid[row][column].isLinked(grid[row][column+1]):
                    pygame.draw.rect(
                        screen, color,
                        [
                        (MARGIN+WIDTH)*column + WIDTH + MARGIN,
                        (MARGIN+HEIGHT)*row + MARGIN,
                        MARGIN, HEIGHT
                        ]
                    )
                if row < GRIDSIZE-1 and grid[row][column].isLinked(grid[row+1][column]):
                    pygame.draw.rect(
                        screen, color,
                        [
                        (MARGIN+WIDTH)*column + MARGIN,
                        (MARGIN+HEIGHT)*row + HEIGHT +MARGIN,
                        WIDTH, MARGIN
                        ]
                    )

        clock.tick(60) # Limits program to 60 FPS

        pygame.display.flip()

    pygame.quit()
