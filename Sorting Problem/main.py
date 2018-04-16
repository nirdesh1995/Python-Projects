
# coding: utf-8

# In[ ]:

import time, random, sys, glob, os, copy
import datetime as dt
import time

sys.setrecursionlimit(1500)

#<----------------------------RANDROM NUMBER GENERATOR------------------------->
def number_generator(size):
    # Open a file
    file = open(str(size)+".txt", "w")

    # Generating random numbers
    for i in range(size):
        no = random.randrange(1,100,1)
        # Writing random numbers in the file
        file.write(str(no)+" ");

    # Close opend file
    file.close()



#<---------------------------- OUTPUT LIST ------------------------>
def writeList(list,type):

    # Checking Sort type
    if type == "m":
        name = "_MergeSort.txt"

    elif type == "i":
        name = "_InsertionSort.txt"

    elif type == "s":
        name ="_SelectionSort.txt"

    # Open a file
    file = open("Python/"+str(len(list))+name, "w")

    # Generating random numbers
    for i in list:
        # Writing the number in sorted list
        file.write(str(i)+" ")

    # Close opend file
    file.close()


#<------------------------------------ MERGE SORT --------------------------------->
def merge(S1, S2, S):
    """Merge two sorted Python lists S1 and S2 into properly sized list S."""
    i = j = 0
    while i + j < len(S):
        if j == len(S2) or (i < len(S1) and S1[i] < S2[j]):
            S[i+j] = S1[i]      # copy ith element of S1 as next item of S
            i += 1
        else:
            S[i+j] = S2[j]      # copy jth element of S2 as next item of S
            j += 1

def merge_sort(S):
    """Sort the elements of Python list S using the merge-sort algorithm."""
    n = len(S)
    if n < 2:
        return                # list is already sorted
    # divide
    mid = n // 2
    S1 = S[0:mid]           # copy of first half
    S2 = S[mid:n]           # copy of second half
    # conquer (with recursion)
    merge_sort(S1)          # sort copy of first half
    merge_sort(S2)          # sort copy of second half
    # merge results
    merge(S1, S2, S)        # merge sorted halves back into S
    #print(S)

#<----------------------------------INSERTION SORT ------------------->

def insertionSort(alist):
    for index in range(1,len(alist)):

        currentvalue = alist[index]
        position = index

        while position>0 and alist[position-1]>currentvalue:
            alist[position]=alist[position-1]
            position = position-1

        alist[position]=currentvalue

#<--------------------------- SELECTIONSORT ---------------------------------->
def selectionSort(alist):
    for fillslot in range(len(alist)-1,0,-1):
        positionOfMax=0
        for location in range(1,fillslot+1):
            if alist[location]>alist[positionOfMax]:
                positionOfMax = location

        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp

# <----------------- METHOD TO MAKE LIST FROM FILE ----------------->

def read_filenum(file):
    alist=[]
    for line in file:
        line = line.strip()
        blist = line.split()
        blist = [int(i) for i in blist]
        alist.extend(blist)
    return alist

#<---------------------------------- GENERATING NUMBERS ------------------------------------------>
number_generator(10)
number_generator(100)
number_generator(1000)
number_generator(10000)
number_generator(100000)

#<---------------------------------- OPENING FILES ----------------------------------------------->
file1 = open('10.txt','r')
file2 = open('100.txt','r')
file3 = open('1000.txt','r')
file4 = open('10000.txt','r')
file5 = open('100000.txt','r')

#<---------------------------------- CREATING LIST FROM FILE -------------------------------------->

list1 = read_filenum(file1)
list2 = read_filenum(file2)
list3 = read_filenum(file3)
list4 = read_filenum(file4)
list5 = read_filenum(file5)

list6 = copy.deepcopy(list1)
list7 = copy.deepcopy(list2)
list8 = copy.deepcopy(list3)
list9 = copy.deepcopy(list4)
list10 = copy.deepcopy(list5)

list11 = copy.deepcopy(list1)
list12 = copy.deepcopy(list2)
list13 = copy.deepcopy(list3)
list14 = copy.deepcopy(list4)
list15 = copy.deepcopy(list5)


# <------------------------------------ MERGE-SORT -------------------------------------------------->

print("MergeSort")
print("Input size (N): (# of numbers) \t\t Time cost:")


t0 = time.time()
merge_sort(list1)
merge_time1 = (time.time()-t0)*1000000

print("10 \t\t\t\t\t", merge_time1, "microseconds")

t0 = time.time()
merge_sort(list2)
merge_time2 = (time.time()-t0)*1000000
print("100 \t\t\t\t\t", merge_time2, "microseconds")


t0 = time.time()
merge_sort(list3)

merge_time3 = (time.time() - t0)*1000000
print("1000 \t\t\t\t\t", merge_time3, "microseconds")

t0 = time.time()
merge_sort(list4)
merge_time4 = (time.time()-t0)*1000000
print("10000 \t\t\t\t\t", merge_time4, "microseconds")



t0 = time.time()
merge_sort(list5)
merge_time5 = (time.time()-t0)*1000000
print("100000 \t\t\t\t\t", merge_time5, "microseconds")


writeList(list1,"m")
writeList(list2,"m")
writeList(list3,"m")
writeList(list4,"m")
writeList(list5,"m")








print("===================================================================================================================")
print()


# <------------------------------------ SELECTIONSORT ----------------------------------------------->

print("Selection Sort")
print("Input size (N): (# of numbers) \t\t Time cost:")

t0 = time.time()
selectionSort(list6)
select_time1 = (time.time()-t0)*1000000
print("10 \t\t\t\t\t", select_time1, "microseconds")



t0 = time.time()
selectionSort(list7)
select_time2 = (time.time()-t0)*1000000
print("100 \t\t\t\t\t", select_time2, "microseconds")

t0 = time.time()
selectionSort(list8)
select_time3 = (time.time()-t0)*1000000
print("1000 \t\t\t\t\t", select_time3, "microseconds")

t0 = time.time()
selectionSort(list9)
select_time4 = (time.time()-t0)*1000000
print("10000 \t\t\t\t\t", select_time4, "microseconds")

t0 = time.time()
selectionSort(list10)
select_time5 = (time.time()-t0)*1000000
print("100000 \t\t\t\t\t", select_time5, "microseconds")

writeList(list6,"s")
writeList(list7,"s")
writeList(list8,"s")
writeList(list9,"s")
writeList(list10,"s")








print("===================================================================================================================")
print()


# <------------------------------------ INSERTION SORT ----------------------------------------------->

print("Insertion Sort")
print("Input size (N): (# of numbers) \t\t Time cost:")


t0 = time.time()
insertionSort(list11)
insert_time1 = (time.time()-t0)*1000000
print("10 \t\t\t\t\t", insert_time1, "microseconds")



t0 = time.time()
insertionSort(list12)
insert_time2 = (time.time()-t0)*1000000
print("100 \t\t\t\t\t", insert_time2, "microseconds")


t0 = time.time()
insertionSort(list13)
insert_time3 = (time.time()-t0)*1000000
print("1000 \t\t\t\t\t", insert_time3, "microseconds")


t0 = time.time()
insertionSort(list14)
insert_time4 = (time.time()-t0)*1000000
print("10000 \t\t\t\t\t", insert_time4, "microseconds")


t0 = time.time()
insertionSort(list15)
insert_time5 = (time.time()-t0)*1000000
print("100000 \t\t\t\t\t", insert_time5, "microseconds")



writeList(list11,"i")
writeList(list12,"i")
writeList(list13,"i")
writeList(list14,"i")
writeList(list15,"i")



print("===================================================================================================================")
print()
# <-------------------------------------- CLOSING FILE --------------------------------------------------->

file1.close()
file2.close()
file3.close()
file4.close()
file5.close()

# <-------------------------------------- PRINTING OUTPUT --------------------------------------------------->

# <------------------------------------ MERGE SORT ---------------------------------------->

# <------------------------------------ INSERTION SORT ---------------------------------------->


# <------------------------------------ SELECTIONSORT ---------------------------------------->


delete_res = input("Do you want to delete the generated files (Y/N): ")
while True:

    if delete_res.upper() == "Y" or delete_res.upper()=="N":
        if delete_res.upper() == "Y":
            for file in glob.glob("*.txt"):
                os.remove(file)

            break
        else:
            break
    else:
        print("The response is invalid, please type again Y or N")
        delete_res = input("Do you want to delete the generated files (Y/N): ")
        


# In[ ]:



