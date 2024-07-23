#include<stdio.h>
void prime(int x)

{
	int n;
	printf("\n enter the numbers");
	scanf("%d",&n);
	prime(n);
	return 0;
}
int main()
{
	int i,p=0,x;
	for(i=1;i<x;i++)
	{
		if(x%i==0)
		{
			p++;
		}
	}
	if(p==1)
	printf("\n given no is prime");
}
  
	


