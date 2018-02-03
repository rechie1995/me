// mysort.c
// Create by rechie on 2018/02/03.
//

#include "mysort.h"

// 插入排序
void InsertSort(int R[], int num)
{
    int i,j,tmp;
    for(i=2;i<=num;i++)
    {
        tmp=R[i];
        j=i-1;
        while(j>=1 && R[j]>tmp)
        {
            R[j+1]=R[j];
            j--;
        }
        R[j+1]=tmp;
    }
}

// 选择排序
void SelectSort(int R[], int num)
{
    int i,j,k,tmp;
    for(i=1;i<=num;i++)
    {
        k=i;
        for(j=i+1;j<=num;j++)
        {
            if(R[j]<R[k])
            {
                k=j;
            }
        }
        tmp=R[i];
        R[i]=R[k];
        R[k]=tmp;
    }
}