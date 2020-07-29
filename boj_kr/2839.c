int getPacks(int N){
    if(N<0) return -1;
    if(N%5==0) return N/5;
    if(N==3) return 1;
    if(N==1 || N==2) return -1;
    int a;
    a = getPacks(N-5) + 1;
    if(a!=0) return a;
    a = getPacks(N-3) + 1;
    if(a==0) return -1;
    else return a;
    /* Prev approach
     * int a, b;
     * a = getPacks(N-5) + 1;
     * b = getPacks(N-3) + 1;
     * if(a==0 && b==0) return -1;
     * if(a>b) return a;
     * else return b;
     * double recursion -> as it goes down, squared recursion! TIME OUT
     */
    // How about DP? maybe Knapsack
}
int main(){
    int N;
    scanf("%d", &N);
    printf("%d", getPacks(N));
}