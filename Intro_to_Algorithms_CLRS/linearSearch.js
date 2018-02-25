/* Linear Search from Intro to Algorithms */ 
/*
Author: Robert P Mulligan
Created: 2/23/2018
RAM Computational Model:
	-n is the number of integers in the array
	-O(n) 
*/ 


var a = [4, 1, 2, 20, 2300, 300, 324, 20];

function linearSearch(value, array) {
 for(var i = 0; i < array.length; i++){
   // soft equals to array object
   if(a[i] == value) {return i;}
 }
  return -1; 
}

linearSearch(4, a); // 0
linearSearch(300, a); // 5
linearSearch(20, a); // 3
linearSearch(2039, a); // -1
