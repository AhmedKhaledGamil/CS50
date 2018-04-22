#include <stdio.h>

int main (int argc, char *argv[])
{
    //Ensure proper usage
    if (argc != 2)
        {
            fprintf (stderr, "Usage: ./recover image\n");
            return 1;
        }
    
    //Ensure proper input
    FILE *input = fopen(argv[1], "r");
    if (input == NULL)
        {
            fclose(input);
            fprintf (stderr, "Could not open %s.\n",argv[1]);
            return 2;
        }
    // "It didn't compile inside the while loop"
    FILE *image = NULL;
    
    //for naming jpg files
    int jpgcounter = 0;
    char jpgname[8] = {0};
    
    // because block size in jpeg is 512 bytes "It didn't work with Char"
    unsigned char buffer[512] = {0};
    
    fread (&buffer, 512, 1, input);
    
    while (fread (&buffer, 512, 1, input) > 0)
        {
            if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] == 0xe0 || buffer[3] == 0xe1 || buffer[3] == 0xe2))
                {
                    sprintf (jpgname, "%03i.jpg" , jpgcounter);
                    image = fopen(jpgname, "w");
                    jpgcounter ++;
                    fwrite (buffer, sizeof(buffer), 1, image);
                }
            else if (jpgcounter > 0)
                {
                    fwrite (buffer, sizeof(buffer), 1, image);
                }
        }
        
    //closing all files
    fclose (input);
    fclose (image);
}