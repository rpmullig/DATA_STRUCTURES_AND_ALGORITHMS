For the fixes, I simply combined the nested if statements with and's. Then I added a recusive step, but only for the new_elements added to the list, and checks them for all directions. This will recure to only allow new_elements to be checked again and again. 

The time complexity is O(n^2)  because it will continue to loop through and check in each direction until there are no more colored spaced on the borders with the same color. The recursive call and redoing the whole list again once new elements are added causes this algorithm to take so much time. 






