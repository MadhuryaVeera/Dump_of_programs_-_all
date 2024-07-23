#include<stdio.h>
#include<string.h>
int main()
{
	char str[100];
	scanf("%[^\n]s",&str);
	int i,vc=0,cc=0;
	for(i=0;str[i]!='\0';i++)
	{
		if(str[i]=='a'||str[i]=='e'||str[i]=='i'||str[i]=='o'||str[i]=='u')
		{
			vc++;
		}
		else
		{
			cc++;
		}
	}
	printf("%d %d",vc,cc);
}
