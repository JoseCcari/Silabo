#include <iostream>
using namespace std;

int main(){
    int in , q,e;
    cin>>in>>q;
    while (cin>> in>>q){
        if(in==0 && q==0)   
            break;
        if ((in>=0 && in<=10000) && (q>=0 && q<=10000)){
            for (int i=0; i<in ;i++){
                cin>>e;
                if(e%q==0){
                    if (e%2==0 )
                }
            }

        }

    return 0;
}

