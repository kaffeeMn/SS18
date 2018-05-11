#include<stdlib.h>
#include<stdio.h>
#include<unistd.h>
#include<sys/types.h>
#include<sys/wait.h>
#include<string.h>

#include <errno.h>

int main(int argc, char **argv){
    int len, z;
    len = 256;
    z = 2;
    int time_to_wait = 5;
    char command[z][len];
    if(argc != 3){
        // time not set
        printf(
            "Submit one additional argument to set the time. Time set to 5.\n"
        );
    }else{
        // args parsing
        int take_arg = 0;
        for(int i=0; i<argc; ++i){
            if(take_arg){
                time_to_wait = atoi(argv[i]);
                break;
            }else if(strncmp("-n", argv[i], 2) == 0){
                take_arg = 1;
            }
        }
        if(time_to_wait<0 || !take_arg){
            // time set impropperly
            time_to_wait = 5;
            printf("Please submit numeric input. Time set to 5.\n");
        }
    }

    // collecting user input
    printf("Zu beobachtenes Programm mit einem Parameter eingeben:");
    if(scanf("%255s %255s",command[0], command[1])<1){
        printf("Fehler bei scanf!\n");
        return 1;
    }
    int status;
    pid_t e_wait, e_waitpid, fork_pid;

    while(1){
        // forking process
        fork_pid = fork();
        e_wait = wait(&status);
        if(e_wait == -1 && errno != ECHILD){
            // wait failed
            perror("wait");
            exit(EXIT_FAILURE);
        }
        if(fork_pid == 0){
            // child process, to execute the command
            execlp(command[0], command[0], command[1], NULL);
            printf("Fehler bei execlp!\n");
            exit(EXIT_FAILURE);
        }else{
            // killing the undead children
            e_waitpid = waitpid(-1, NULL, WNOHANG);
            if(e_waitpid == -1 && errno != ECHILD){
                // waitpid failed
                perror("waitpid");
                exit(EXIT_FAILURE);
            }
            // indicating end of command and sleeping
            printf("----\n");
            sleep(time_to_wait);
        }
    }
    return 1;
}
