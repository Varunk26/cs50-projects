#include "helpers.h"
#include <math.h>
#include <stdlib.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    double average = 0;

    //find average
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            average = (image[i][j].rgbtBlue + image[i][j].rgbtRed + image[i][j].rgbtGreen) / 3.0;

            //round to nearest int
            average = round(average);

            //store average
            image[i][j].rgbtBlue = (BYTE) average;
            image[i][j].rgbtGreen = (BYTE) average;
            image[i][j].rgbtRed = (BYTE) average;

        }
    }

    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    //declare new red, green & blue
    double new_red = 0.0;
    double new_blue = 0.0;
    double new_green = 0.0;
    RGBTRIPLE copy[height][width];

    //create a copy of image
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copy[i][j] = image[i][j];
        }
    }


    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            //initializing sepiared
            new_red = (0.393 * (double) image[i][j].rgbtRed) + (0.769 * (double) image[i][j].rgbtGreen) + (0.189 *
                      (double) image[i][j].rgbtBlue);
            new_red = round(new_red);

            if (new_red > 255.0)
            {
                new_red = 255.0;
            }

            //initializing sepiagreen
            new_green = (0.349 * (double) image[i][j].rgbtRed) + (0.686 * (double) image[i][j].rgbtGreen) + (0.168 *
                        (double) image[i][j].rgbtBlue);
            new_green = round(new_green);

            if (new_green > 255.0)
            {
                new_green = 255.0;
            }

            //initializing sepiablue
            new_blue = (0.272 * (double) image[i][j].rgbtRed) + (0.534 * (double) image[i][j].rgbtGreen) + (0.131 *
                       (double) image[i][j].rgbtBlue);
            new_blue = round(new_blue);

            if (new_blue > 255.0)
            {
                new_blue = 255.0;
            }

            //storing new colours to copy pixel
            copy[i][j].rgbtRed = (BYTE) new_red;
            copy[i][j].rgbtGreen = (BYTE) new_green;
            copy[i][j].rgbtBlue = (BYTE) new_blue;

        }
    }
    //storing copy pixel to original image
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < height; j++)
        {
            image[i][j] = copy[i][j];
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE new_image[height][width];
    int k = width;

    //initializing loop to store reflected image in a new image
    for (int i = 0; i < height; i++)
    {
        k = width;

        for (int j = 0; j < width; j++)
        {
            //re -arranging pixels horizontally
            new_image[i][k - 1] = image[i][j];
            k--;
        }

    }
    //storing new_image to original
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j] = new_image[i][j];
        }
    }

    return;

}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE copy[height][width];

    //copy image
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copy[i][j] = image[i][j];
        }
    }

    //find adjacent pixels
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int Red = 0;
            int Blue = 0;
            int Green = 0;
            float counter = 0.0;

            for (int x = -1; x < 2; x++)
            {
                for (int y = -1; y < 2; y++)
                {
                    int a_x = i + x;
                    int a_y = j + y;

                    if (!(a_x < 0 || a_x > (height - 1) || a_y < 0 || a_y > (width - 1)))
                    {
                        Red = Red + image[a_x][a_y].rgbtRed;
                        Blue = Blue + image[a_x][a_y].rgbtBlue;
                        Green = Green + image[a_x][a_y].rgbtGreen;
                        counter++;
                    }
                }
            }

            copy[i][j].rgbtRed = Red / counter;
            copy[i][j].rgbtBlue = Blue / counter;
            copy[i][j].rgbtGreen = Green / counter;

        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j].rgbtRed = copy[i][j].rgbtRed;
            image[i][j].rgbtBlue = copy[i][j].rgbtBlue;
            image[i][j].rgbtGreen = copy[i][j].rgbtGreen;

        }
    }

    return;
}




