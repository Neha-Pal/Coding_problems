#include <stdio.h>

int reverse(int num){
    int rev_num = 0;
    while(num>0){
        rev_num = rev_num*10 + num % 10;
        num = num /10;
    }
    return rev_num;
}

int isPalindrome(int num, int rev_num){
    reverse(num);
    if(num == rev_num){
        return 1;
    }
    else{
        return 0;
    }
}

int main(){
    int num = 231;
    int rev_num = 0;
    if(isPalindrome(num, rev_num)){
        printf("%d is palindrome",num);
    }
    else{
        printf("%d is not palindrome",num);
    }
    
}