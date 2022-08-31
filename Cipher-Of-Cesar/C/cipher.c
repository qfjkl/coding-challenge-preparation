#include "cipher.h"

void shift(char *character, int lenghtOfCharacter, int start){
    *character %= lenghtOfCharacter;
    *character += start;
}

char * cipher(char *msg, int k){

    typedef struct{
        int start;
        int end;
    } interval;

    int cpt = 0;
    int witness = 0;

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
            witness = 1;
        } else if(msg[cpt] >= intervals[1].start && msg[cpt] <= intervals[1].end){ // char between [A-Z]
            msg[cpt] %= intervals[1].start;
            msg[cpt] += NUMBER_LETTER;
            witness = 1;
        } else if(msg[cpt] >= intervals[2].start && msg[cpt] <= intervals[2].end){ // char between [0-9]
            msg[cpt] %= intervals[2].start;
            msg[cpt] += NUMBER_LETTER * 2;
            witness = 1;
        }

        if(witness == 1){ // if char belongs [a-zA-Z0-9]
            msg[cpt] = (msg[cpt] + k) % ALL_CHARS_NUMBER;
            if(msg[cpt] <= 26){ // for lower case char 
                shift(&msg[cpt], NUMBER_LETTER, intervals[0].start);       
            } else if(msg[cpt] > 26 && msg[cpt] <= 52){ // for upper case char
                shift(&msg[cpt], NUMBER_LETTER, intervals[1].start);       
            } else{ // for digits
                shift(&msg[cpt], NUMBER_DIGITS, intervals[2].start);       
            }
        }

        witness = 0;
        cpt++;
    }while(msg[cpt] != '\0');

    return msg;
}
