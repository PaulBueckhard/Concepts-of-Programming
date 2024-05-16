#include <stdio.h>
#include <stdlib.h>

int main() {
    // Allocate memory for an array of 10 integers
    int *arr = (int*)malloc(10 * sizeof(int));

    // Check if memory allocation was successful
    if (arr == NULL) {
        printf("Memory allocation failed\n");
        return 1;
    }

    // Use the allocated memory
    for (int i = 0; i < 10; i++) {
        arr[i] = i * i;
        printf("%d ", arr[i]);
    }
    printf("\n");

    // Free the allocated memory to prevent memory leaks
    free(arr);

    return 0;
}
