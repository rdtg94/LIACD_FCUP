#include <stdio.h>

int main()
{
	int n;
	int i;
	int j;

	scanf("%d", &n);

	if (n < 1 || n > 20)
		return (1);

	i = 0;
	while (i < n)
	{
		j = 0;
		while (j < n)
		{
			if ((i + j) % 2 == 0)
				printf("#");
			
			else
				printf("_");
			
			j++;
		}
		printf("\n");
		i++;
	}
	return (0);
}