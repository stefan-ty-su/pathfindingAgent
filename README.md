# pathfindingAgent
## Description
The repository is a demonstration of using the A* Path-finding algorithm to find an optimal path (determined by distance travelled) between a starting location to a target location.
- The path-finding algorithm utilised is A*, using a Graph Search approach
- Recursive back-tracking is used for the generation of the maze.

## Usage
Currently, there parameters cannot be input to change the size of the maze, nor the points of interest.
- Top left is the starting location
- Bottom right is the target location
To run, run the following in console:

```console
> python main.py
```
### Controls
- Left Click - makes an untraversable cell for the agent
- Right CLick - makes a cell traversable for the agent
- Spacebar - starts the path-finding algorithm

### Interpretation
The program represents the state of a node using colours:
- Blue - Node that is either a target or starting location
- Red - Location that has already been traversed (closed node)
- Green - Locations which are part of the solution path
- Aqua - Locations which the agent is currently at
- Black - A location which is untraversable by the agent
