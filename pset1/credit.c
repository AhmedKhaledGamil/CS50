#include <cs50.h>
#include <stdio.h>
#include <math.h>

int digits(long long n);
bool check(int n);
bool validity(long long n);
string creditcard_type(long long n);

int main(void)
{
    printf ("Number: ");
    long long credit_number = get_long_long();
    int no_digits = digits(credit_number);
    if (check(no_digits))
        {
            if (validity(credit_number))
                {
                    string type = creditcard_type(credit_number);
                    printf ("%s\n",type);
                }
            else
                {
                    printf ("INVALID\n");
                }
        }
    else
        {
            printf ("INVALID\n");
        }
    return 0;
}

// Count The Digits Of The Entered Credit Card
int digits(long long n)
{
     int digits = floor(log10(llabs(n))) + 1;
     return digits;
}

// Check If It's AmericanExpress Or MasterCard Or Visa
bool check(int n)
{
    if (n == 13 || n == 15 || n == 16)
        {
            return true;
        }
    else
        {
            return false;
        }
}

//Check Luhn's Algorithm For Validity
bool validity(long long n)
{
    int sum = 0;
    int j = digits(n);
    long long x;
    int product;
    int y;
    for (int i = 0; i < j ; i++)
        {
            x = n%10;
            n = n/10;
            if (i%2)
                {
                    product = x*2;
                    if (product <10)
                        {
                            sum = sum + product;
                        }
                    else if (product >= 10)
                        {
                            for (int k = 0 ; k < 2; k++)
                                {
                                    y = product%10;
                                    product = product/10;
                                    sum = sum + y ;
                                }
                        }
                }
            else
                {
                    sum = sum + x;
                }
            }
    sum = sum%10;
    if (sum == 0)
        {
            return true;
        }
    else
        {
            return false;
        }
}

string creditcard_type(long long n)
{
    string type = "";
    long long x = digits(n);
    if (x == 15)
        {
            n = n / (10000000000000);
            if (n == 34 || n == 37)
                {
                    type = "AMEX";
                }
            else
                {
                    type = "INVALID";
                }
        }
    else if (x == 13)
        {
            type = "VISA";
        }
    else if (x == 16)
        {
            int mcard = n / (100000000000000);
            n = n / (1000000000000000);
            if (n == 4)
                {
                    type = "VISA";
                }
            else
                {
                    if (mcard >= 51 && mcard <= 55)
                    {
                        type = "MASTERCARD";
                    }
                    else
                    {
                        type = "INVALID";
                    }
                }
        }
    return type;
}