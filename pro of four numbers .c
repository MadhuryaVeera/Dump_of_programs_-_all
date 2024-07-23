#include<stdio.h>
int four(int a,int b,int c, int d)
{
	int p,q,r;
	p=a+b;
	q=c*d;
	r=q-p;
}
int main()
{
	int a,b,c,d;
	scanf("%d%d%d%d",&a,&b,&c,&d);
	int x=four(a,b,c,d);
	printf("%d",x);
}
