#include<iostream>
using namespace std;
int n, k;
int max = 20;
int x[20];
int d[20];
void printSolution(int x[]){
    for(int i = 1; i <= k; i++){
        cout << x[i] << " ";
    }
}
void Chl(int i){
    for(int j = 1; j <= n; j++){
        if(d[j] == 0){
            x[i] = j;
            d[j] = 1;
            if(i == k){
                printSolution(x);
                cout << endl;
            }else{
                Chl(i+1);
            }
            d[j] = 0;
        }
    }
}
int main(){
    cout << "Nhap n: " << endl;
    cin >> n;
    cout << "Nhap k: " << endl;
    cin >> k;
    Chl(1);
} 