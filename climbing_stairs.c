#include <stdio.h>

// Function to calculate the number of ways to climb the staircase
int climbStairs(int n) {
    if (n == 1) return 1;
    if (n == 2) return 2;
    
    int first = 1, second = 2, result = 0;
    
    for (int i = 3; i <= n; i++) {
        result = first + second;
        first = second;
        second = result;
    }
    
    return second;
}

int main() {
    int n;

    printf("Enter the number of steps: ");
    scanf("%d", &n);

    int result = climbStairs(n);
    printf("Number of distinct ways to reach the top: %d\n", result);

    return 0;
}
