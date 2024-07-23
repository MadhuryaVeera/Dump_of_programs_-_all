#include<stdio.h>
#include<string.h>
int main()
{
	char name1[20],name2[20];
	scanf("[^\n]s",&name1);
	scanf("[^\n]s",&name2);
	//gets(name1);
		//gets(name2);
	//printf("%s\n",name1);
	strcat(name1,name2);
	printf("name=%s",name1);
}
