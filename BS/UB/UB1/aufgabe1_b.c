#include<stdlib.h>
#include<stdio.h>
#include<unistd.h>

int main(){
    int len = 256;
    int n = 2;
    char command[n][len];
    printf("Zu beobachtenes Programm mit einem Parameter eingeben: ");
    if(scanf("%255s %255s",command[0], command[1])<1){
        printf("Fehler bei scanf!\n");
        return 1;
    }
    if(execlp(NULL, command[0], command[0])){
        printf("Fehler bei execlp!\n");
        return 1;
    }
    return 0;
}
