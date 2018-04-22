/**
 * Implements a dictionary's functionality.
 */

#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>

#include "dictionary.h"

#define ALPHABETS_SIZE 26
#define LENGTH 45


typedef struct node
    {
        bool is_word[ALPHABETS_SIZE + 1];

        /* Alphabets plus \ */
        struct node *children[ALPHABETS_SIZE + 1];
    }
    node;
    node *root;

unsigned int words = 0;
/**
 * Returns true if word is in dictionary else false.
 */
bool check(const char *word)
{
    node *ptr = root;
    int index;
    for (int i = 0; word[i] != '\0'; i++)
    {
        if (word[i] == '\'')
            {
                index = 26;
            }
        else
            {
                // To make index between 0 & 26
                index = tolower(word[i]) - 'a';
            }
        if (ptr -> children[index] == NULL)
        {
                if (ptr -> is_word[index])
                {
                    return true;
                }
                else
                {
                    return false;
                }
        }
        else if (ptr -> is_word[index] && (i == (strlen(word)-1)))
            {
                return true;
            }
        else
        {
            ptr = ptr -> children[index];
        }
    }
    /*if (ptr -> is_word)
                {
                    return true;
                }*/
    return false;
}

/**
 * Loads dictionary into memory. Returns true if successful else false.
 */
bool load(const char *dictionary)
{
    // give the root the size it needs
    root = malloc(sizeof(node));
    //Conditional jump or move depends on uninitialised values
    memset(root,0,sizeof(node));
    // opening the dictionary
    FILE *file = fopen(dictionary, "r");

    // checking it returns something
    if (file == NULL)
    {
        return false;
    }

    // size of the longest word plus \0
    char word[LENGTH+1];

    while (fscanf (file , "%s" , word) != EOF)
    {
        // making a default pointer looks for the root at each iteration
        node *ptr = root;

        int i = 0, index = 0;
        for (; word[i] != '\0'; i++)
        {
            if (word[i] == '\'')
            {
                index = 26;
            }
            else
            {
                // To make index between 0 & 26
                index = tolower(word[i]) - 'a';
            }
            if (ptr -> children[index] == NULL)
            {
                if (i == strlen(word)-1)
                    {
                        ptr->is_word[index] = true;
                    }
                // If the pointer is not pointing at something create a space in memory for it to look at and create a new row
                ptr -> children[index] = malloc(sizeof(node));
                ptr = ptr -> children[index];
                //Conditional jump or move depends on uninitialised values
                memset(ptr,0,sizeof(node));
                //ptr -> children[index] = NULL;
                /*if (i == strlen(word)-1)
                    {
                        ptr->is_word = true;
                    }*/
                //ptr = ptr -> children[index];
            }
            else
            {
                // If it is already the pointing at a row then make the pointer points at it
                ptr = ptr -> children[index];
            }
        }
        //ptr -> is_word[index] = true;
        words++;
    }

    fclose(file);

    return true;
}

/**
 * Returns number of words in dictionary if loaded else 0 if not yet loaded.
 */
unsigned int size(void)
{
    return words;
}

void freenode(node *ptr)
{
   for (int i = 0; i < ALPHABETS_SIZE + 1; i++)
   {
       if (ptr -> children[i] != NULL)
       {
           freenode(ptr -> children[i]);
       }
   }
   free (ptr);
}


/**
 * Unloads dictionary from memory. Returns true if successful else false.
 */
bool unload(void)
{
    freenode(root);
    return true;
}
