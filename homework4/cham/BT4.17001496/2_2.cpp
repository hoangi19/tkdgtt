/*
{1,2,3} => {1,2} {1,3} {2,3}
*/
#include<iostream>
using namespace std;
int n, k;
void printN(int x[]){
    for(int i = 1; i <= k; i++){
        cout << x[i] << " ";
    }
}
void Try(int i, int x[]){
    for(int j = x[i-1] + 1; j <= n-k+i; j++){
        x[i] = j;
        if(i == k){
            printN(x);
            cout << endl;
        }else{
            Try(i+1, x);
        }
    }
}
int main(){
    cout << "Nhap n: ";
    cin >> n;
    cout << "Nhap k: ";
    cin >> k;
    cout << "To hop chap k cua n: " << endl;
    int x[k];
    x[0] = 0;
    Try(1, x);
}