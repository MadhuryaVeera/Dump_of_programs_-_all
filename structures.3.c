#include<stdio.h>
struct student 
   {
   	int rollno;//4 bytes
   	char name[20];//20 bytes
   	float per;//8 bytes
   };
   int main()
   {
   	struct student std;
   	scanf("%d\n%s\n%f",&std.rollno,&std.name,&std.per);
   	printf("%d\n%s\n%f",std.rollno,std.name,std.per);
   }
