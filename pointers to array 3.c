#include<stdio.h>
#include<string.h>
int main()
{
	int n,i; 
	scanf("%d",&n);
	int a[n];//array declaration 
	int *ptr;
	ptr=&a;
	printf("%d\n",ptr);
	for(i=0;i<n;i++)//reading array
	{
		scanf("%d",ptr+i);
	}
	for(i=0;i<n;i++)//printing the array 
	{
		printf("%d--------->%d\n",ptr+i,*(ptr+i));
	}
}
