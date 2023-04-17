#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int n;
    do
    {
        //Prompting user for height
        n = get_int("Height: ");
    }
    //Checking if height is within range
    while (n < 1 || n > 8);

    printf("Stored: %i\n", n);

    //Printing rows
    for (int i = 0; i < n; i++)
    {
        //printing empty spaces
        for (int k = n - 1; k > i; k--)
        {
            printf(" ");
        }

        //Printing collumns
        for (int j = 0; j <= i; j++)
        {
            printf("#");
        }

        printf("\n");

    }

}
