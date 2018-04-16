
To run our program simply use the following command: 
$python3 main.py tennis.txt

The following is our list of functions and their functionalities:

read_file(path="tennis.txt"): - Takes in a path and reads the file line by line and stores the tab separated values in a lists of lists and returns it. 

all_examples(df):Takes in the list of examples and returns the outcomes, the attributes corresponding to those outcomes and a list of possible attributes after iterating over all examples. 

leave_one_example(df, test): Used for leave one out cross validation. Takes in the test example index and list with all the examples and does the same thing as ‘all_examples’ except it leaves out the test example in the outcomes and attributes but saves new attributes(if discovered) in the set of possible attributes.  

partition(listVals): Partitions the list into subsets. 

entropy(s): Returns entropy value. 

information_gain(y, x): Takes in outcomes and attributes and returns value for information gain. 

has_one_class(classification): Returns true if pure set. 
 
plurality_value(y):Calculates plurality value of a node. If there is a tie in the number of yes and no, then return no.  

recursive_split(attributes, outcomes, head, possible_attr, parent_plurality = None): Recursive function that makes the decision tree by splitting every node with the best possible attribute. Returns the best split. 

pretty(d, printTree, indent=0): Prints the tree in a properly indented format and returns the count of number of nodes

get_attr_index(attr, head):Method to get attribute index in a list. 

get_key(attr, test, head): Method to get key of the child dictionary path like 'outlook = sunny' given outlook.

predict(test_set, tree, head): Returns the prediction of the decision tree.

match(test_set, tree, head): Checks if the decision tree predicted the outcome correctly. 

cross_validation(path, printTree = False): Goes through all n examples and builds a tree each time excluding one example and uses the left out example to predict the accuracy of the tree.

training_accuracy(path):Uses the tree built using all examples to calculate the accuracy by going over each example and checking whether our tree correctly predicted it or not. Returns the accuracy score. 

********

....................................................................................
