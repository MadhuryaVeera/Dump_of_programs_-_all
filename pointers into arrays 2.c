#include<stdio.h>
#include<string.h>
int main()
{
	int n,i;
	scanf("%d",&n);
	int a[n];//declaraion
	printf("%d\n",&a);
	for(i=0;i<n;i++)//reading array
	{
		scanf("%d",&a[i]);
		
	}
	for(i=0;i<n;i++)//printfing the array
	{
		printf("%d------------->%d\n",ptr+i,*(ptr+i));
