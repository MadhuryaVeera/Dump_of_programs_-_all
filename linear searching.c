#include<stdio.h>
int main()
{
	int n,key,i,c=0;
	int a[n];
	scanf("%d%d",&n,&key);
    for(i=0;i<n;i++)
      {
      	scanf("%d",&a[i]);
	  }
	  for(i=0;i<n;i++)
	  {
	  	if(key==a[i])
	  	{
	  		c++;
	  		break;
		  }
	  }
	  if(c!=0)
	  	printf("found");
	  else
	  	printf("not found");
	
}
