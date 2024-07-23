#include<stdio.h>
struct student 
   {
   	int rollno;//4 bytes
   	char name[20];//20 bytes
   	float per;//8 bytes
   };
   int main()
   {
   	struct student std[10];
   	int n,i;
   	scanf("%d",&n);
   	for(i=0;i<n;i++)
   	{
   		scanf("%d%s%f",&std[i].rollno,&std[i].name,&std[i].per);
	   }
	   for(i=0;i<n;i++)
	   {
	   	printf("%d\n%s\n%f",std[i].rollno,std[i].name,std[i].per);
	   }
   }
