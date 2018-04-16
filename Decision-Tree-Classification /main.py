
import sys
import csv
import numpy as np
import random

debug = False

# Method to read file
def read_file(path="tennis.txt"):
    with open(path) as file:
        reader = csv.reader(file, delimiter="\t")
        df = list(reader)
        return df   

# Method to extract features from the testing set
def all_examples(df):
    attr =[]
    first = True
    run = 0
    possible_attr = []
    for d in df:
        if run == 0: 
            first = False
            for i in range(len(d)):
                attr.append([])
                possible_attr.append([])
            run += 1
            continue
            
        for i in range(len(d)):
            attr[i].append(d[i])
            possible_attr[i].append(d[i])
        
        run += 1
    del possible_attr[-1]
    
    new = []
    for i in possible_attr:
        i = list(set(i))
        new.append(i)
        
    possible_attr = new
    outcome = attr[-1]
    del attr[-1]
    return outcome, attr, possible_attr

# Method to extract features from the testing set
def leave_one_example(df, test):
    attr =[]
    test += 1
    first = True
    run = 0
    possible_attr = []
    for d in df:
        if run == 0: 
            first = False
            for i in range(len(d)):
                attr.append([])
                possible_attr.append([])
            run += 1
            continue
            
        elif run == test:
            run += 1
            for i in range(len(d)):
                possible_attr[i].append(d[i])
            continue
            
        for i in range(len(d)):
            attr[i].append(d[i])
            possible_attr[i].append(d[i])
        
        run += 1
    del possible_attr[-1]
    
    new = []
    for i in possible_attr:
        i = list(set(i))
        new.append(i)
        
    possible_attr = new
    outcome = attr[-1]
    del attr[-1]
    return outcome, attr, possible_attr


# Method to partition the data in a particular node
def partition(listVals):
    return {val: (listVals==val).nonzero()[0] for val in np.unique(listVals)}

# entrophy function
def entropy(classifications):
    ent = 0
    value, counts = np.unique(classifications, return_counts=True)
    
    freqs = counts.astype('float')/len(classifications)
    for prob in freqs:
        if prob != 0.0:
            ent -= prob * np.log2(prob)
    return ent

# Method to calculate the information gain of a particular node
def information_gain(y, x):

    res = entropy(y)

    # We partition x, according to attribute values x_i
    val, counts = np.unique(x, return_counts=True)
    freqs = counts.astype('float')/len(x)
    
    if debug:
        print("X ",x)
        print("VAL ", val)
        print("C ", counts)
        print(freqs)
        print()
    
    # We calculate a weighted average of the entropy
    for prob, v in zip(freqs, val):
        if debug:
            print("prob ", prob)
            print("v ", v)
            print("x ", x)
            print(x == v)
            print(y[x == v])
            print()
        
        res -= prob * entropy(y[x == v])

    return res

# Method to check if a node contains only one classification
def has_one_class(classification):
    return len(set(classification)) == 1

# Method to calculate plurality value of a node
def plurality_value(y):
    val, counts = np.unique(y, return_counts=True)
    
    maxval = max(counts)
    indices = [index for index, v in enumerate(counts) if v == maxval]
    
    # If there is a tie in the number of yes and no, then return no
    if not all(map(lambda x: x == counts[0], counts)):
        return 'no'
    index = indices[0]
    return val[index]

# A recursive function that makes the decision tree by splitting every node with the best possible attribute
def recursive_split(x, y, head, possible_attr, parent_plurality = None):

    # If all examples have same classification, return the classification
    if has_one_class(y):
        return y[0]
    
    # if examples is empty, return pluraity of the parent
    if len(y) == 0:
        return parent_plurality
    
    # if attribute is empty, return the plurarity of the node
    if len(x.T) == 0:
        return plurality_value(y)
    
    plurality = plurality_value(y)
    
    # ----------------------------------------------------------------------
    # Section to get attribute that gives the highest information_gain {
    
    
    # Calculate a list of gains for all the attributes splits
    gains = np.array([information_gain(y, x_attr) for x_attr in x.T])
    if debug:
        print("###########################")
        print(gains)
        print(np.argmax(gains))
        print("###########################")
    
    # selected the attribute with highest gains (this only takes the index as that is easy to use for later use)
    selected_attr = np.argmax(gains)
    
    # } ----------------------------------------------------------------------
    
    # If the gain is very small, it is due to floating point error in computer, so skip that and return the classification
    if np.all(gains < 1e-6):
        return plurality_value(np.array(y))
    
    if debug:
        print("X ", x)
        print("#########lll")
        print("Sel ", x[:, selected_attr])
    
    # Split using the selected attribute
    sets = partition(x[:, selected_attr])
    
    # Adding attributes values that are not in the testing set examples
    for v in possible_attr[selected_attr]:
        if v not in list(sets.keys()):
            sets[v] = np.array([], dtype='int64')
    
    if debug: print(sets)
    
    result = {}
    for k, v in sets.items():
        y_child = y.take(v, axis=0)
        if debug: print("y_child ", y_child)
        x_child = x.take(v, axis=0)
        if debug: print("x_child ", x_child)
        result["%s = %s" % (head[selected_attr], k)] = recursive_split(x_child, y_child, head, possible_attr, plurality)
        if debug: print("--------")
        
    return result

# Method to print tree and return count of number of nodes
    
#https://stackoverflow.com/questions/3229419/how-to-pretty-print-nested-dictionaries
def pretty(d, printTree, indent=0):
    num_nodes = 0
    for key, value in d.items():
        num_nodes += 1
        if printTree: print('\t' * indent + str(key))
        if isinstance(value, dict):
            num_nodes += pretty(value, printTree, indent+1)
            
        else:
            if printTree: print('\t' * (indent+1) + str(value))
            num_nodes += 1
    return num_nodes

# Method to get attribute index in a list
def get_attr_index(attr, head):
    return head.index(attr)

# Method to get key of the child dictionary path like 'outlook = sunny' given outlook
def get_key(attr, test, head):
    index = get_attr_index(attr, head)
    key = attr +' = '+ test[index]
    return key

# Method to return the prediction of decision tree
def predict(test_set, tree, head):
    if not isinstance(tree,dict):
        return tree
    attr = next(iter(tree)).split()[0]
    child_key = get_key(attr, test_set, head)
    child_tree = tree[child_key]
    return predict(test_set, child_tree, head)

# Method to check if the decision tree predicted the outcome correctly
def match(test_set, tree, head):
    return test_set[-1] == predict(test_set, tree, head)

# Leave one out cross validation method
def cross_validation(path, printTree = False):
    ls = []
    df = read_file(path)
    head = df[0]
    num_examples = len(df) -1
    for i in range(num_examples):
        y, x, attr = leave_one_example(df, i)
        test = df[i+1]
        X = np.array(x).T
        Y = np.array(y)
        tree = recursive_split(X, Y, head, attr)
        num_of_nodes = pretty(tree, printTree)
        if printTree: print("\nThe number of nodes is: ", num_of_nodes, "\n")
        ls.append(match(test, tree, head))

    accuracy = sum(ls)/len(ls)
    print("The leave-one-out cross validation accuracy is: ", accuracy)
    print()
    return accuracy

# Method to generate tree for all examples provided in the dataset
def training_accuracy(path):
    s = []
    df = read_file(path)
    head = df[0]
    y, x, attr = all_examples(df)
    X = np.array(x).T
    Y = np.array(y)
    tree = recursive_split(X, Y, head, attr)
    print("\nReading file ", path)
    print()
    num_of_nodes = pretty(tree, True)
    print("\nThe number of nodes: ", num_of_nodes)
    print()
    
    # Calculating training accuracy
    num_examples = len(df)
    ls = []
    for i in range(1, num_examples):
        test = df[i]
        ls.append(match(test, tree, head))
    accuracy = sum(ls)/len(ls)
    print("The training accuracy is: ", accuracy)
    print()
    return accuracy
    

if __name__ == "__main__":
    #if len(sys.argv) != 2:
        #print("Please provide filename as the first argument: Ex. main.py pets.txt")
        #exit()
        
    filename = "./data_files/titanic2.txt"
    print("The tree is :\n")
    training_accuracy(filename)
    
    cross_validation(filename, False)
