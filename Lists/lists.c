/* 
** Author: Robert Mulligan
** Date Created: 10/13/2014
** Last Modified by: Robert Mulligan
** Date Last Modified: 10/13/2014
*/

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>


   //function prototypes
int demo_function();
void DisplayStats ();


//a struct, person, with fields of preselected datatypes
struct person {
  //fields with given data types
  char first[40];
  char last[40];
  int year;
  double ppg;
}; //end of struct


//start of main
int main(void)

{
  // calls external functions
  demo_function();
  linked();

  return (0);
}


int demo_function()
{
    //an array of people in class of 7 elements
  struct person class[10];

// people struct assigning values
  strcpy(class[0].first,"Jane"); // inputs the string into the array "first"
  strcpy(class[0].last,"Doe");
  class[0].year=2004; // assigns the value to year field
  class[0].ppg=5.2;

  strcpy(class[1].first,"Brian");
  strcpy(class[1].last,"Smith");
  class[1].year=2005;
  class[1].ppg=4.9;

  class[2].year=2004;
  class[2].ppg=12.3;
  strcpy(class[2].first,"Rip");
  strcpy(class[2].last,"Caryle");


  class[3].year=2004;
  class[3].ppg=11;
  strcpy(class[3].first,"Rex");
  strcpy(class[3].last,"Cutshall");

  class[4].year=2004;
  class[4].ppg=9.3;
  strcpy(class[4].first,"Robbie");
  strcpy(class[4].last,"Reynalds");

  class[5].year=2004;
  class[5].ppg=4.2;
  strcpy(class[5].first,"Carolyn");
  strcpy(class[5].last,"Geirner");

  class[6].year=2004;
  class[6].ppg=6.9;
  strcpy(class[6].first,"Greg");
  strcpy(class[6].last,"Kitzmiller");

  class[7].year=2004;
  class[7].ppg=5;
  strcpy(class[7].first,"John");
  strcpy(class[7].last,"McGuire");

//a loop to send each person structure to displayStats
  int i;
  for(i = 0; i < 8; i++) {
        DisplayStats(class[i]);
    }//end of for loop
}//end of main


void DisplayStats (struct person people)
{
    //declaring an int for the for loop
    int i;

// the for loop will go through until it finds the end of the last field array
    for(i = 0; people.last[i] != '\0'; i++){
        printf("%c",people.last[i]);
    }
    printf(", ");
// the for loop will go through until it finds the end of the first field array
    for(i = 0; people.first[i] != '\0'; i++){
        printf("%c",people.first[i]);
    }

   printf(":    ");
   //calls the values for parameter structure and finds the fields given for printing
   printf("%2f PPG in %d",people.ppg, people.year);

    printf("\n");
}


 //Basic linked list with a node and a pointer to next
struct NODE {
  int number;
  struct NODE *next;
};

// Prototypes for list functions
void append_node(struct NODE *llist, int num);
void delete_node(struct NODE *llist, int num);
int search_value(struct NODE *llist, int num);
void display_list(struct NODE *llist);

//external function
int linked(void) {

  int num = 0;
  int input = 1;
  int retval = 0;
  struct NODE *llist;

//'->' works like a pointer dereference but with structures
  llist = (struct NODE *)malloc(sizeof(struct NODE));
  llist->number = 0;
  llist->next = NULL;


//user menu to modify the lists
  while(input != 0) {

//a print for the user
    printf("\n-- Menu Selection --\n");
    printf("0) Quit\n");
    printf("1) Insert\n");
    printf("2) Delete\n");
    printf("3) Search\n");
    printf("4) Display\n");
    //input value from user
    scanf("%d", &input);

//goes through option from input and calls function
    switch(input) {

         //exits the menu and will stop the while loop
       case 0:
         printf("Goodbye ...\n");
         input = 0;
         break;

         //inserts a value by creating an ode at the end
       case 1:
         printf("Your choice: 'Insertion'\n");
         printf("Enter the value which should be inserted: ");
         scanf("%d", &num);
         append_node(llist, num);
         break;

       //removes the value
       case 2:
      printf("Your choice: 'Deletion'\n");
      printf("Enter the value which should be deleted: ");
      scanf("%d", &num);
      if((retval = search_value(llist, num)) == -1)
	printf("Value '%d' not found\n", num);
      else
	delete_node(llist, num);
      break;

      // returns the position of the value
       case 3:
      printf("Your choice: 'Search'\n");
      printf("Enter the value you want to find: ");
      scanf("%d", &num);
      if((retval = search_value(llist, num)) == -1)
	printf("Value '%d' not found\n", num);
      else
	printf("Value '%d' located at position '%d'\n", num, retval);
      break;

      // shows the list values
    case 4:
      printf("You choice: 'Display'\n");
      display_list(llist); break;
      /*Catch all unmanaged input and return to menu */
    default:
      printf("That is not a valid menu option\n");
      break;
    } /*end of switch-case */

  } /*end of while loop */

  free(llist); //frees up malloc..
  return(0);

} // End of Linked function


//adds a value by appending the node
void append_node(struct NODE *llist, int num) {
  while(llist->next != NULL)
    llist = llist->next;
  llist->next = (struct NODE *)malloc(sizeof(struct NODE));
  llist->next->number = num;
  llist->next->next = NULL;
}


//removes a node. We add a temp to store the pointer
void delete_node(struct NODE *llist, int num) {

  struct NODE *temp;
  temp = (struct NODE *)malloc(sizeof(struct NODE));

  if(llist->number == num) {
    /* remove the node */
    temp = llist->next;
    free(llist); /*FREE UP THAT MEMORY!! */
    llist = temp;
  } else {

    while(llist->next->number != num)
      llist = llist->next;
    temp = llist->next->next;
    free(llist->next); /*FREE UP THAT MEMORY!! */
    llist->next = temp;
  }

}//end of delete_node

//searches for a node by starting and going through the list
int search_value(struct NODE *llist, int num) {
  int retval = -1;
  int i = 1;
  while(llist->next != NULL) {
    if(llist->next->number == num)
      return i;
    else
      i++;
    llist = llist->next;
  }
  return retval;
}

//goes through and prints the elements of the list
void display_list(struct NODE *llist) {
  while(llist->next != NULL) {
    printf("%d ", llist->number);
    llist = llist->next;
  }
  printf("%d", llist->number);
}
