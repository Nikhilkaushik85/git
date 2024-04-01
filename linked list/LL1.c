// singly linked list
#include<stdio.h>
#include<stdlib.h>
void main()
{
    struct node;
    {
        int data;
        struct node*next;
    };
    struct node*newnode,*head,*temp;
    
    head=0;
    int choice=1;
    while(choice==1){
        newnode=(struct node*)malloc(sizeof(struct node));
        printf("enter the data");
        scanf("%d",&newnode->data);
        if(head==0){
            head=temp=newnode;
        }
        else{
            temp->next=newnode;
            temp=newnode;
        }
        printf("enter the choice if continue press 1 otherbise 0");
        scanf("%d",&choice);
    }
}








