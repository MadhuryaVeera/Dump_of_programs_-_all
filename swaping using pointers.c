#include<stdio.h>
void swap(int *,int *);
	int main()
	{
		int a,b;
		scanf("%d%d",&a,&b);
		swap (a,b);
		printf("a=%d b=%d",a,b);//address is different values are same
	}
void swap(int *x,int *y)
{
	int t;
	t=*x;
	*x=*y;
	*y=t;
	printf("x=%d y=%d",*x,*y);
}










