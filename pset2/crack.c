#include <cs50.h>
#include <stdio.h>
#include <string.h>
#define _XOPEN_SOURCE
#include <unistd.h>
#include <crypt.h>

bool check(int n);
int crack(string hash);

int main (int argc,string argv[])
{
    if (check(argc))
    {
        // A function to crack the hash and print the password
        crack(argv[1]);
        return 0;
    }
    else
    {
        printf ("Usage: ./crack hash\n");
        return 1;
    }
}

bool check(int n)
{
    if (n == 2)
    {
        return true;
    }
    else
    {
        return false;
    }
}

int crack(string hash)
{
    char salt[] = "  ";
    salt[0] = hash[0];
    salt[1] = hash[1];
    char first = '\0',second = '\0',third = '\0',fourth = '\0',fifth = '\0';
    char key[] = "     ";
    int i = 0,j = 0,m = 0,n = 0,v = 0;
    for (v = 0; v < 53; v++)
    {
        key[4] = fifth;
        for (i = 0; i < 53; i++)
        {
            key[3] = fourth;
            for (j = 0; j < 53; j++)
            {
                key[2] = third;
                for (m = 0; m < 53; m++)
                {
                    key[1] = second;
                    for (n = 0; n < 53; n++)
                    {
                        key[0] = first;
                        string possible_hash = crypt (key,salt);
                        if ((strcmp(hash,possible_hash)) == 0)
                        {
                            for (int k = 0; k < 5; k++)
                            {
                                printf ("%c",key[k]);
                            }
                            printf ("\n");
                            return 0;
                        }
                        first++;
                        if (n == 0)
                        {
                            first = 'A';
                        }
                        if (n == 26)
                        {
                            first = 'a';
                        }
                    }
                    second++;
                    if (m == 0)
                    {
                        second = 'A';
                    }
                    if (m == 26)
                    {
                        second = 'a';
                    }
                }
                third++;
                if (j == 0)
                {
                    third = 'A';
                }
                if (j == 26)
                {
                    third = 'a';
                }
            }
            fourth++;
            if (i == 0)
            {
            fourth = 'A';
            }
            if (i == 26)
            {
            fourth = 'a';
            }
        }
        fifth++;
        if (v == 0)
        {
        fifth = 'A';
        }
        if (v == 26)
        {
        fifth = 'a';
        }
    }
    return 1;
}
