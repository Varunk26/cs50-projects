#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

int plaintocipher(int a, string s);
char cipher(int a, char p);

int main(int argc, string argv[])
{
    string key = argv[1];
    int l = strlen(argv[1]);
    int key_to_int = atoi(key);
    string text;


    //check if argc = 2

    if (argc != 2)
    {
        printf("Usage: ./ caesar key\n");
        return 1;
    }


    //check if key i digit

    for (int i = 0; i < l; i++)
    {
        if (isdigit(key[i]) == 0)
        {

            printf("Usage: ./ caesar key\n");
            return 1;

        }
    }

    //Get string from user prompt
    text = get_string("plaintext: ");
    //convert plain to cipher text
    plaintocipher(key_to_int, text);



}

//Convert plain text to cipher text

int plaintocipher(int a, string s)

{
    //check if character is alphabet and convert it into alphabetical index

    int k = strlen(s);
    printf("ciphertext: ");

    for (int i = 0; i < k; i++)
    {
        // Check for uppercase
        if (isupper(s[i]) != 0)
        {
            s[i] = s[i] - 65;
            s[i] = cipher(a, s[i]);
            s[i] = s[i] + 65;
            printf("%c", s[i]);
        }

        //check for lower case
        else if (islower(s[i]) != 0)
        {
            s[i] = s[i] - 97;
            s[i] = cipher(a, s[i]);
            s[i] = s[i] + 97;
            printf("%c", s[i]);
        }
        //check for non alphabet
        else
        {
            printf("%c", s[i]);
        }
    }
    printf("\n");
    return 0;
}
//convert character into cipher
char cipher(int a, char p)
{
    int c;
    //mod function for rotation of alphabets
    c = (p + a) % 26;

    return c;

}
