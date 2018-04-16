#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <time.h>
#include <cstdio>
//<----------------------------RANDOM NUMBER GENERATOR------------------------->
void copyarray(int arr1[], int arr2[], int arr3[] ,int i){
    int b;
    for(b=0; b<i; b++){
        arr2[b] = arr1[b];
        arr3[b] = arr1[b];
    }
}


void number_generator(int size){
  char fsize[20];
  // Open a file
  FILE * fp;
  sprintf(fsize, "%d", size);
  strcat(fsize, ".txt");
  //printf("%s", fsize);
  fp = fopen(fsize,"w");

  // Generating random numbers
  for (int i = 0; i < size; i++) {
    int no = rand() % 100;
    // Writing random numbers in the file
    fprintf(fp, "%d ", no);
  }
  // CLose file
  fclose(fp);
}



//<---------------------------- OUTPUT LIST ------------------------>
void writeList(int list[], char type[1], int list_size){

    char name[40];
    char fname[40] = "C/";
    // Checking Sort type
    if (strcmp(type, "m") == 0){
      strcpy(name,"_MergeSort.txt");
    }
    else if (strcmp(type, "i") == 0){
      strcpy(name,"_InsertionSort.txt");
    }
    else if (strcmp(type, "s") == 0){
      strcpy(name,"_SelectionSort.txt");
    }

    char fsize[40];
    sprintf(fsize, "%d", list_size);
    strcat(fsize, name);
    strcat(fname, fsize);

    // Open a file
    FILE *fp;
    fp = fopen(fname,"w");
    // Generating random numbers
    for (int i = 0; i < list_size; i++){
      fprintf(fp, "%d ", list[i]);
    }

    // Close file
    fclose(fp);
}

/* <----------------------------------INSERTION SORT ------------------->*/
/* Function to sort an array using insertion sort*/
void insertionSort(int arr[], int n)
{
   int i, key, j;
   for (i = 1; i < n; i++)
   {
       key = arr[i];
       j = i-1;

       /* Move elements of arr[0..i-1], that are
          greater than key, to one position ahead
          of their current position */
       while (j >= 0 && arr[j] > key)
       {
           arr[j+1] = arr[j];
           j = j-1;
       }
       arr[j+1] = key;
   }
}

// <------------------------------------MERGESORT------------------------->

void merge(int arr[], int l, int m, int r)
{
    int i, j, k;
    int n1 = m - l + 1;
    int n2 =  r - m;

    /* create temp arrays */
    int L[n1], R[n2];

    /* Copy data to temp arrays L[] and R[] */
    for (i = 0; i < n1; i++)
        L[i] = arr[l + i];
    for (j = 0; j < n2; j++)
        R[j] = arr[m + 1+ j];

    /* Merge the temp arrays back into arr[l..r]*/
    i = 0; // Initial index of first subarray
    j = 0; // Initial index of second subarray
    k = l; // Initial index of merged subarray
    while (i < n1 && j < n2)
    {
        if (L[i] <= R[j])
        {
            arr[k] = L[i];
            i++;
        }
        else
        {
            arr[k] = R[j];
            j++;
        }
        k++;
    }

    /* Copy the remaining elements of L[], if there
       are any */
    while (i < n1)
    {
        arr[k] = L[i];
        i++;
        k++;
    }

    /* Copy the remaining elements of R[], if there
       are any */
    while (j < n2)
    {
        arr[k] = R[j];
        j++;
        k++;
    }
}

/* l is for left index and r is right index of the
   sub-array of arr to be sorted */
void mergeSort(int arr[], int l, int r)
{
    if (l < r)
    {
        // Same as (l+r)/2, but avoids overflow for
        // large l and h
        int m = l+(r-l)/2;

        // Sort first and second halves
        mergeSort(arr, l, m);
        mergeSort(arr, m+1, r);

        merge(arr, l, m, r);
    }
}



// <------------------------------------SELECTIONSORT------------------------->
void SelectionSort(int arr[], int n)
{
//pos_min is short for position of min
    int pos_min,temp;

    for (int i=0; i < n-1; i++)
    {
        pos_min = i;//set pos_min to the current index of array

        for (int j=i+1; j < n; j++)
        {

        if (arr[j] < arr[pos_min])
                   pos_min=j;
    //pos_min will keep track of the index that min is in, this is needed when a swap happens
        }

    //if pos_min no longer equals i than a smaller value must have been found, so a swap must occur
            if (pos_min != i)
            {
                 temp = arr[i];
                 arr[i] = arr[pos_min];
                 arr[pos_min] = temp;
            }
    }
}


// <----------------- METHOD TO MAKE LIST FROM FILE ----------------->

void read_filenum(char name[100],int list[]){
  FILE *fp;
  fp = fopen(name,"r");

  int i = 0;
  int b = 0;
  while(!feof(fp)){
    fscanf(fp, "%d", &i);
    list[b] = i;
    b++ ;
    }
  }



//---------------------Driver Program----------------------------------automer

int main(){
    char test[1];
    printf("If you have not run the python program, this program generates the random numbers else it uses the same problem to sort. \n ");
    printf("Have you run the Python program? (Y/N): \n");
    scanf("%s", test);
    if (strcmp(test, "y") != 0 && strcmp(test, "Y") != 0){
        number_generator(10);
        number_generator(100);
        number_generator(1000);
        number_generator(10000);
        number_generator(100000);
    }
    
    
    
        
    // Reading files
    int list1[10],list2[100],list3[1000],list4[10000],list5[100000];
    int list6[10],list7[100],list8[1000],list9[10000],list10[100000];
    int list11[10],list12[100],list13[1000],list14[10000],list15[100000];

    read_filenum("10.txt",list1);
    read_filenum("100.txt",list2);
    read_filenum("1000.txt",list3);
    read_filenum("10000.txt",list4);
    read_filenum("100000.txt",list5);

    copyarray(list1,list6, list11,10);
    copyarray(list2,list7,list12,100);
    copyarray(list3,list8,list13,1000);
    copyarray(list4,list9,list14,10000);
    copyarray(list5,list10,list15,100000);

    clock_t start_t, end_t;
    double diff_t;





    printf("MergeSort");
    printf("Input size (N): (# of numbers) \t Time cost:\n");

    start_t = clock();
    mergeSort(list1,0,10);
    end_t = clock();
    diff_t  = (double)(end_t - start_t)*1000000/ CLOCKS_PER_SEC ;
    printf("10 \t\t\t\t\t %f Microseconds\n", diff_t);
    writeList(list1, "m", 10);

    start_t = clock();
    mergeSort(list2,0,100);
    end_t = clock();
    diff_t  = (double)(end_t - start_t)*1000000/ CLOCKS_PER_SEC ;
    printf("100 \t\t\t\t\t %f Microseconds\n", diff_t);
    writeList(list2, "m", 100);

    start_t = clock();
    mergeSort(list3,0,1000);
    end_t = clock();
    diff_t  = (double)(end_t - start_t)*1000000/ CLOCKS_PER_SEC ;
    printf("1000 \t\t\t\t\t %f Microseconds\n", diff_t);
    writeList(list3, "m", 1000);

    start_t = clock();
    mergeSort(list4,0,10000);
    end_t = clock();
    diff_t  = (double)(end_t - start_t)*1000000/ CLOCKS_PER_SEC ;
    printf("10000 \t\t\t\t\t %f Microseconds\n", diff_t);
    writeList(list4, "m", 10000);

    start_t = clock();
    mergeSort(list5,0,100000);
    end_t = clock();
    diff_t  = (double)(end_t - start_t)*1000000/ CLOCKS_PER_SEC ;
    printf("100000 \t\t\t\t\t %f Microseconds\n\n", diff_t);
    writeList(list5, "m", 100000);

//-----------------------------------------------------------------------------------------

    printf("InsertionSort");
    printf("Input size (N): (# of numbers) \t Time cost:\n");
    start_t = clock();
    insertionSort(list6,10);
    end_t = clock();
    diff_t  = (double)(end_t - start_t)*1000000/ CLOCKS_PER_SEC ;
    printf("10 \t\t\t\t\t %f Microseconds\n", diff_t);
    writeList(list6, "i", 10);


    start_t = clock();
    insertionSort(list7,100);
    end_t = clock();
    diff_t  = (double)(end_t - start_t)*1000000/ CLOCKS_PER_SEC ;
    printf("100 \t\t\t\t\t %f Microseconds\n", diff_t);
    writeList(list7, "i", 100);

    start_t = clock();
    insertionSort(list8,1000);
    end_t = clock();
    diff_t  = (double)(end_t - start_t)*1000000/ CLOCKS_PER_SEC ;
    printf("1000 \t\t\t\t\t %f Microseconds\n", diff_t);
    writeList(list8, "i", 1000);


    start_t = clock();
    insertionSort(list9,10000);
    end_t = clock();
    diff_t  = (double)(end_t - start_t)*1000000/ CLOCKS_PER_SEC ;
    printf("10000 \t\t\t\t\t %f Microseconds\n", diff_t);
    writeList(list9, "i", 10000);


    start_t = clock();
    insertionSort(list10,100000);
    end_t = clock();
    diff_t  = (double)(end_t - start_t)*1000000/ CLOCKS_PER_SEC ;
    printf("100000 \t\t\t\t\t %f Microseconds\n\n", diff_t);
    writeList(list10, "i", 100000);

//-----------------------------------------------------------------------------------------
    printf("SelectionSort");
    printf("Input size (N): (# of numbers) \t Time cost:\n");
    start_t = clock();
    SelectionSort(list11,10);
    end_t = clock();
    diff_t  = (double)(end_t - start_t)*1000000/ CLOCKS_PER_SEC ;
    printf("10 \t\t\t\t\t %f Microseconds\n", diff_t);
    writeList(list11, "s", 10);

    start_t = clock();
    SelectionSort(list12,100);
    end_t = clock();
    diff_t  = (double)(end_t - start_t)*1000000/ CLOCKS_PER_SEC ;
    printf("100 \t\t\t\t\t %f Microseconds\n", diff_t);
    writeList(list12, "s", 100);

    start_t = clock();
    SelectionSort(list13,1000);
    end_t = clock();
    diff_t  = (double)(end_t - start_t)*1000000/ CLOCKS_PER_SEC ;
    printf("1000 \t\t\t\t\t %f Microseconds\n", diff_t);
    writeList(list13, "s", 1000);

    start_t = clock();
    SelectionSort(list14,10000);
    end_t = clock();
    diff_t  = (double)(end_t - start_t)*1000000/ CLOCKS_PER_SEC ;
    printf("10000 \t\t\t\t\t %f Microseconds\n", diff_t);
    writeList(list14, "s", 10000);

    start_t = clock();
    SelectionSort(list15,100000);
    end_t = clock();
    diff_t  = (double)(end_t - start_t)*1000000/ CLOCKS_PER_SEC ;
    printf("100000 \t\t\t\t\t %f Microseconds\n", diff_t);
    writeList(list15, "s", 100000);

    char ans[1] ; 
    int rets ;
    printf("Do you want to delete the generated files?\n");
    scanf("%s", ans);

    
      std::remove("/home/js/file.txt");

    if (strcmp(ans, "y") == 0 || strcmp(ans, "Y") == 0){
      rets = remove("C/SelectionSort_C_10.txt");
      rets = remove("C/SelectionSort_C_100.txt");
      rets = remove("C/SelectionSort_C_1000.txt");
      rets = remove("C/SelectionSort_C_10000.txt");
      rets = remove("C/SelectionSort_C_100000.txt");
      rets = remove("C/InsertionSort_C_10.txt");
      rets = remove("C/InsertionSort_C_100.txt");
      rets = remove("C/InsertionSort_C_1000.txt");
      rets = remove("C/InsertionSort_C_10000.txt");
      rets = remove("C/InsertionSort_C_100000.txt");
      rets = remove("C/MergeSort_C_10.txt");
      rets = remove("C/MergeSort_C_100.txt");
      rets = remove("C/MergeSort_C_1000.txt");
      rets = remove("C/MergeSort_C_10000.txt");
      rets = remove("C/MergeSort_C_100000.txt");

    }



}
