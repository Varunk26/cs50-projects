#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

int main(int argc, char *argv[])
{
    //declare variables
    typedef uint8_t BYTE;
    int count = 0;
    char filename[8];
    int BLOCK_SIZE = 512;
    FILE *img_out;
    int old_count = 0;

    BYTE buffer[512];

    //check if argc = 2

    if (argc != 2)
    {
        printf("Enter image file\n");
        return 1;
    }

//open memory card
    FILE *f = fopen(argv[1], "r");

    if (f == NULL)
    {
        printf("could not open file");
        return 1;
    }

    while (fread(buffer, 1, BLOCK_SIZE, f) == BLOCK_SIZE)
    {
        //finding jpeg in memory
        if ((buffer[0] == 0xff) && (buffer[1] == 0xd8) && (buffer[2] == 0xff) && ((buffer[3] & 0xf0) == 0xe0))
        {
            //compute name of the jpg file
            sprintf(filename, "%03i.jpg", count);

            //open file and write jpeg to it
            img_out = fopen(filename, "w");
            if (img_out != NULL)
            {
                fwrite(buffer, 1, BLOCK_SIZE, img_out);
            }

            count++;

        }
        //check if next blocksize is start of a new Jpeg
        else if ((count > old_count) && ((buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff) && ((buffer[3] & 0xf0) == 0xe0)))
        {
            //close and open new file for new jpeg
            old_count = count;
            count++;
            fclose(img_out);
            sprintf(filename, "%03i.jpg", count);

            img_out = fopen(filename, "w");
            if (img_out != NULL)
            {
                fwrite(buffer, 1, BLOCK_SIZE, img_out);
            }
        }

        // checking in next blocksize is not a new Jpeg file
        //potential error line 71

        else if ((count > 0) && !((buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff) && ((buffer[3] & 0xf0) == 0xe0)))
        {
            //writing new block into same file
            fwrite(buffer, 1, BLOCK_SIZE, img_out);
        }

    }

    fclose(f);
    fclose(img_out);

}

