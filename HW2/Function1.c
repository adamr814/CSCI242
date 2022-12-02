#include <stdio.h>
#include <stdlib.h>

void function(int (n=1))
{
    int count = 0;
    for (int i = n/2; i <= n; i++)
        for (int j = 1; j <= n; j = 2*j)
            for (int k = 1; k<=n; k = k * 2)
                count++;
    printf("%d", count);
    return 0;
}