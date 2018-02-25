/* Insertion sort from Intro to Algorithms */ 
/*
Author: Robert P Mulligan
Created: 2/21/2018

RAM Computational Model:
	-n is the numbers in the array
	-O(n^2)
*/ 


var a = [ 5, 2, 4, 6, 1, 3 ]; 

function insertionSort(a){
  var key, i, j;

  for(j = 1; j < a.length; j++) { 
    key = a[j]; 
    // insert a[j] into the sorted sequence
    i = j - 1;
    while(i >= 0 && a[i] > key){
      a[i + 1] = a[i];
      i = i - 1;
    }    
    a[i + 1] = key; 
  }
}

insertionSort(a);
