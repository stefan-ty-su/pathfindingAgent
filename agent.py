from maze import Maze
from node import Node
import heapq

class Agent:

    def __init__(self, layout: Maze, start: Node, target: Node) -> None:
        """
        
        """
        self.layout = layout
        self.grid = layout.grid
        self.gridSize = layout.gridSize

        self.startNode = start
        self.startNode.gCost = 0
        self.targetNode = target

        self.openNodes = [self.startNode]
        heapq.heapify(self.openNodes)
        self.closedNodes = []
    
    def getLowestCostNode(self) -> Node:
        '''
        Function gets the lowest node in a given array of nodes

        Raises:
        :valueError: when the array is empty

        Returns:
        :Node: the node with the lowest fCost
        '''

        if self.openNodes == None or len(self.openNodes) == 0:
            raise ValueError(f'Node Array is {self.openNodes}')

        minNode = heapq.heappop(self.openNodes)
        return minNode

    # Astar Algo
    def updateChildNode(self, node: Node, parentNode: Node) -> None:
        '''
        Changes Costs of child node
        '''
        if (node.value != 3) and (node.value != 4):
            newPath = node.updateCosts(parentNode, self.targetNode)
            if newPath:
                heapq.heappush(self.openNodes, node)
                node.value = 2

    def updateNeighbours(self, node: Node) -> None:
        '''
        Function sets costs of neighbouring nodes and places them in array of open Nodes

        param:
        :node: node which neighbours are to be generated

        raises:
        :valueError: if no node is given
        '''

        if node == None:
            raise ValueError("Input arguments are incorrect")

        if node.y > 0 and node.isLinked(self.grid[node.y-1][node.x]):
            self.updateChildNode(self.grid[node.y-1][node.x], node)

        if node.y < self.gridSize-1 and node.isLinked(self.grid[node.y+1][node.x]):
            self.updateChildNode(self.grid[node.y+1][node.x], node)

        if node.x > 0 and node.isLinked(self.grid[node.y][node.x-1]):
            self.updateChildNode(self.grid[node.y][node.x-1], node)

        if node.x < self.gridSize-1 and node.isLinked(self.grid[node.y][node.x+1]):
            self.updateChildNode(self.grid[node.y][node.x+1], node)

    def findPath(self, finalNode: Node) -> None:
        list = []
        if finalNode != None:
            self.findPathAux(list, finalNode)
            for node in list:
                node.value = 1

    def findPathAux(self, list: list, node: Node) -> None:
        list.append(node)
        if node.parent != None:
            self.findPathAux(list, node.parent)