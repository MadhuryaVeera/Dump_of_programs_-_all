#include<stdio.h>
struct student 
   {
   	int rollno;//4 bytes
   	char name[20];//20 bytes
   	float per;//8 bytes
   };
   int main()
   {
   	struct student std,std1;
   	scanf("%d\n%s\n%f",&std.rollno,&std.name,&std.per);
   	scanf("%d\n%s\n%f",&std1.rollno,&std1.name,&std1.per);
   	scanf("%d\n%s\n%f",std.rollno,std.name,std.per);
   	scanf("%d\n%s\n%f",std1.rollno,std1.name,std1.per);
   }
