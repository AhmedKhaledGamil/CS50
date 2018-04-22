/**
 * helpers.c
 *
 * Helper functions for Problem Set 3.
 */
 
#include <cs50.h>

#include "helpers.h"

/**
 * Returns true if value is in array of n values, else false.
 */
bool search(int value, int values[], int n)
{
    // TODO: implement a searching algorithm
    if (value < 0)
        {
            return false;
        }
    int end = n - 1;
    int start = 0;
    int list_length = end - start;
    int middle = 0;
    do 
        {
            middle = (end + start)/2;
            if (value == values[middle])
                {
                    return true;
                }
            else if (value > values[middle])
                {
                    start = middle + 1;
                    list_length = end - start + 1;
                }
            else 
                {
                    end = middle -1;
                    list_length = end - start + 1;
                }
        } while (list_length > 0);
    return false;
}

/**
 * Sorts array of n values.
 */
void sort(int values[], int n)
{
    // TODO: implement a sorting algorithm
    int index = 0;
    int counting_array[65536] = {0};
    for (int i = 0; i < n; i++)
        {
            counting_array[values[i]]++;
        }
    for (int i = 0; i < 65536; i++)
        {
            for (int j = 0; j < counting_array[i]; j++)
                {
                    values[index] = i;
                    index++;
                }
        }
    return;
}
