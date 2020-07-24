int main(){
    int num[26] = {0};
    char c;
    while(scanf("%c", &c) != -1){ //use EOF instead of '\n' or '\0'
        if(c>96) num[c-97]++;
        else num[c-65]++;
    }
    int idx = 0;
    int dup = 0; // 0: only one, 1: mult
    for(int i=1; i<26; i++){
        if(num[i]==num[idx]) dup = 1;
        if(num[i]>num[idx]){ // if this comes first, changed idx satisfies upper condition
            idx = i;
            dup = 0;
        }
    }
    if(dup == 1) printf("?");
    else printf("%c", idx+65);
}