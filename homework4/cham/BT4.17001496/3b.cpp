#include<iostream>
#include<algorithm>
using namespace std;
int n;  // so loai to tien trong may ATM <= 20
int S;  // so tien can tra
int t[20];    //danh sach menh gia tien
int sum = 0;
int max = 20;
int tmax;
int c, cbest;   //so to tien hien tai, so to tien tot nhat hien tai
void swap(int *xp, int *yp)  
{  
    int temp = *xp;  
    *xp = *yp;  
    *yp = temp;  
}  
  
// A function to implement bubble sort  
void bubbleSort()  
{  
    int i, j;  
    for (i = 0; i < n-1; i++)      
      
    // Last i elements are already in place  
    for (j = 0; j < n-i-1; j++)  
        if (t[j] > t[j+1])  
            swap(&t[j], &t[j+1]);  
}  
void update(){
    if(c < cbest){
        cbest = c;
    }
}
void Init(){
    c = 0;
    cbest = INT16_MAX;
    sum = 0;
    tmax = t[n-1];
}
void Atm(){
    if((int)(c + (S-sum)/tmax) >= cbest) return;
    if(S==sum){
            update();
            return;
    }
    if(S < sum){
        return;
    }
    for(int j = 0; j < n; j++){
        sum = sum + t[j];
        c = c + 1;
        Atm();
        sum = sum - t[j];
        c = c - 1;
    }
}
int main(){
    n = 3;
    S = 20;
    for(int i = 0; i < 3; i++){
        t[i] = i+1;
    }
    bubbleSort();
    Init();
    Atm();
    cout << cbest;
}
