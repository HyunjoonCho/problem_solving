int main(){
    char c;
    int first [26]; 
    int idx = 0;
    for(int i=0; i<26; i++) first[i] = -1;
    while(1){
        scanf("%c", &c);
        if(c=='\n') break;
        if(first[c-97] == -1) first[c-97] = idx; 
        // 'a' == 97 in ASCII
        // '0' == 48 in ASCII
        idx++;
    }
    for(int i=0; i<26; i++) printf("%d ", first[i]);
}