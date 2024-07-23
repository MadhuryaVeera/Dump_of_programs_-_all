#include<stdio.h>
int div(int a,int b)
{

	if(a%b==0)
	{
		return 0;
	}
	else
	{
		return 1;
	}
}
int main()
{
	int a,b;
	scanf("%d%d",&a,&b);
	int x=div(a,b);
	if(x==0)
	printf("0");
	else
	printf("1");
	
}
