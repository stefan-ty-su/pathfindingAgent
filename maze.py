from node import Node
import random

class Maze:

    def __init__(self, gridSize: int, start: tuple, target: tuple) -> None:
        # Creating Grid
        self.grid = []
        self.gridSize = gridSize
        for row in range(self.gridSize):
            self.grid.append([])
            for column in range(self.gridSize):
                self.grid[row].append(Node(column, row))

        # Algo Setup
        self.startNode = self.grid[start[0]][start[1]]
        self.startNode.value = 1 # Start Square
        self.startNode.gCost = 0

        self.targetNode = self.grid[target[0]][target[1]]
        self.targetNode.value = 1

        self.generateMaze()

    def generateMaze(self) -> None:
        '''
        Function to generate maze, using 'Recursive Back-tracker' method

        Parameters:
        :grid: Grid Object of Nodes
        :startNode: node at which the maze will start
        '''
        nodeStack = [self.startNode]
        nodeMax = self.gridSize**2
        visitedArr = [self.startNode]
        self.generateMazeAux(self.grid, nodeStack, visitedArr, False)

    def generateMazeAux(self, grid: list, nodeStack: list, visitedArr: list, backTracking: bool) -> None:
        '''
        Auxillary Function for Recursive Back-tracker method of generateMaze()
        '''
        current = nodeStack[-1] # 'popping' top of stack
        if backTracking == False:
            visitedArr.append(current)
        neighbours = []

        if len(visitedArr) == self.gridSize**2+1:
            return

        if current.x > 0:
            left = grid[current.y][current.x-1]
            if left not in visitedArr:
                neighbours.append(left)

        if current.y > 0:
            top = grid[current.y-1][current.x]
            if top not in visitedArr:
                neighbours.append(top)

        if current.x < self.gridSize-1:
            right = grid[current.y][current.x+1]
            if right not in visitedArr:
                neighbours.append(right)

        if current.y < self.gridSize-1:
            bottom = grid[current.y+1][current.x]
            if bottom not in visitedArr:
                neighbours.append(bottom)

        if len(neighbours) == 0:
            nodeStack.pop()
            self.generateMazeAux(grid,nodeStack,visitedArr, True)
        else:
            nextNode = random.choice(neighbours)
            current.linkNode(nextNode)
            nodeStack.append(nextNode)
            self.generateMazeAux(grid,nodeStack,visitedArr, False)