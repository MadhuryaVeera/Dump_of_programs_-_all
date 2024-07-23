#include<stdio.h>
#include<string.h>
int main()
{
	int a,b,c;
	scanf("%d%d%d",&a,&b,&c);
	int *ptr1,*ptr2,*ptr3;
	ptr1=&a;
	ptr2=&b;
	ptr3=&c;
	if(*ptr1>*ptr2&&*ptr1>*ptr3)
	{
		printf("%d bigger",*ptr1);
	}
		else if(*ptr2>*ptr1&&*ptr2>*ptr3)
	{
		printf("%d bigger",*ptr2);
	}	
	else
	{
		printf("%d bigger",*ptr3);
	}
}
