/* Bogo Sort */ 
/*
Author: Robert P Mulligan
Created: 2/24/2018

RAM Computational Model:
    -n is the numbers in the array
    -O((n+1)!)
    -highly inefficient, used for testing purposes only

This algorithm is like shuffling cards, checking to see if
they are in order. If the cards are out of order, reshuffle
till and recheck--continue this till the elements are in order. 
*/

var a = [12, 100, 30, -10, 1, 3, 501645, -150, 564, 1, 13];

function bogoSort(a){
 
 var new_array = []; 
  a.forEach(function(item) {
    new_array.push(item)
  });
   
  function notSorted(arr){
    for(var x = 1; x < arr.length; x++) {
     if(arr[x-1] > arr[x]){return true; } 
    }
    return false; 
  }
 
 function shuffle(arr){
    var max = arr.length, random;
    for(var i = 0; i < max; i++){
    random = Math.floor(Math.random() * max); 
    swap(arr, i, random)
    }
  return arr;  
 }
 
 function swap(arr, i, x) {
    var temp = arr[i];
    arr[i] = arr[x];
    arr[x] = temp; 
    return arr; 
 }
 
 
 while(notSorted(new_array)) {
    shuffle(new_array)  
  }  
  
  return new_array;
}

bogoSort(a); 
