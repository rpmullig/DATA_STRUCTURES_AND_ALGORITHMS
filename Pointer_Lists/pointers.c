/* pointers.c
**
** Author: Robert Mulligan
** Date Created: 10/01/2014
** Last Modified by: Robert Mulligan
** Date Last Modified: 10/03/2014
*/

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

//Calls the functions
int main() {

//Calling of the functions
printf("\n ===== Start of bitmodels =====\n\n");
bitmodels();
printf("\n ===== End of bitmodels =====\n\n\n ");

printf("\n ===== Start of pointers =====\n\n");
pointers();
printf("\n ===== End of pointers =====\n\n");

printf("\n ===== Start of morePointers =====\n\n");
morePointers();
printf("\n ===== End of morePointers =====\n\n");

printf("\n ===== Start of pointerfunction =====\n\n");
pointerfunction();
printf("\n ===== End of pointerfunction =====\n\n");

printf("\n ===== Start of pointerarithmetic =====\n\n");
pointerarithmetic();
printf("\n ===== End of pointerarithmetic =====\n\n");

printf("\n ===== Start of pointerarray =====\n\n");
pointerarray();
printf("\n ===== End of pointerarray =====\n\n");

return(0);
}

int bitmodels(void) {

//declaring variables
 unsigned char a;
 unsigned char b,c;
 unsigned char d,e;
 char f;
 int i;

//bit operations - flip sign
a=17;
a=~a;

//print of the operations
printf("bitwise NOT of 17\n");
printf("%d\n",a);



//bit AND
b=17;
c=22;
b=b & c;


printf("bitwise AND of 17 and 22\n");
printf("%d\n",b);


//Bitwise OR
d=17;
e=22;
d=d | e;

printf("bitwise OR of 17 and 22\n");
printf("%d\n",d);



f=17;
//bit #3 in f's memory address is flipped to 1
f=f | (1 << 3); /* set bit #3 */

printf("Sets bit #3 in 17, new value is 17+8=25\n");
printf("%d\n",f);


//bit operation combining, flip, and changing bit 4 to 1
f=f & (~(1<<4)); /* clear bit #4 */
printf("Clears bit #4 in 25, new value is 25-16=9\n");
printf("%d\n",f);


printf("Reads i-th bit in current value of f (which is the base10 number 9),\nplus a loop that prints every bit in 8-bit space\n");


// goes through the loop and changes bits
for (i=7; i>=0; i--)
 printf("%d ",(f&(1<<i)) >> i); /* read i'th bit */


printf("\n");
printf("Current value of a\n");


for (i=7; i>=0; i--)
 printf("%d ",(a&(1<<i)) >> i); /* read i'th bit */


printf("\n");
printf("Current value of d\n");



for (i=7; i>=0; i--)
 printf("%d ",(d&(1<<i)) >> i); /* read i'th bit */

printf("\n");


printf("Current value of e\n");


for (i=7; i>=0; i--)
 printf("%d ",(e&(1<<i)) >> i); /* read i'th bit */

printf("\n");

return(0);

}


int pointers(void) {

/*Declaring some variables of different types */

 int count, x;
 int *count_p;
 char letter;
 char *letter_p = &letter;


/*Assigning specific values to the declared variables */
 count=10;
 count_p=&count;
 x=*count_p;
 letter = 'Q';


 //Let's print the contents of count and x

printf("Here's is the step-by-step output from the integer pointer example\n");

 //Let's confirm the values of count and x

 printf("count = %i and x = %i\n", count, x);

 //Changes count using the pointer count_p

 *count_p = 42;


 printf("count = %i and x = %i\n", count, x);


 //Let's change count to the value of x

 count = x;

 //Let's print the contents of count and x again

 printf("count = %i and x = %i\n", count, x);
 printf("Here's is the step-by-step output from the character pointer example\n");

 //Let's confirm the values of letter and letter_p

 printf("letter = %c and letter_p = %c\n", letter, *letter_p);

 //Let's change letter but not letter_

 letter = '/';

 //Let's print the contents of letter and letter_p again

 printf("letter = %c and letter_p = %c\n", letter, *letter_p);

 //Let's change letter_p but not letter

 *letter_p = '!';

 //prints again

 printf("letter = %c and letter_p = %c\n", letter, *letter_p);

return(0);

}


int morePointers(void) {

//declares variables, int's and pointers of ints

 int firsti, secondi;
 int *firsti_p, *secondi_p;

//assigns values to one another

 firsti=5;
 firsti_p=&firsti;
 secondi = *firsti_p / 2 + 10;
 secondi_p = firsti_p;

 //prints out the results

 printf("Here the output from the first integer pointer example\n");

 // prints the values out

printf("firsti = %i, secondi = %i, value of firsti_p = %i and value of secondi_p =%i\n", firsti, secondi, *firsti_p, *secondi_p);


return(0);

}

//declaring a function
int division(int numerator, int denominator, int *dividend, int *remainder);

int pointerfunction(void){

 // variables for the division functions
int x,y,d,r;

 x=9;
 y=2;

 printf("address of d: %u\n",&d);
 // address where dividend in function should \ point

 printf("address of r: %u\n",&r);
 // address where remainder in function should\ point

// calls data to the function
 division(x,y,&d,&r);
 printf("%d/%d = %d with %d remainder\n",x,y,d,r);
 printf("x=%d\n",x);

 return(0);
}

//This is the division function, with 2 int variables and 2 int pointer variables

int division(int numerator, int denominator, int *dividend, int *remainder)
{
 printf("address stored in dividend: %u\n",dividend);
 printf("address stored in remainder: %u\n",remainder);

 if (denominator < 1)
    return(0);
//performing operations
 *dividend=numerator/denominator;
 *remainder=numerator%denominator;

 numerator=7;
}


int pointerarithmetic(void){

//Declaring variables and pointers

 char ca[3],*cp;
 int ia[3],*ip;

//assigning values

 ca[0]='A';
 ca[1]='B';
 ca[2]='c';
 cp=&(ca[0]);


 ia[0]=1234;
 ia[1]=5678;
 ia[2]=9999;
 ip=&(ia[0]);


//Show output, then use pointers, then show output again.

 printf("char pointer cp points to value = %c\n",*cp);
 printf("ca[2] = %c\n", ca[2]);
 printf("int pointer ip points to value = %i\n", *ip);
 printf("ia[2] = %i\n",ia[2]);

 *(cp+2) = 'Q';
 *(ip+2) = 33;


 printf("Results after we apply pointer arithmetic.\n");
 printf("ca[2] = %c\n",ca[2]);
 printf("ia[2] = %i\n",ia[2]);

return(0);

}

int pointerarray (void){

 double array[10];
 double *d_ptr;
 double value;
 int i,offset;


 for (i=0; i<10; i++)

    array[i]=(double)i+10.0;
    // access memory using array index and fill cells with #s

    d_ptr=&(array[0]);
    // access memory location of first array cell using pointer


 while (1)
    {
//prints with special commands
    printf("\nAddress(hex)\tAddress(base10)\tValue\n");


    for (i=0; i<10; i++)

        printf("%p\t%u\t%lf\n",&(array[i]),&(array[i]),array[i]);
            printf("Enter offset value (0 0 to quit): ");

scanf("%d %lf",&offset,&value);
 if (offset == 0 && value == 0.0)
break; /* break out of loop */

 if (offset < 0 || offset > 9)
{

 printf("Offset out of bounds\n");

// go back to start of loop
 continue;
}


//The three different ways to perform this operation

 array[offset]=value; /* using array syntax */

// *(d_ptr+offset)=value; // using pointer syntax
//  *(array+offset)=value; // Using mixed syntax
 }

return(0);

}
