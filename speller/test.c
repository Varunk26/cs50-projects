#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>

int main(void)
{
    // TODO: Improve this hash function

    string word = get_string("word:");
    printf("\n");
    int sum = 0;

    sum = (int)(toupper(word[0])) - 65;
    printf("sum:%i\n", sum);
}


