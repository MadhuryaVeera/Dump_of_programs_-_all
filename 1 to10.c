#include<stdio.h>
#include<math.h>
int main()
{
	int n,r,q,s=0,d;
	scanf("%d",&n);
	while(n!=0)
	d=log10(n);
	q=n;
	{
		r=q%10;
		q=q/10;
		s=s+pow(r,d);
	}
	if(n==s)
	{
		printf("amstrong");
	}
	else
	{
		printf("not amstrong");
	}
   
}

