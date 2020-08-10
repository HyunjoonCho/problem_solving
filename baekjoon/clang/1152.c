int main(){
    char c;
    short blank = 0;
    int cnt = 0;
    
    // okay with empty input, " ", " ~~", "~~ ", " ~~ ", "~~" then what?
    if(scanf("%c", &c) != -1){ 
        if(c==' ') blank = 1;
        else cnt++;

        while(scanf("%c", &c) != -1){
            if(c==' ') blank = 1;
            else if(blank==1){
                blank = 0; 
                cnt++;
            }
        }
    }
    printf("%d", cnt);
}