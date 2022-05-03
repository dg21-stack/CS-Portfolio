/*
 * Author : Daniel Gaidar - gaidar@bc.edu
 */

#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>

#define MIN_DIM_POWER 3
#define MAX_DIM_POWER 10
#define MAX_VALUE 20
#define FALSE 0
#define TRUE 1

void multiply(const int dim, const int * const a, const int * const b, int * const c){   
    for (int i = 0; i < dim; i++){
        for (int j = 0; j < dim; j++){
            c[i * dim + j] = 0;
            for (int k = 0; k < dim; k++){
                c[i * dim + j] += a[i * dim + k] * b[k * dim + j];
            }    
        }
    }
}
void multiply_transpose(const int dim, const int * const a, const int * const b_t, int * const c){
    for (int i = 0; i < dim; i++){
        for (int j = 0; j < dim; j++){
        c[i * dim + j] = 0;
            for (int k = 0; k < dim; k++){
                c[i * dim + j] += a[i * dim + k] * b_t[j * dim + k];
            }     
        }
    }
}
void transpose(const int dim, int * m){
    int tmp;
    for (int i = 0; i < dim; i++){
        for (int j = 0; j < i; j++){
            tmp = m[i * dim + j];
            m[i * dim + j] = m[j * dim + i];
            m[j * dim + i] = tmp;
        }
    }
}
void print(const int dim , const int * const m){
    for (int n = 0; n < dim * dim; n++){
        printf("%d ", *(m + n));
    }
    printf("\n");
}
void init(const int dim, int * const m){
    for (int i = 0; i < dim * dim; i++) {
        m[i] = rand() % MAX_VALUE;
    }   
}
struct timeval run_and_time(void (* mult_func)(const int, const int * const, const int * const, int * const), const int dim, const int * const a, const int * const b, int * const c){
    struct timeval time, tvalBefore, tvalAfter;
    gettimeofday(&tvalBefore, NULL);
    mult_func(dim,a,b,c);
    gettimeofday(&tvalAfter, NULL);
    time.tv_usec = tvalAfter.tv_usec - tvalBefore.tv_usec;
    time.tv_sec = tvalAfter.tv_sec - tvalBefore.tv_sec;
    if (time.tv_usec < 0) {
        time.tv_sec--;
        time.tv_usec += 1000000;
    }
    return time;
}
int verify(const int dim, const int * const c1, const int * const c2) {
    for (int i = 0; i < dim * dim; i++) {
        if (c1[i] != c2[i]){
            return FALSE;
        }
    }
    return TRUE;   
}
void run_test(const int dim){
    int * a = malloc(sizeof(int) * dim * dim);
    int * b = malloc(sizeof(int) * dim * dim);
    int * c1 = malloc(sizeof(int) * dim * dim);
    int * c2 = malloc(sizeof(int) * dim * dim);
    init(dim,a);
    init(dim,b);
    struct timeval matrix = run_and_time(&multiply, dim, a, b, c1);
    transpose(dim, b);
    struct timeval t_matrix = run_and_time(&multiply_transpose, dim, a, b, c2);
    free(a);
    free(b);
    if (verify(dim, c1,c2)){
        printf("Results agree\n");
        printf("Standard Multiplication: %ld seconds, %d microseconds \n", (long) matrix.tv_sec, (int) matrix.tv_usec);
        printf("Multiplication with transpose: %ld seconds, %d microseconds \n", (long) t_matrix.tv_sec, (int) t_matrix.tv_usec);
    }
    else {
       printf("Results between matrices DO NOT agree \n");
    }
   free(c1);
   free(c2); 
}
int main(int argc, char * argv[]){
    for (int power = MIN_DIM_POWER; power <= MAX_DIM_POWER; power++){
        run_test(1 << power);
    }
    return EXIT_SUCCESS;
}
