# gameOfLife
## Implementation of Game of Life in Python

The Game of Life is a cellular automaton devised by the British mathematician John Conway. It's a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input. 
One interacts with the Game of Life by creating an initial configuration and observing how it evolves.

## RULES:
1.- Any live cell with 2 or 3 live neighbours survives.

2.- Any dead cell with 3 or more live neighbours becomes a live cell.

3.- All other live cells die in the next generation. Similarly, all other dead cells stay dead.

EXAMPLE:

![Game_of_life_blinker](https://user-images.githubusercontent.com/44360352/147565845-5ca7b260-469e-459f-93a8-f750ac5de856.gif)

## IMPLEMENTATION
In this implementation we use the libraries numpy and pygame. 
The first one will help us with the matrix definition of the game while the pygame library will be used to provide the game with a graphical interface.

NOTE: throughout the code you will find some comments that will help you to understand the implementation.
