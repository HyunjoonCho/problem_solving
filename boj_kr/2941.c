//m1: read two -> what if c1 c2 != but c2 c3 == ?
//m2: read one by one -> still! c2 is abandoned Then, how?
//m3: keep track of prev char! maybe two...? No! simple flag or enum!
// č	c=
// ć	c-
// dž	dz=
// đ	d-
// lj	lj
// nj	nj
// š	s=
// ž	z=

enum Croatian
{
    None = 0,
    C,
    D,
    DZ,
    L,
    N,
    S,
    Z
}; 
int getCroatian(char c){
    if(c=='c') return 1;
    else if(c=='d') return 2;
    else if(c=='l') return 4;
    else if(c=='n') return 5;
    else if(c=='s') return 6;
    else if(c=='z') return 7;
    return 0;    
}
int main(){
    char c;
    int cnt = 0;
    enum Croatian croa = None;

    while (1)
    {
        if (scanf("%c", &c) == -1 || c == '\n' || c == '\0'){
            if(croa == DZ) cnt += 2;
            else if(croa != None) cnt++; // incr cnt when croatian not matched
            break;
        }
        if(croa == None){
            if((croa = getCroatian(c))==0) cnt++;
        } else{
            if(croa == C){
                if(c=='=' || c=='-'){
                    croa = None;
                    cnt++;
                } else{
                    if((croa = getCroatian(c))==0) cnt += 2;    // may use goto for those
                    else cnt++; // if croa != None, consider possibility
                }
            } else if(croa == D){
                if(c=='-'){
                    croa = None;
                    cnt++;
                } else if(c=='z'){
                    croa = DZ;
                } else{
                    if((croa = getCroatian(c))==0) cnt += 2;     
                    else cnt++;           
                }
            } else if(croa == DZ){
                if(c=='='){
                    croa = None;
                    cnt++;
                } else{
                    if((croa = getCroatian(c))==0) cnt += 3;     
                    else cnt += 2;           
                }
            } else if(croa == L){
                if(c=='j'){
                    croa = None;
                    cnt++;
                } else{
                    if((croa = getCroatian(c))==0) cnt += 2;     
                    else cnt++;           
                }
            } else if(croa == N){
                if(c=='j'){
                    croa = None;
                    cnt++;
                } else{
                    if((croa = getCroatian(c))==0) cnt += 2;     
                    else cnt++;           
                }
            } else if(croa == S){
                if(c=='='){
                    croa = None;
                    cnt++;
                } else{
                    if((croa = getCroatian(c))==0) cnt += 2; 
                    else cnt++; 
                }
            } else if(croa == Z){
                if(c=='='){
                    croa = None;
                    cnt++;
                } else{
                    if((croa = getCroatian(c))==0) cnt += 2;     
                    else cnt++;           
                }
            }
        }

    }
    printf("%d", cnt);
}