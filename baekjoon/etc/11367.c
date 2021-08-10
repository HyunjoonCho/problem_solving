#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(n){
    scanf("%d\n", &n);
    char line[11] = {0};
    char** names = malloc(n*sizeof(char*));
    int* scores = malloc(n*sizeof(int));    // variable size array -> malloc
    for(int i=0; i<n; i++){
        names[i] = malloc(11);  // only mem for ptr is allocated, not actual string
        scanf("%s", line);
    	memcpy(names[i], &line, strlen(line)+1);
        scanf("%s", line);
        scores[i] = atoi(line);
    }
    int score;
    for(int i=0; i<n; i++){
        printf("%s ", names[i]);
        score = scores[i];
        // printf("%d ", score);
        if(score>96) printf("A+\n");
        else if(score>89) printf("A\n");
        else if(score>86) printf("B+\n");
        else if(score>79) printf("B\n");
        else if(score>76) printf("C+\n");
        else if(score>69) printf("C\n");
        else if(score>66) printf("D+\n");
        else if(score>59) printf("D\n");
        else printf("F\n");
        free(names[i]);
    }
    free(names);
    free(scores);
}