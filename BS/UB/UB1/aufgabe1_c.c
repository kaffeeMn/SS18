#include<stdlib.h>
#include<stdio.h>
#include<unistd.h>
#include<sys/types.h>
#include<sys/wait.h>

#include <errno.h>

int main(){
    int len, z;
    len = 256;
    z = 2;
    char command[z][len];
    printf("Zu beobachtenes Programm mit einem Parameter eingeben:");
    if(scanf("%255s %255s",command[0], command[1])<1){
        printf("Fehler bei scanf!\n");
        return 1;
    }
    int status;
    pid_t e_wait, e_waitpid, fork_pid;
    while(1){
        fork_pid = fork();
        e_wait = wait(&status);
        if(e_wait == -1 && errno != ECHILD){
            perror("wait");
            exit(EXIT_FAILURE);
        }
        if(fork_pid == 0){
            execlp(command[0], command[0], command[1], NULL);
            printf("Fehler bei execlp!\n");
            exit(EXIT_FAILURE);
        }else{
            e_waitpid = waitpid(-1, NULL, WNOHANG);
            if(e_waitpid == -1 && errno != ECHILD){
                perror("waitpid");
                exit(EXIT_FAILURE);
            }
            printf("----\n");
            sleep(5);
        }
    }
    return 1;
}
