#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // TODO: Prompt for start size

    int start;
    int end;
    int n = 0;

    do
    {
        start = get_int("Start size:");
    }
    while (start < 9);

    // TODO: Prompt for end size
    do
    {
        end = get_int("End size:");
    }
    while (end < start);

    // TODO: Calculate number of years until we reach threshold
    while (start < end)
    {
        int born;
        int dead;

        born = start / 3;
        dead = start / 4;

        start = start + born - dead;
        n++;
    }

    printf("Years: %i\n", n);

    // TODO: Print number of years
}
