#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

int numberofwords(string word);
int numberofletters(string word);
int numberofsentences(string word);
float calculateindex(float letters, float words, float sentences);

int main(void)
{
    float letters;
    float sentences;
    float words;
    float index;
    string text;


    //get text
    text = get_string("Text:");
    //calculate letters
    letters = numberofletters(text);
    //calculate words
    words = numberofwords(text);
    //calculate sentences
    sentences = numberofsentences(text);

    //ycalculate index
    index = calculateindex(letters, words, sentences);
    index = round(index);

    //Check for grade range

    if (index < 1)

    {
        printf("Before Grade 1\n");
    }

    else if (index >= 1 && index <= 16)

    {
        printf("Grade %i\n", (int) floor(index));
    }

    else if (index > 16)

    {
        printf("Grade 16+\n");
    }

    else
    {
        return 1;
    }
}

//Calculate number of letters

int numberofletters(string word)
{
    int x = strlen(word);
    int letters = 0;

    for (int i = 0; i < x; i++)
    {
        if (isalpha(word[i]))
        {
            letters++;
        }
    }

    return letters;
}

//Calculate number of words

int numberofwords(string word)
{
    int x = strlen(word);
    int words = 0;

    for (int i = 0; i <= x; i++)
    {
        if (isspace(word[i]))
        {
            words++;
        }
    }
    words++;
    return words;
}

//Calculate number of sentences

int numberofsentences(string word)
{
    int x = strlen(word);
    int sentences = 0;

    for (int i = 0; i < x; i++)
    {
        if (word[i] == '.' || word[i] == '!' || word[i] == '?')
        {
            sentences++;
        }
    }

    return sentences;
}

//calculate index

float calculateindex(float letters, float words, float sentences)
{
    float index, l, s = 0;

    l = (letters / words) * 100;
    s = (sentences / words) * 100;
    index = (0.0588 * l) - (0.296 * s) - 15.8;
    return index;
}




