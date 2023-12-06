import math

class Node:

    def __init__(self, xCoord: int, yCoord: int):
        # Node Class Initialisation

        # Costs and Node Value
        self.value = 0 # Determines node status
        self.gCost = None # Distance traversed to get to node
        self.hCost = 0 # Distance from End (Heuristic)
        self.fCost = 0 # Total Cost (gCost + hCost)

        # Node Positioning
        self.x = xCoord
        self.y = yCoord
        self.parent = None
        self.links = []

    # Functions for Pathfinding Algo

    def updateCosts(self, parentNode, targetNode) -> bool:
        '''
        Function used to update gCost and parent of node if gCost is lower.

        Parameters:
        :parentNode: The node in which this node is being traversed from
        :targetNode: Node to find path to

        Raises:
        :valueError: If parentNode is None
        '''

        if parentNode == None:
            raise ValueError("Parent Node is None")

        directionCost = self.__calcDistance(parentNode)
        gCost = parentNode.gCost + directionCost

        if self.gCost == None or self.gCost > gCost:
            self.gCost = gCost
            self.parent = parentNode
            self.__updateHCost(targetNode)
            return True
        return False


    def __updateHCost(self, targetNode) -> None:
        '''
        Function used to calculate hCost of node, given a targetNode.

        Parameters:
        :targetNode: The Final Destination of path finding

        Raises:
        :valueError: Raises error when targetNode is NoneType
        '''
        if targetNode == None:
            raise ValueError("Target Node is None")

        self.hCost = self.__calcDistance(targetNode)
        self.__updateFCost()


    def __updateFCost(self) -> None:
        '''
        Internal function used to update fCost of none
        '''
        self.fCost = self.hCost + self.gCost

    def __calcDistance(self, node) -> int:
        '''
        Internal function used to calculate distance between self and another node
        '''
        # return math.floor(math.sqrt((node.y-self.y)**2+(node.x-self.x)**2) * 10) # SLD, worse heuristic
        return math.floor(abs(node.y-self.y)+abs(node.x-self.x) * 10)

    # Functions for maze generation Algo
    def linkNode(self, node) -> None:
        '''
        Function to link nodes together

        Raises:
        :ValueError: when node is not a direct neighbour
        '''
        # if self.__calcDistance(node) !=  10:
        #     raise ValueError("Node to link is not direct neighbour")
        self.links.append(node)
        node.links.append(self)

    def isLinked(self, node) -> True:
        return node in self.links
    
    def __lt__(self, other) -> bool:
        return self.fCost < other.fCost


