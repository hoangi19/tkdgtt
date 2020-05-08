#include<iostream>
using namespace std;
int maxE = 100;
int maxC = 100 * 100;
 
int C[100][100];
int X[101];
int T[100];
 
int BestWay[101];
 
int FREE[100];
 
int minSpending;
int N;
 
 
void Enter ()
{  
    int i,j,k;
    cout << " So thanh pho: " ;
    cin >> N;       
    for ( i = 1; i <= N; i++ )
    {
        cout << "Nhap hang thu [" << i << "]" << endl;
        for ( j = 1; j <= N; j++ )
        {
            cin >> C[i][j];
        }
    }
    cout << "bang chi phi giua cac thanh pho:" << endl;
    for ( i = 1; i <= N; i++ )
    {
        for ( j = 1; j <= N; j++ )
        {
            if(i == j) C[i][j] = 0;
            cout << C[i][j] << " ";
        }
        cout << endl;
    }
   
}
void InI()
{
    for ( int i = 1; i <= N; i++ )
    {
        FREE[i] = 1; // chua di qua
    }
 
    FREE[1] = 0;
    X[1] = 1;
    T[1] = 0;
 
    minSpending = maxC;
}
 
void PRINT()
{
       if (minSpending == maxC)
       {
            cout << "NO SOLUTION ";
       }
       else
       {
            for (int i = 1; i <= N; i++)
            {
               cout << BestWay[i] << "->";
            }
            cout << BestWay[1] << endl;
            cout << "Chi phi be nhat : " << minSpending;
       }
}
 
void BACKTRACK (int i)
{
    for (int j = 2; j <= N; j++)
    {
        if (FREE[j])
        {
            X[i] = j;
            T[i] = T[i-1] + C[X[i-1]][j];
            if (( T[i] + C[i][1]) < minSpending ) // chi phi tai thanh phan i + chi phi tu i ve tp 1 < bestcost
            {
                if ( i < N )
                {
                    FREE[j] = 0;
                    BACKTRACK ( i + 1 );
                    FREE[j] = 1;
                }
                else
                {
                    for ( int var = 1; var <= N; var++ )
                    {
                        BestWay[var] = X[var];
                    }
                    minSpending = T[N] + C[X[N]][1];               
                }
            }
           }
    }
}
 
int main()
{
    Enter();
    InI();
    BACKTRACK(2);
    PRINT();
    return 0;
}