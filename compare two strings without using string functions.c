#include<stdio.h>
int main()
{
	char str1[100],str2[100];
	int i,len1,len2,s=1;
	printf("Enter the string1:");
	scanf("%[^\n]s",&str1);
	printf("Enter the string2:");
	scanf("%[^\n]s",&str2);
	for(i=0;str1[i]!='\0';i++)
	len1=i;
	for(i=0;str2[i]!='\0';i++)
	len2=i;
	if(len1==len2)
	{
	for(i=0;i<len1;i++)
	if(str1[i]!=str2[i])
     	{
		s=0;
		break;
	    }
	if(s==0)
	    
		printf("strings are not equal");
	    
	else
	    
		printf("strings are equal");
    }
	 else
	 {
	 	printf("strings are not equal");
	 }
}

	

