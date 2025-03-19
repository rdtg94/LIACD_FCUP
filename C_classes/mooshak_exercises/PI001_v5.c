#include <stdio.h>

int main(void)
{
    int n;
    int i;
    int sum;

    sum = 0;

    scanf("%d", &n);

    i = 0;
    while (i <= n)
    {
        if (i % 2 == 0)
        {
            sum += i;
        }
        i++;
    }

    printf("%d\n", sum);
    return 0;
}