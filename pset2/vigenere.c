#include <cs50.h>
#include <stdio.h>
#include <string.h>

bool check1(int n);
bool check2(string k);
string chiper(string text,string key);
int change(char c);

int main (int argc, string argv[])
{
    // check if only two commands entered
    if (check1(argc))
        {
            string k = argv[1];
            // check if key consists of letters only
            if (check2(k))
                {
                    printf ("plaintext: ");
                    string plain_text = get_string();
                    // a Function to the chiper text
                    string s = chiper(plain_text,k);
                    printf ("ciphertext: ");
                    printf("%s",s);
                    // int n = strlen(s);
                    // char array[n+1];
                    // for (int i=0; i<n; i++)
                    //     array[i] = s[i];
                    // array[n+1] = '\0';
                    // printf("%s",array);

                }
            else
                {
                    printf ("Usage: ./vigenere k\n");
                    return 1;
                }
            printf("\n");
            return 0;
          }
    else
        {
            printf ("Usage: ./vigenere k\n");
            return 1;
        }
}

bool check1(int n)
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

bool check2(string k)
{
    for(int i = 0,j = strlen(k); i < j; i++ )
        {
            // check if k is only letters not numbers
            if (!((k[i] >= 'a' && k[i] <= 'z') || (k[i] >= 'A' && k[i] <= 'Z')))
                {
                    return false;
                }
        }

    return true;
}

// To change each letter to corresponding number
int change(char c)
{
    char small = 'a';
    char cap = 'A';
    int key = 0;
    for (int i =  0; i < 26; i++)
        {
            if (c == small || c == cap )
                {
                    return key;
                }
            small++;
            cap++;
            key++;
        }
    return key;
}

string chiper(string text,string key)
{
    int value = 0;
    int offset = 0;
    int key_digits = strlen(key);
    for (int i = 0,n = strlen(text);i < n;i++)
        {
            if (text[i] == ' ')
                {
                    continue;
                }
            else
                {
                    value = change(key[offset]);
                    if (text[i] <= 'z' && text[i] >= 'a')
                        {
                            if ((text[i] + value) <= 'z')
                                {
                                    text[i] = text[i] + value;
                                    offset++;
                                }
                            else
                                {
                                    text[i] = text[i] -26;
                                    text[i] = text[i] + value;
                                    offset++;
                                }
                        }
                    else if (text[i] <= 'Z' && text[i] >= 'A')
                        {
                            if ((text[i] + value) > 'Z')
                                {
                                    text[i] = text[i] -26;
                                    text[i] = text[i] + value;
                                    offset++;

                                }
                            else
                                {
                                    text[i] = text[i] + value;
                                    offset++;
                                }

                        }
                }
            if (offset == key_digits)
                {
                    offset = 0;
                }
        }
        return text;
}