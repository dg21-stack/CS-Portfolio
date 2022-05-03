/* 
 * Daniel Gaidar - gaidar@bc.edu
 */

#include <stdio.h>
#include <stdlib.h>

#define BYTE_SIZE 8

char decode(const int count, const int bits[]) { 
    int twos = 1;
    int sum = 0;
    for (int n =0; n< count; n++) {
        twos <<= bits[n];
        sum += twos;
        twos = 1;
    }
    char outter = sum;
    return outter;
}
void read_and_decode_file(const char * file_name) {
    FILE * Fr = fopen(file_name, "r");
    int a;
    int bits[BYTE_SIZE];
    char printer;
    while (fscanf(Fr, "%1d", &a) != EOF) {
       for (int i = 0; i < a; i++) {
          fscanf(Fr, "%1d", &bits[i]);
       } 
       printer = decode(a, bits);
       fprintf(stdout, "%c", printer);
    }
}
int main(int argc, char * argv[]) {
    if (argc <= 1) {
        fprintf(stderr, "Please enter an input file name as a command-line argument.\n");
        return EXIT_FAILURE;
    }
    else { 
        read_and_decode_file(argv[1]);
        return EXIT_SUCCESS;
    }  
}
