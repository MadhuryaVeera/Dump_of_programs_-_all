#include<stdio.h>
int main()
{
	struct student
	{
        int rollno; 
        char name[20];
        float per;                
        }std={1,"aditya",98};
         printf("%d\n%s\n%f",std.rollno,std.name,std.per);
    
}
