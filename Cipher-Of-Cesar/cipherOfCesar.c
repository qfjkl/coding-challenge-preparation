#include <stdlib.h>
#include <stdio.h>
#include <string.h>

char * cipher(char *msg, int k){
    
    typedef struct{
        int start;
        int end;
    } interval;

    int cpt = 0;
    interval intervals[3];

    intervals[0].start = 97;
    intervals[0].end = 122;
    intervals[1].start = 65;
    intervals[1].end = 90;
    intervals[2].start = 48;
    intervals[2].end = 57;

    do{

        if((msg[cpt] >= intervals[0].start && msg[cpt] <= intervals[0].end)){ // char between [a-z]
            msg[cpt] %= intervals[0].start;
        } else if(msg[cpt] >= intervals[1].start && msg[cpt] <= intervals[1].end){ // char between [A-Z]
            msg[cpt] %= intervals[1].start;
        } else if(msg[cpt] >= intervals[2].start && msg[cpt] <= intervals[2].end){ // char between [0-9]
            msg[cpt] %= intervals[2].start;
        }

        if((msg[cpt] >= intervals[0].start && msg[cpt] <= intervals[0].end) ||
            (msg[cpt] >= intervals[1].start && msg[cpt] <= intervals[1].end) || 
            (msg[cpt] >= intervals[2].start && msg[cpt] <= intervals[2].end)){
        
            msg[cpt] = (msg[cpt] + k) % 62;

            if(msg[cpt] <= 25){
                msg[cpt] %= 25;
                msg[cpt] += intervals[0].start;
            } else if(msg[cpt] > 25 && msg[cpt] <= 51){
                msg[cpt] %= 25;
                msg[cpt] += intervals[1].start;
            } else{
                msg[cpt] %= 9;
                msg[cpt] += intervals[2].start;
            }
        }
        
        cpt++;
    }while(msg[cpt] != '\0');

    return msg;
}

int main(int argc, char *argv[]){

    char msg[100];
    char msg2[100];
    char response[100] = "yes";
    char default_value[100] = "yes";
    int K;
    
    while(strcmp(response, default_value) == 0){

        printf("Enter The Value Of K (0, 2^32-1) : ");
        scanf("%d", &K);

        printf("Enter The Message To Encrypt : ");
        scanf("%s", msg);
        
        strcpy(msg2, msg);
        cipher(msg, K);

        printf("%s => %s\n\n", msg2, msg);
        printf("Did You Want To Continue To Encrypt Message? (yes | no) : ");
        scanf("%s", response);
        printf("\n\n");
        // printf("%lu\n", strlen(result));
    }


    return 0;
}