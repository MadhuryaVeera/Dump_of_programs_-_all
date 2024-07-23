#include<stdio.h>
#include<string.h>
int main()
{
	int n,i;
	scanf("%d",&n);
	int a[n];//declaraion
	for(i=0;i<n;i++)
	{
		scanf("%d",&a[i]);
		
	}
	for(i=0;i<n;i++)
	{
		printf("%d------------->%d\n",&a[i],a[i]);
		
	}
}
