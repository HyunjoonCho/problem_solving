char isSelfNum(int n){
    if(n<11 && n%2 == 1) return 1;

    // ab + a + b = 11a + 2b where b is one-digit number
    // 18? 11 + 7 X 18 O
    if(n>10 && n<101 && n%11 == 9) return 1;

    // abc + a + b + c = 101a + 11b + 2c
    // 209? 202 + 7 X 101 + 88 + 20 X 
    // 220? 202 + 18 O 
    // 207? 101 + 88 + 18 O -> three-digit num % 101 == 7 or 9? NO maybe...

    // abcd + a + b + c + d = 1001a + 101b + 11c + 2d
    // 1006? 1001 + 5 X 909 + 88 + 9 X  909 + 77 + 20 X 1107? 1001 + 88 + 18 O
    // 1008? 1001 + 7 X 909 + 99 O 1109? 1001 + 101 + 7 X 1001 + 88 + 20 X

    int a, b;
    a = n/1001;
    b = n/101>9? 9:n/101;
    for(int i=a; i>=0; i--){
        for(int j=b; j>=0; j--){
            for(int k=9; k>=0; k--){
                for(int l=9; l>=0; l--)
                    if((1001*i + 101*j + 11*k + 2*l) == n) return 0;
            }
        }
    }

    return 1;
}
int main(){
    for(int i=1; i<10000; i++){
        if(isSelfNum(i)) printf("%d\n", i);
    }
}