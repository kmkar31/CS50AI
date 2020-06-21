<h1> Knights and Knaves</h1>
<h3>The above code is a solver for the Knights and Knaves game<h3>
<br>
<b>Rules:</b> 
<br>
<ul><li><b>Knights</b> always tell the <u>truth</u> and <b>Knaves</b> always <u>lie</u></li>
<li>Find who is a Knight and who is a Knave based on their statements.</li>
</ul>
<br><br><hr>
<h2>Method</h3>
This method uses Propositional Logic to solve the problem i.e., every single statement is transformed into a form that uses only boolean variables connected by Operators
<br>
The Operators used are : <b> AND,OR,NOT,IMPLICATION</b> and <b>BICONDITIONAL</b>
<br><br>
<b>For Example :</b> If there are two characters A and B and their statements are as follows:
<br><br>
<ol>
<li> <b>A</b>: We are both Knights</li>
<li><b>B</b>:I am a Knight but A is a Knave</li>
<br><br>
Such a Statement is encoded as:<br> <i><b>And(
<br>Or(AKnight,AKnave),
<br>Or(Bknight,Bknave),
<br>Implication(AKnave,Not(AKnight)),
<br>Implication(BKnave,Not(BKnight)),
<br>Biconditional(AKnight,And(AKnight,BKnight)),
<br>Biconditional(BKnight,And(AKnave,BKnight))
<br>)</i></b>
<br>
Where AKnight is True iff A is a Knight and AKnave is True iff A is a knave and so on.
<br><br>
<b>What This Means:</b><ul>
<li> <i>And(</i> - All of the following conditions must be True</li>
<li><i>Or(AKnight,AKnave),Or(Bknight,Bknave)</i> - Both A and B must either be a Knight or a Knave or both(in case of uncertainity)</li>
<li><i>Implication(AKnave,Not(AKnight)),Implication(BKnave,Not(BKnight))</i> - If A or B is not a Knight , they A or B must be Knave</li>
<li><i>Biconditional(AKnight,And(AKnight,BKnight))</i> - The fact that A is a Knight and so is B must be either True or False Together. This represents A's Statement.</li>
<li><i>Biconditional(BKnight,And(AKnave,BKnight))</i> - The fact that B is a Knight and A is a Knave must be True or false simultaneously. This represents B's Statement.</li>
<br><br><hr>
<h3>Model Checking Algorithm:</h3>This Algorithm checks for all possible combinations of the two states(True/False) for each and every single variable in the Model.
It then picks the statement where the above condition(called Knowledge) is True ans returns the result.
<hr>
This Algorithm represents a <b>Zeroth Order Propositional logic</b> i.e., every single state is encoded as a separate variable. In this case we had only two characters and they had only two states each.
<br>
Even So, the algorithm feels messy and tedious. In a Comlex real Life scenario with thousands of characters and states, such a model is infeasible.
<br>
For such complex cases, <b>First-Order</b>, <b>Second-Order Propositional Logic</b> were proposed.
<hr>
