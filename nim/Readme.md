# NIM
### An AI Opponent for the NIM strategy game
<hr>
<b>Rules:</b>
<ul>
<li>A Player can remove as many objects as he/she wants from a <b>single</b> pile in one move</li>
<li>The number of objects removed however must be greater than 0</li>
<li>Each player takes turna st playing the game making moves according to the rules above</li>
<li>The Objective is to make sure that you don't remove the last object</li>
</ul>
<hr>

## Method

The Program makes use of a Reinforcement leraning technique known as Q-Learning algorithm.
<br>
In this algorithm, the AI is handed out a reward or a punishment based on the moves it makes.
<br>
The magnitude of the reward or punishment is called <b>Q(s,a)</b> and is a function of the current state and subsequent action.
<br>
A state refers to the current arrangement of objects contained in piles whereas an action refers to the AI making a move
<br>
This reward is updated during the training ptocess as the AI makes moves resulting in a victory or defeat
<br>
The AI essentially maps out every single path the game may take and constructs the moves which would result in a victory.
<br>
The &epsilon;-Greedy approach leads the algorithm to make random move so that more paths are explored.
<hr>

## Output
<br>
<b>GamePlay</b> 
<img src='GamePlay/GamePlay_img.png'>
