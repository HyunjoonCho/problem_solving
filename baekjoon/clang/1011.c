int main(){
    int T;
    scanf("%d", &T);
    double x, y, dist;
    int idx;
    for(int i=0; i<T; i++){
        scanf("%lf %lf", &x, &y); // NOT %f but %lf!
        dist = y - x;
        idx = sqrt(dist);
        // printf("dist %lf idx %lf\n",dist, idx);
        if(idx*idx == dist) idx = idx*2 - 1;
        else if(dist < idx * (idx+1) + 1) idx = idx*2; 
        else idx = idx*2 + 1;
        /*
        while(1){
            if(idx%2==0){
                // bound = (idx/2+1)*(idx/2)+1; // 2* (idx/2)*(idx/2 + 1)/2 + 1
                bound += idx/2;
                if(dist<bound) break;
            } else{
                // bound = (idx/2+1)*(idx/2)+idx/2+2; // 2*(idx/2)*(idx/2 + 1)/2 + idx/2+1 + 1
                bound += idx/2 + 1; 
                if(dist<bound) break;
            }
            idx++;
        }
        */
        printf("%d\n",idx);
    }
}
// 1 1 ->1
// 2 11 ->2
// "4" 121 ->3
// 6 1221->4
// "9" 12321
// 12 123321
// "16" 1234321
// 20
// "25"