#include<stdio.h>
int main()
{  
      int x;
      scanf("%d",&x);
      for(int j=1;j<=x;j++)
	{
			int n;
		scanf("%d",&n);
		int rev=0,t=n;
		while(n!=0)
		{
			rev=rev*10+n%10;
			n=n/10;
		}
		if(t==rev) 
		printf("Yes\n");
		else
		printf("No\n");
   }    
}
