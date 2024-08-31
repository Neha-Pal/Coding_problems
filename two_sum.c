#include<stdio.h>
#include<stdbool.h>

bool twoSum(int arr[],int n,int target){
    for(int i = 0 ; i<n ; i++){
        for(int j = i+1; j<n ; j++){
            if(arr[i] + arr[j] == target){
                return true;
            }
        }
    }
    return false;
}

int main(){
    int arr[] = {2,1,6,5,3};
    int target = 4;
    int n = sizeof(arr)/sizeof(arr[0]);
    
    printf("%d\n",twoSum(arr,n,target));
    return 0;
}
