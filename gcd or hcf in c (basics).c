#include<stdio.h>
int main()
{
    int p,q,i,gcd;
    scanf("%d%d",&p,&q);
    for(i=1;i<=p&&i<=q;i++)
    {
        if(p%i==0&&q%i==0)
        gcd=i;
        
    }
    printf("%d",gcd);
}
