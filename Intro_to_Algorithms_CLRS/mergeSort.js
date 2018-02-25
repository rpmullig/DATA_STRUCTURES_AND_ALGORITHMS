/* Merge sort from Intro to Algorithms */ 
/*
Author: Robert P Mulligan
Created: 2/24/2018

RAM Computational Model:
    -n is count of integers in the array
    -O(n*log(n))
    
Divide-and-conquer algorithm that
splits up the array and sorts the smaller
bits through combining them back together
*/

// basic helper function FIND OUT WHAT THE PARAMETERS ARE!
function merge(arr, p, q, r) {
  
  var  i, j, k; // incrementors
  
  var n_one = q - p + 1; 
  var n_two = r - q; 
  var L = new Array(n_one + 1);
  var R = new Array(n_two + 1 )
  
  for(i = 0; i < n_one - 1; i++){
   L[i] = arr[p + i]; 
  }
  for(j = 0; j < n_two - 1; j++){
   R[j] = arr[q + j]; 
  }
  
  /* Infinity will mark the ending 
    sentinel variable for knowing it's the end
  */ 
  L[n_one] = INFINITY; 
  R[n_two] = INFINITY; 
  i = 1;
  j = 1; 
  
  for(k = p; k < r; k++){
   L[i] <= R[j] ? {arr[k] = L[i]; i++;} : {arr[k] = R[j]; j++;} 
  }
}
