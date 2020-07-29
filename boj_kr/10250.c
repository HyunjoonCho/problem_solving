
int main(){
    int T;
    scanf("%d", &T);
    int h, w, n, room; // room no = YYXX format
    for(int i=0; i<T; i++){
        scanf("%d %d %d", &h, &w, &n);
        /*
         * if(n/h<9) printf("%d0%d\n", n%h, n/h+1); <- sets blank not zero
         * else printf("%d%d\n", n%h, n/h+1);
         */
        if(n%h==0) room = h*100 + n/h; 
        // if n%h==0, YY should be h itself and XX should be n/h
        else room = n%h*100 + n/h + 1;
        printf("%d\n", room);
    }
}