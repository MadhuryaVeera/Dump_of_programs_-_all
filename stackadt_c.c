#include <stdio.h>
int stack[100],top=-1,size;
void push(int element){
	if(top==size-1)
	{
		printf("Stack is full .Insertions are not posibble\n");
	}
	else
	{
		top++;
		stack[top]=element;//top will be 0
		printf("%d is the insertion into stack\n",element);
	}
}
int pop(){
	if(top==-1){
		return -1;
	}
	else
	{
		int rm=stack[top];//rm= removed element
		top--;
		return rm;
	}
	void peek()
	{
		if(top==-1)
		{
			printf("Stack is empty\n");
		}
		else
		{
		  printf("Element in the top %d\n",stack[top]);	
		}
	}
	void display()
	{
		if(top==-1)
		{
			printf("Stack is the empty. No elements to display \n");
		}
		else
		{
			printf("Elementsin the stAack are\n");
			int i;
			for(i=top;i>=0;i--){
				printf("%d",stack[i]);
			}
			printf("\n");
		}
	}
}
int main() {
	printf("Enter size of the stack:");
	scanf("%d",&size);
	//menu driven program 
	int choice;
	while(1){
		printf(" Enter 1.Push 2. Pop 3. Peek 4. Display and any other to exit: ");
	scanf("%d",&choice);
	if(choice==1){
		//push() operation
		int ele;
		printf("Enter an element to pushed into the stack:");
		scanf("%d",ele);
		push(ele);
	}
	else if(choice==2){
		//pop()operataion
		int removed_element=pop();
		if(removed_element ==-1)
		{
			printf("Stack is empty .Cannot delete the element\n");
		}
		else
		{
			printf("Removed element is: %d\n",removed_element);
		}
	}
	else if(choice==3){
		//peek()operataion
		peek();
	}
	else if(choice==4){
		//display()operataion
		display();
	}
	else
	   {
		printf("by");
		break;
	   }
	}
}
