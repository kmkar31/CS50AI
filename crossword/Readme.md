<h1> AI Crossword Solver</h1>

This Program implements a <b>Recursive Backtracking Algorithm</b> that iterates through a set of words to determine possible solutions to the given crossword.
Each set of blank spaces required to be filled in by a word is considered to be a variable. The structure and word set for the crossword can be found in the
/data folder.
<br>

<hr>
<h2>Method</h2>
<h3>Node-Consistency</h3><br>
A Node(read Variable)-Consistency being satisfied implies that every single Unary Constraint(constraints that depend only on that variable) are satisfied.
<br><br>
<h3>Arc-Consistency</h3><br>
Arc-Consistency refers to binary constraints between two nodes connected by an edge being satisfied.
<br><br>

<h3>Constraints:</h3><br><ol>
<li><b>Unary Constraints</b>(ensured by Node-Consistency):
<ul>
<li> The word assigned to a variable must have the same number of letters as the number of blanks to fill for that variable</li>
</ul></li>
<li><b>Binary Constarints</b>(ensured by Arc Consistency):
<ul>
<li> The common blank space of two different variables must be filled by the same letter</li>
</ul></li>
<li><b> No two variables may hve the same word</b></li>
</ol>

<h3>Domain</h3><br>
Domain refers to the set of words available for that particular variable.<br>
Initially, the entire set of words is set as a words domain.<br>
Node-Consistency is ensured first followed by Arc Consistency
<br><br>

<b>The BackTracking works as follows:</b>
<br><ol>
<li>Picks a Random Variable from the list of unassigned variables.</li>
<li> Assigns a random word to that variable from its domain</li>
<li> Based on the provided constraints, it continues assigning words to variables until it either acheives a solution or hits a dead-end</li>
<li> If a dead-end is hit, the function backtracks one assignment at a time and reassigns a new word and the process is repeated</li>
</ol>
<br><br>

<h3>Picking a Variable</h3>
Though this process can be done randomly, a solution can be reached faster if a variable to e assigned is picked as follows:
<ol>
<li> Sort the variables according to the number of words in their domain.</li>
<li> For those variables with equal domain sizes, order them according to decreasing number of neighbors</li>
</ol>
<br>
This way, there is lesser chance of an assignment order failing and hence reduces the number of times an algorithm may backtrack.
<br><br>

<h3> Picking which word to choose</h3>
The word which causes the least decrease in the domain sizes of the variable's neighbors is preferred first.
<br>This is due to the fact that a highly specific path has a larger chance of failing as compared to one that keeps its options open.
<br><br>
<hr>
<h2>Outputs</h2>
<img src='Outputs/Crossword 0/Crossword0.png'>
<img src='Outputs/Crossword 1/Crossword1.png'>
<img src='Outputs/Crossword 2/Crossword2_try3.png'>
<img src='Outputs/Crossword 2/Crossword2_try6.png'>
<img src='Outputs/Crossword 2/Crossword2_try9.png'>
