#include <stdlib.h>
#include <stdio.h>
#include <string.h>


// char * numberToWord(int num){
//     static struct digits{
//         char A[1];
//         char B[1];

//     };

// }
int len(const char* str){
    int cpt = 0;
    char current_char = str[0];
    
    while(current_char != '\0'){
        current_char = str[cpt];
        cpt++;
    }

    cpt--;
    return cpt;
}

int main(int argc, char *argv[]){
    char name[100];
    char chaine2[] = "salut";

    size_t lenName = 0;
    printf("Veuillez entrer votre nom : ");
    scanf("%s", name);
    lenName = len(name);
    printf("%s %s\n",chaine2, name);
    printf("La taille de votre chaine est %zu", lenName);

    return 0;
}