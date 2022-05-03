/*
 * Daniel Gaidar - gaidar@bc.edu
 */

#include <stdlib.h>
#include <stdio.h>
#include <signal.h>
#include <string.h>
#include <unistd.h>
#include <errno.h>

#define NUM_HANDLERS 5
#define MAX_COUNT 5

typedef void (*sighandler_t)(int signum);

sighandler_t backup[NUM_HANDLERS];
sighandler_t custom[NUM_HANDLERS];

sighandler_t sigaction_checked(int sig_num, sighandler_t handler) { 
    struct sigaction new_action;
    struct sigaction old_action; 
    new_action.sa_handler = handler;
    sigemptyset(& (new_action.sa_mask));
    sigaddset(& (new_action.sa_mask), sig_num);
    if (sigaction(sig_num, & new_action, NULL) == -1) {
        fprintf(stderr, "Error instlling signal handler: %s", strerror(errno));
        exit(EXIT_FAILURE);
    } 
    return old_action.sa_handler;       
}

void SIGHUP_handler(int signum) {
    puts("Hey, don't hang up on me!");
}
void SIGINT_handler(int signum){
    puts("Hey, don't interrupt me!");
}
void SIGQUIT_handler(int signum){
    puts("I refuse to quit!");
}
void SIGILL_handler(int signum){
    puts("I did nothing illegal!");
}
void custom_handler(int signal){
    static int count = 0;
    custom[signal](signal);
    if (++count >= MAX_COUNT) {
        sigaction_checked(signal, backup[count]);
    }    
    
}
void install_handlers(){
    custom[1] = SIGHUP_handler;
    custom[2] = SIGINT_handler;
    custom[3] = SIGQUIT_handler;
    custom[4] = SIGILL_handler;
    for (int i = 1; i < 5; i++) {
        sigaction_checked(i, custom_handler);
    }
}
int main(){
    int pid_t= getpid();
    printf("pid is : %d\n",pid_t);
    install_handlers();
    while(1);
    return EXIT_SUCCESS;
}
