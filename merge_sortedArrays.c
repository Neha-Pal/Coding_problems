#include <stdio.h>


void printArr(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        printf("%d\t", arr[i]);
    }
    printf("\n");
}

void merge(int arr_1[], int arr_2[], int arr_3[], int n_1, int n_2) {
    int i = 0, j = 0, k = 0;

    while (i < n_1 && j < n_2) {
        if (arr_1[i] < arr_2[j]) {
            arr_3[k++] = arr_1[i++];
        } else {
            arr_3[k++] = arr_2[j++];
        }
    }

    while (i < n_1) {
        arr_3[k++] = arr_1[i++];
    }

    while (j < n_2) {
        arr_3[k++] = arr_2[j++];
    }
}

int main() {
    int arr_1[] = {1, 3, 5, 7};
    int arr_2[] = {2, 6, 8, 9};
    int n_1 = sizeof(arr_1) / sizeof(arr_1[0]);
    int n_2 = sizeof(arr_2) / sizeof(arr_2[0]);
    int arr_3[n_1 + n_2]; 

    merge(arr_1, arr_2, arr_3, n_1, n_2);

    
    printf("Merged array: \n");
    printArr(arr_3, n_1 + n_2);

    return 0;
}
