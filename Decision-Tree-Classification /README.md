# Decision Tree Implementation using Python 

##Goal
For this lab we have implemented the DECISION-TREE-LEARNING algorithm as seen in
chapter 18. 
Our program reads in a tab-delimited dataset and outputs the decision tree in
the screen along with the training set accuracy and the cross validation accuracy. 

Our program uses numpy arrays to pass outcomes and attributes along to functions.We decided this was the best way to maintain consistency and make best use of some very helpful numpy libraries for counting unique values, transposing lists, partitioning subsets
and frequency calculations.

##Results 
First, we generated the trees using all the examples and tested the accuracy of our tree foreach of the examples. The accuracy score we received for this were as follows:Pets.txt - 0.86 (86\%) no of nodes: 43Tennis.txt - 1.0 (100\%) no of nodes: 12Titanic2.txt ? 0.69 (69\%) no of nodes: 36
Then we used Leave-one-out cross-validation method to check the accuracy of ourdecision trees by testing it against n examples for each dataset. For this we picked out asingle test example whose attributes were recorded (incase they weren?t observed in otherexamples) and the tree was generated using the rest of the examples. The test case wasthen used to check if the decision tree could accurately predict the outcome. The accuracyscores we received were as follows:
Pets.txt - 0.47 (47\%)Tennis.txt - 0.79 (79\%)Titanic2.txt ? 0.69 (69\%)