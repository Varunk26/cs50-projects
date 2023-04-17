#include <cs50.h>
#include <stdio.h>

int main(void)
{
    //Get name
    string name;
    name = get_string("What is your name?\n");

    //print name
    printf("hello, %s\n", name);
}