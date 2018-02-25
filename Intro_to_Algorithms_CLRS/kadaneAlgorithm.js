
var arr = [ 1, 3, 4, -6, 11, -10, 100, -1, -2, -3, 104, 100, -100]; 

function kadane(a){
  var max_current = a[0], max_global = a[0];
  for(var i = 1; i < a.length; i++) {
    max_current = Math.max(a[i], max_current + a[i]); 
    max_global = Math.max(max_current, max_global); 
    }
  return max_global; 
}

kadane(arr); 
