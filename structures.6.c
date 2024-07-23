#include<stdio.h>
struct student 
   {
   	int rollno;//4 bytes
   	char name[20];//20 bytes
   	float per;//8 bytes
   };
   int main()
   {
   
   	struct student std,*ptr;
   	int n,i;
   	ptr=&std;
   	          scanf("%d%s%f",&ptr->rollno,&ptr->name,&ptr->per);
   	          printf("%d %s %f",ptr->rollno,ptr->name,ptr->per);
   	      }
