/* 
 * Daniel Gaidar - gaidar@bc.edu
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BYTE_SIZE 8
#define ON_SWITCH 1

char * dec_to_bin_str(char input, char * output, int * counter) {
    int shift = (sizeof(input) * BYTE_SIZE) - 1;
    unsigned char mask = 1u << shift;
    int i = 0;
    int a = 0;
    while (mask) {
        if (((input & mask) >> shift) == ON_SWITCH){
            a++;
        }
        output[i++] = ((input & mask) >> shift--) + '0';
        mask>>=1;
    }
    * counter = a;
    return output;
}
int encode(unsigned char input, int * bits) {
    char output[BYTE_SIZE];
    int a;
    char * mold;
    mold = dec_to_bin_str(input, output, &a);
    strcpy(output, mold);
    char fin[a+1];
    fin[0] = a + '0';
    int n = 1;
    for (int i = BYTE_SIZE; i > -1; i--) { 
        if (output[i] == '1') {
            char index = (BYTE_SIZE - i - 1) + '0';
            fin[n++] = index;   
        }
    }
    * bits = atoi(fin);
    return a;
}
void read_and_encode_file(char * in_file, char * out_file){
    FILE * Fr = fopen(in_file, "r");
    FILE * Fw = fopen(out_file, "w");
    char read;
    int writer;
    read = fgetc(Fr);
    while (read != EOF) {
        encode(read, &writer);
        fprintf(Fw, "%d", writer);
        read = fgetc(Fr);
    }
    fclose(Fw);
    fclose(Fr);
}
int main(int argc, char * argv[]){
    if (argc <= 2) { 
        fprintf(stderr, "Please enter input and output file names as command-line arguments.");
        return EXIT_FAILURE;
    }
    else {
       read_and_encode_file(argv[1], argv[2]);
       return EXIT_SUCCESS;
    }    
}

