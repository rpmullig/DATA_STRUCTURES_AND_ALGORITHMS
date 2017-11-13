My code creates a matrix of 0 then will fill in the firt row and column with increasing negative numbers 

THe matrix will score itself through utilizing the fact that the diagonal will usually be the max of the previous top left position and the gaps will be the max of the previous gapped location

Once the matrix is scored, the algorithm works back from the bottom right position. It'll compare going up, left, or diagonal and going backwards down the string add in gaps or spaced.

from bottom right to top left
left: add in a gap for s2
up: add in a gap for s1
diag: increment down 1 on both
