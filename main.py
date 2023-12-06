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

if __name__ == "__main__":
    pygame.init()
    windowSize = [(WIDTH + MARGIN)*GRIDSIZE + MARGIN,(WIDTH + MARGIN)*GRIDSIZE + MARGIN] # Setting window size
    screen = pygame.display.set_mode(windowSize) # Creating window object
    pygame.display.set_caption("A Star with Maze") # Setting Name of window`
    done = False # used to determine whether done
    finalFound = False
    begin = False
    clock = pygame.time.Clock()

    maze = Maze(GRIDSIZE, (1, 1), (GRIDSIZE-2, GRIDSIZE-2))
    grid = maze.grid

    agent = Agent(maze)

    while not done:

        if finalFound == False and begin == True:
            currentNode = agent.getLowestCostNode()
            if currentNode == maze.targetNode:
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
                    if begin is False:
                        begin = True
                    else: # If algo is finished, make another maze and agent
                        begin = False
                        finalFound = False
                        maze = Maze(GRIDSIZE, (1, 1), (GRIDSIZE-2, GRIDSIZE-2))
                        grid = maze.grid
                        agent = Agent(maze)

        screen.fill(BLACK) # Sets window background to black

        # Drawing grid
        for row in range(GRIDSIZE):
            for column in range(GRIDSIZE):
                color = WHITE
                if grid[row][column].value == 1:
                    if grid[row][column] == maze.startNode or grid[row][column] == maze.targetNode:
                        color = BLUE
                    else:
                        color = GREEN
                elif grid[row][column].value == 3:
                    if grid[row][column] == maze.startNode or grid[row][column] == maze.targetNode:
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
