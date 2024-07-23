#include<stdio.h>
void main()
{
	int a[50][50],b[50][50],i,r,j,c;
	printf("Enter the rows and coloums of the matrix:");
	scanf("%d %d",&r,&c);
	printf("Enter the elements of the matrix:\n");
	for(i=0;i<r;i++)
	  for(j=0;j<c;j++)
	    {
	    	scanf("%d",&a[i][j]);
		}
		 printf("\nThe matrix:");
		 for(i=0;i<r;i++)
		 for(j=0;j<c;j++)
		 {
		 	printf("%d\n",a[i][j]);
		    printf("\n");
		 }
		 for(i=0;i<r;i++)
		 for(j=0;j<c;j++)
		 b[i][j]=a[i][j];
		 printf("\nThe transsposee of a matrix:");
		 for(i=0;i<r;i++)
         {
         	for(j=0;j<c;j++)
         	printf("%d\n",b[i][j]);
         	printf("\n");
		 }
		 
}
