#include<iostream>
using namespace std;
int k;
void printN(int x[]){
    for(int i = 1; i <= k; i++){
        cout << x[i] << " ";
    }
}
void Try(int i, int x[]){
    for(int j = 0; j <= 1; j++){
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
    cout << "Length of binary string: " << endl;
    cin >> k;
    int x[20];
    x[0] = 0;
    if(k >= 1)
        Try(1, x);
    else
        cout << "length = 0";
}