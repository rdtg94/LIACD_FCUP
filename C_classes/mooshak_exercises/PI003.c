#include <stdio.h>

int main() {
    int n, i, j;

    n = 0;
    i = 0;
    j = 0;

    scanf("%d", &n);

    if (n < 1 || n > 20)
        return 1;

    for (i = 0; i < n; i++) {
        for (j = 0; j < n - i - 1; j++) {
            printf("_");
        }
        for (j = 0; j <= i; j++) {
            printf("#");
        }
        printf("\n");
    }
    return 0;
}
