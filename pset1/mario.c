#include <cs50.h>
#include <stdio.h>

void print_pyramid(int n);

int main(void)
{
    bool condition = true;
    while (condition)
    {
        printf ("Height: ");
        int height = get_int();
        if (height <= 23 && height >= 0 )
            {
                print_pyramid(height);  
                condition = false;
            }
    }  
}
   

void print_pyramid(int n)
{
    for (int i = 0; i < n ; i++)
    {
        int j = n - i - 1;
        while (j > 0)
            {
                printf (" ");
                j--;
            }
        for (int h = 0 ; h <= i ; h++)
            {
                printf ("#");
            }
        printf ("  ");
        for (int h = 0 ; h <= i ; h++)
            {
                printf ("#");
            } 
        printf ("\n");
    }
}