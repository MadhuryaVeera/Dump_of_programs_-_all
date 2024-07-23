#include<stdio.h>
int main()
{
FILE *fp=fopen("files in c.txt","r");
//returns a pointer 
//returns a null pointer if the file dolesnt exist 
if(fp==NULL)
    {
	printf("File does not exist");
     }
else 
   { 
	printf("File is opened");
    }
}

