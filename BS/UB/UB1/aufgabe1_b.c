#include<stdlib.h>
#include<stdio.h>
#include<unistd.h>

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
    execlp(command[0], command[0], command[1], NULL);
    printf("Fehler bei execlp!\n");
    return 1;
}
