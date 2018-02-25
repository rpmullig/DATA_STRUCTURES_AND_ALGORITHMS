/* Selection sort from Intro to Algorithms */ 
/*
Author: Robert P Mulligan
Created: 2/24/2018

RAM Computational Model:
    -n is the numbers in the array
    -O(n^2)
    -space complexity O(n)
*/

var a = [ 5, 2, 4, 6, 1, 3, -100, -5, 156056406, 5]; 

function selectionSort(a){
  var new_array = [], temp = 0, helper = []; 
    
  /* javascript will only make a pointer to
     the a array object--destructively mutating
     it--so I much create a new one */
  a.forEach(function(item) {
    new_array.push(item)
  });
  
  // find the smallest value and its location  
  function linearSearchMin(a, loc){
    var min = a[loc], index = loc;
    
    for(var i = index; i < new_array.length; i++) {
      if(new_array[i] < min) {min = new_array[i]; index = i;} 
    }  
    return [min, index]; 
  }
  
  for(var x = 1; x < new_array.length; x++) {
      helper = linearSearchMin(new_array, x-1); // [min, index]
      // swap 
      temp = new_array[x-1];
      new_array[x-1] = helper[0];
      new_array[helper[1]] = temp;
  }

  return new_array;
}
  
  
var sorted_a = selectionSort(a); 

function printArray(a){
 for(var x = 0; x < a.length; x++){
    Console.log(a[x]);
 }
}
  
