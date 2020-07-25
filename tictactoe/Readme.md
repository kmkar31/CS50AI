# Tic-Tac-Toe

## Use a Minimax algorithm to search all possible moves and take the optimal action
### The AI can never lose a game. It can only draw one.

![Minimax Working](https://www.researchgate.net/publication/262672371/figure/fig1/AS:393455625883662@1470818539933/Game-tree-for-Tic-Tac-Toe-game-using-MiniMax-algorithm.png)

<hr>

## Implementation

This is an example of an adverserial search algorithm where an agent either tries to maximise or minimise the reward from all possible actions resulting out of the opponents move.

The reward is recursively calculated as the <b>v = max(v, minValue(result(board, action)))</b> or <b>v = min(v, maxValue(result(board, action)))</b>. 

<hr>
<br><br>
Output:
<br><br>

![Game1](tictactoe/g1.png)
![Game2](tictactoe/g2.png)
