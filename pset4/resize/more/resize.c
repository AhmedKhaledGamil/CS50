#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#include "bmp.h"

int main(int argc, char *argv[])
{
    // ensure proper usage
    if (argc != 4)
    {
        fprintf(stderr, "Usage: ./resize n infile outfile\n");
        return 1;
    }

    // remember filenames
    float f = atof(argv[1]);
    if (f <= 0 || f >= 100)
        {
            fprintf(stderr, "The factor must be larger than zero and less than 100\n");
            return 5;
        }
    char *infile = argv[2];
    char *outfile = argv[3];

    // open input file 
    FILE *inptr = fopen(infile, "r");
    if (inptr == NULL)
    {
        fprintf(stderr, "Could not open %s.\n", infile);
        return 2;
    }

    // open output file
    FILE *outptr = fopen(outfile, "w");
    if (outptr == NULL)
    {
        fclose(inptr);
        fprintf(stderr, "Could not create %s.\n", outfile);
        return 3;
    }

    // read infile's BITMAPFILEHEADER
    BITMAPFILEHEADER bf;
    fread(&bf, sizeof(BITMAPFILEHEADER), 1, inptr);

    // read infile's BITMAPINFOHEADER
    BITMAPINFOHEADER bi;
    fread(&bi, sizeof(BITMAPINFOHEADER), 1, inptr);

    // ensure infile is (likely) a 24-bit uncompressed BMP 4.0
    if (bf.bfType != 0x4d42 || bf.bfOffBits != 54 || bi.biSize != 40 || 
        bi.biBitCount != 24 || bi.biCompression != 0)
    {
        fclose(outptr);
        fclose(inptr);
        fprintf(stderr, "Unsupported file format.\n");
        return 4;
    }
    // determine original padding for scanlines
    int original_padding = (4 - (bi.biWidth * sizeof(RGBTRIPLE)) % 4) % 4;
    int original_width = bi.biWidth;
    int original_height = bi.biHeight;
    bi.biWidth *= f;
    bi.biHeight *= f;
    
    // determine resized padding for scanlines
    int padding = (4 - (bi.biWidth * sizeof(RGBTRIPLE)) % 4) % 4;
    
    bi.biSizeImage = ((sizeof(RGBTRIPLE) * bi.biWidth) + padding ) * abs(bi.biHeight);
    bf.bfSize = bi.biSizeImage + sizeof(BITMAPFILEHEADER) + sizeof(BITMAPINFOHEADER);
    
    // write outfile's BITMAPFILEHEADER
    fwrite(&bf, sizeof(BITMAPFILEHEADER), 1, outptr);

    // write outfile's BITMAPINFOHEADER
    fwrite(&bi, sizeof(BITMAPINFOHEADER), 1, outptr);
    // used for testing
    long place = ftell(inptr);
    long place2 = ftell(outptr);
    fpos_t position;
    // if the factor is integer(upsizing or identical)
    if (floor(f) == f)
    {
        // iterate over infile's scanlines
        for (int i = 0, biHeight = abs(original_height); i < biHeight; i++)
        {
            fgetpos(inptr, &position);
            for (float m = 0; m < f; m++)
            {
                fsetpos(inptr, &position);
                // iterate over pixels in scanline
                for (int j = 0; j < original_width; j++)
                {
                    // temporary storage
                    RGBTRIPLE triple;
        
                    // read RGB triple from infile
                    fread(&triple, sizeof(RGBTRIPLE), 1, inptr);
                    place = ftell(inptr);
                    
                    // write the same pixel f number of times
                    for (float k = 0; k < f; k++)  
                    {
                        // write RGB triple to outfile
                        fwrite(&triple, sizeof(RGBTRIPLE), 1, outptr);
                    }
                }
                // skip over old padding, if any
                fseek(inptr, original_padding, SEEK_CUR);
                place = ftell(inptr);
                // Add padding to output file
                for (int k = 0; k < padding; k++)
                    {
                        fputc(0x00, outptr);
                    }
            }
        }
    }
    else 
        {
        //upsizing
        if (f > 1)
            {
                // additional width after resizing
                int diff = bi.biWidth - original_width;
                // used to return the pointer the begining of the scanline when needed
                long cursor = (sizeof(RGBTRIPLE) * original_width) + original_padding;
                // used to count how many time cursor is used
                int counter = 0;
                // condition to end repetition of using cursor
                int repetition = 0;
                // iterate over infile's scanlines
                for (int i = 0, biHeight = abs(original_height); i < biHeight + diff; i++)
                {
                    if (i == ((biHeight/2))+1)
                        {
                            repetition = 1; 
                        }
                    if (repetition)
                        {
                            fseek(inptr, -cursor, SEEK_CUR);
                            counter++;
                            if (counter == diff)
                                repetition = 0;
                        }
                    fgetpos(inptr, &position);
                    for (float m = 0; m < floor(f); m++)
                    {
                        fsetpos(inptr, &position);
                        // iterate over pixels in scanline
                        for (int j = 0; j < original_width; j++)
                        {
                            // temporary storage
                            RGBTRIPLE triple;
                
                            // read RGB triple from infile
                            fread(&triple, sizeof(RGBTRIPLE), 1, inptr);
                            place = ftell(inptr);
                            if (j == (original_width/2))
                                {
                                    for (int v = 0; v < diff; v++)
                                        {
                                            fwrite(&triple, sizeof(RGBTRIPLE), 1, outptr);
                                        }
                                }       
                            // write the same pixel f number of times
                            for (float k = 0; k < floor(f); k++)  
                            {
                                // write RGB triple to outfile
                                fwrite(&triple, sizeof(RGBTRIPLE), 1, outptr);
                            }
                        }
                        // skip over old padding, if any
                        fseek(inptr, original_padding, SEEK_CUR);
                        place = ftell(inptr);
                        // Add padding to output file
                        for (int k = 0; k < padding; k++)
                            {
                                fputc(0x00, outptr);
                            }
                    }
                }
            }
        //downsizing
        else
            {
                long cursor = (sizeof(RGBTRIPLE) * original_width) + original_padding;
                for (int i = 0, biHeight = abs(bi.biHeight); i < biHeight; i++)
                    {
                        fgetpos(inptr, &position);
                        for (float m = 0; m < f; m++)
                        {
                            fsetpos(inptr, &position);
                            // iterate over pixels in scanline
                            for (int j = 0; j < bi.biWidth; j++)
                            {
                                // temporary storage
                                RGBTRIPLE triple1;
                                RGBTRIPLE triple2;
                                RGBTRIPLE triple3;
                                RGBTRIPLE triple4;
                                RGBTRIPLE triple5;
                                
                                // read RGB triple from infile
                                fread(&triple1, sizeof(RGBTRIPLE), 1, inptr);
                                place = ftell(inptr);
                                fread(&triple2, sizeof(RGBTRIPLE), 1, inptr);
                                place = ftell(inptr);
                                // the rgb byte it self should not be counted
                                fseek(inptr, (cursor - 6), SEEK_CUR);
                                place = ftell(inptr);
                                fread(&triple3, sizeof(RGBTRIPLE), 1, inptr);
                                place = ftell(inptr);
                                fread(&triple4, sizeof(RGBTRIPLE), 1, inptr);
                                place = ftell(inptr);
                                fseek(inptr, -(cursor), SEEK_CUR);
                                place = ftell(inptr);
                                triple5.rgbtBlue = (triple1.rgbtBlue + triple2.rgbtBlue + triple3.rgbtBlue + triple4.rgbtBlue)/4;
                                triple5.rgbtGreen = (triple1.rgbtGreen + triple2.rgbtGreen + triple3.rgbtGreen + triple4.rgbtGreen)/4;
                                triple5.rgbtRed = (triple1.rgbtRed + triple2.rgbtRed + triple3.rgbtRed + triple4.rgbtRed)/4;
                                // write RGB triple to outfile
                                fwrite(&triple3, sizeof(RGBTRIPLE), 1, outptr);
                                place2 = ftell(outptr);
                            }
                            fseek(inptr, original_padding, SEEK_CUR);
                            // Add padding to output file
                            for (int k = 0; k < padding; k++)
                                {
                                    fputc(0x00, outptr);
                                    place2 = ftell(outptr);
                                }
                            fseek(inptr, cursor, SEEK_CUR);
                        }
                    }        
            }
        }
    // close infile
    fclose(inptr);

    // close outfile
    fclose(outptr);

    // success
    return 0;
}
