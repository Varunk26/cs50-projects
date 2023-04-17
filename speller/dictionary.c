// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <string.h>
#include <strings.h>
#include<stdio.h>
#include<stdlib.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];

//word count
int wcount;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    int c_index = hash(word);
    node *cursor = table[c_index];

    while (cursor != NULL)
    {
        if (strcasecmp(cursor->word, word) == 0)
        {
            return true;
        }
        else
        {
            cursor = cursor->next;
        }
    }

    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    int sum = 0;

    sum = (int)(toupper(word[0])) - 65;

    return sum;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    wcount = 0;
    unsigned int t_index;
    char l_word[N + 1];

    //new code
    for (int i = 0; i < N; i++)
    {
        table[i] = NULL;
    }



    FILE *fr_dictionary = fopen(dictionary, "r");
    if (fr_dictionary == NULL)
    {
        printf("could not load dictionary\n");
        return false;
    }

    while (fscanf(fr_dictionary, "%s", l_word) != EOF)
    {

        node *new_word = malloc(sizeof(node));

        if (new_word == NULL)
        {
            printf("lack of memory\n");
            return false;
        }

        strcpy(new_word->word, l_word);
        new_word->next = NULL;

        //calculate hash
        t_index = hash(l_word);

        //prepend node to a list
        new_word->next = table[t_index];
        table[t_index] = new_word;
        wcount++;

    }

    fclose(fr_dictionary);

    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    return wcount;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    for (int i = 0; i < N; i++)
    {
        node *cursor = table[i];

        while (cursor != NULL)
        {
            node *temp = cursor;
            cursor = cursor->next;
            free(temp);
        }

        if (i == (N - 1) && cursor == NULL)
        {
            free(cursor);
            return true;
        }
    }
    return false;
}