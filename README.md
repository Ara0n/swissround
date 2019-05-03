# Swiss round algorithm

## Objective

The objective of this algorithm is to give access to a simple o implement generic swiss round system.

## Usage

### Creating a player list

Just create a normal python list with the object `Player` in it. Each `Player` is identified with a name/id that you give him (`Player.name`) and `Player.intelligence` is a generic variable that you can use to giv your player some additional stuff (for example when you develop an AI).

### Creating the tournament

Once the player list created you can create the tournament giving it in order the player list your `Game` object and the best of format wanted.

### Playing the tournament

Once the tournament created you will have a recommended number of rounds in `Tournament.nbRounds`.  
For the number of rounds desired you do in this order:
 1) `Tournament.createRound()`
 2) `Tournament.playRound()`
 3) `Tournament.updateRank()`

### Getting the results

The final order for the rankings is available in `Tournament.ranking`, individual scores are in `Player.score`.

## Misc

- Your `Game` object must have a `play()` method and a `results` variable that equals 1 if player one wins, 2 if player 2 wins and 0 if it's a draw.
- Your `Game` object have access to the 2 player objects that fight each other in the match
- A best-of format is a format where a maximum number of games possible per match is declared, the one with the most wins at the end if the best-of wins the match. *If there is more draws than victories for one or the other player the entire match is considered drawn*
- if the number of player is odd, a fictive player player is created: the "Bye". The "Bye" must stay at 0 points and a the end of the rankings. The player playing against the "Bye" will be awarded an auto-win. Only one Bye can be awarded per player during the entire tournament.
- the tournament doesn't switch sides for the players automatically, if you want to make them alternate positions, add it in the `play()` method. Beware that even if you switch p1 victory still has to be 1 and p2 victory 2 for the value of `results`