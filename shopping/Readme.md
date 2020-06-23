# Shopping Analysis
### Determine which customers proceed to buy items and which customers just browse through items

<b> Features in data</b>
<ul>
<li> Administrative,Informational and ProductRelated columns show how many pages of each the user visited and the<br>
corresponding Duration columns show how much time the user spent in each if these columns</li>
<li>BounceRates,ExitRates and pageValues represent the Analytics of the pages visited by the user</li>
<li>SpecialDay shows if the day the user visited is close to a special occasion</li>
<li>OperatingSystems,Browser,Region and TrafficType represent individual infrmation about a user</li>
<li>VisitorType tells whether or not the customer is a returning customer</li>
<li> Weekend tells if the day of browsing was a weekend or not</li>
<li>Finally, Revenue tells if the purchase was made or not</li>
</ul>
<hr>

## Method.

K-NearestNeighbors algorithm is one where each training example is assigned a label depending on the labels of its k nearest neighbors when the datapoints are plotted.
<br>
In this algorithm. K=1 is taken i.e., the datapoint is assigned the same label as the one closest to it.
<br>
This is not very accuracte as outliers in the dataset cause mislabelling of the data.

<hr>

## Output
<b>
Accuracy: 83%<br>
Sensitivity : 40%<br>
Specificity: 90%
</b>
<br><br>
<img src='Outputs/output.png'>
