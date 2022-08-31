#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include "cipherOfCesar.h"


int main(int argc, char *argv[]){

    char msg1[100];
    char msg0[100];
    char response[100] = "yes";

    typedef union{
        char toContinue[100];
        char toStop[100];
    } responses;

    responses default_response[2];

    strcpy(default_response[0].toContinue, "yes");
    strcpy(default_response[1].toContinue, "y");

    int K;

    while(strcmp(response, RESPONSE1) == 0 || strcmp(response, RESPONSE2) == 0){

        printf("Enter The Value Of K (0, 2^32-1) : ");
        scanf("%d", &K);

        printf("Enter The Message To Encrypt : ");
        scanf("%s", msg1);
        
        strcpy(msg0, msg1);
        cipher(msg1, K);

        printf("%s => %s\n\n", msg0, msg1);

        printf("Do You Want To Continue To Encrypt Message? (yes | no) : ");
        scanf("%s", response);
        printf("\n");
    }


    return 0;
}
