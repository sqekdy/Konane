## Konane, a hawaiian board game.  

### Overview :  A fully functional implementation of the game, Konane.  

### About Game:   
          . The board can be of any size (should be squared for eg., 4*4, 8*8 etc). We have 8*8 board in this implementation.  
          . Two players play the game, alternating the moves. Two categories of player are "black" and "white"  
          . Each of the player remove one of their sprite, (or army) from the board initially, (the removal of opposite players should be next  to each other in horizontal or vertical direction).  
          . The players can either move horizontolly or vertically, but not diagonally.  
          . The theme of the game is to continue to have a move for oneself. If a player fails to move in the board at a particular instance, it looses the game.  
          . Valid move is to jump on even numbers, wrt to the present position (for eg, 2 steps, 4 steps and so on). Also, the destination cell should be empty for the moving player to rest on. All the intermediate cells from soruce to destination, should have combination of opposite players and empty cell.  
          . For eg.,   
              -> source (white) --> black sprite --> destination (empty cell)  
              -> source (white) --> black sprite --> empty cell --> black sprite --> destination (empty cell)  
              
### Implementation:   
          . There are several files, in this respository for the implementation which are discussed below.  
          . Black.png, Red.png, White.png -> player represenation image files.  
          . game.py -> Module for the User Interface. Draws the board, and keeps it updated as the game progesses.  
          . Player.py -> Describes the Player object, and its method.  
          . Board.py -> Module for board representation and its behaviour such as updating state of board, calculating static Evaluation Function (SEF), checking if game over et al.  
          . aiEngine.py -> Module that implements minimax algorithm with alpha-beta pruning, to find the next best move by the AI.  
          . gameEngine.py -> Module that initializes the game, and fires up the UI. **Game Entry Point**  
          

### Requirements:  
          . Python 3.6 or above  
          . Install "pygame" library using  -- pip install pygame--  

### Run the game:  
          . Clone this repository in your local system.  
          . Run the game using " python gameEngine.py".  
          . Follow the on-screen (console) instruction to choose the player type, get the initial board, and start playing.  

### How to play:   
          . Click on your player (either black/white) that you wish to move. If a player is set to move, the selection is depicted by green border around the player. Hovering, to the cells is depicted by the red selection.  
          . Click on the destination empty cell to move your selected player.  
          . Wait for AI to make a move, and continue.  
          
### Known Issues:  
          . If a user clicks a player, that cannot make a valid move (marked by green selection) by mistake, it cannot be undone and any move issued for that player is discarded. In simple terms, if you miss to make a correct move, you loose a move and AI makes the next move.

#### Note:  
          . Use master branch for playing the game with console input, or to play with UI use the UI branch.


          
              
              
