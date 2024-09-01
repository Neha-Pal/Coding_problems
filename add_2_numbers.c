// C Program to add two number represented as
// linked list by creating a new list

#include <stdio.h>
#include<stdlib.h>

struct Node {
    int data;
    struct Node *next;
};

struct Node *createNode(int val);

struct Node *reverse(struct Node *head) {
    struct Node *prev = NULL, *curr = head, *next;

    while (curr != NULL) {
        next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }
    return prev;
}


struct Node *addTwoLists(struct Node *num1, struct Node *num2) {
    struct Node *res = NULL, *curr = NULL;
    int carry = 0;

    num1 = reverse(num1);
    num2 = reverse(num2);

    while (num1 != NULL || num2 != NULL || carry != 0) {
        int sum = carry;

        if (num1 != NULL) {
            sum += num1->data;
            num1 = num1->next;
        }
        if (num2 != NULL) {
            sum += num2->data;
            num2 = num2->next;
        }

        struct Node* newNode = createNode(sum % 10);
        carry = sum / 10;
        if (res == NULL) {
            res = newNode;
            curr = newNode;
        } 
          else {
            curr->next = newNode;
            curr = curr->next;
        }
    }
    return reverse(res);
}

void printList(struct Node *head) {
    struct Node *curr = head;
    while (curr != NULL) {
        printf("%d ", curr->data);
        curr = curr->next;
    }
    printf("\n");
}

struct Node *createNode(int val) {
    struct Node *node = 
              (struct Node *)malloc(sizeof(struct Node));
    node->data = val;
    node->next = NULL;
    return node;
}

int main() {

    struct Node *num1 = createNode(1);
    num1->next = createNode(2);
    num1->next->next = createNode(3);

    struct Node *num2 = createNode(9);
    num2->next = createNode(9);
    num2->next->next = createNode(9);

    struct Node *sum = addTwoLists(num1, num2);
    printList(sum);

    return 0;
}
