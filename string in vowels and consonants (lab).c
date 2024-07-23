#include<stdio.h>
#include<string.h>
int main()
{
	char str[100],*ch;
	int i,v=0,c=0;
printf("\n enter the string");

	scanf("%s",&str);
	ch=str;
	while(*ch!='\0')
	{
		if(*ch=='a'||*ch=='e'||*ch=='i'||*ch=='o'||*ch=='u'||*ch=='A'||*ch=='E'||*ch=='I'||*ch=='O'||*ch=='U')
        {
        	v++;
		}
		else
		{
			c++;
		}
		ch++;
	}
	printf("\n no of vowels is =%d\n no of consonants is =%d",v,c);
	
}
