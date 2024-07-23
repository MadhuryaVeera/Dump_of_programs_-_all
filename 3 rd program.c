#include<stdio.h>
void al(int a,int b)
{
	int i;
	for(i=a;i<=b;i++)
	{
		printf("%d",i);
	}
}
int main()
{
	int a,b;
	scanf("%d%d",&a,&b);
	al(a,b);
}
