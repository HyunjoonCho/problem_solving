/*
exceptions: n=1 -> 1, n = 2 -> k+1

10 = 1*3 + 2*2 + 3*1 //2-3
70 = 1* + 2 ... -> NOPE //3-5

1 5 15 35 70 126 ...
1 4 10 20 35 056 ...
1 3 06 10 15 021 ...
1 2 03 04 05 006 ...

-> better to create an array? 
*/
int main(){
    int T;
    scanf("%d", &T);
    int k, n;
    int v = 0;

    for(int i=0; i<T; i++){
        scanf("%d", &k);
        scanf("%d", &n);
        if(n==1) v = 1;
        else if(n==2) v = k+2;
        else{
            int** floors = malloc((k+1)*sizeof(int*));
            for(int j=0; j<k+1; j++) floors[j] = malloc(n*sizeof(int));
            for(int p=0; p<k+1; p++){
                for(int q=0; q<n; q++){
                    if(p==0) floors[p][q] = q+1;
                    else if(q==0) floors[p][q] = 1;
                    else floors[p][q] = floors[p][q-1] + floors[p-1][q];
                }
            }
            v = floors[k][n-1];
            for(int j=0; j<k+1; j++) free(floors[j]);
            free(floors);
        }
        printf("%d\n", v);
    }
}