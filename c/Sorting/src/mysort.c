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

// 冒泡排序
void BubbleSort(int R[],int num)
{
    int i,j,tmp,flag;
    for(i=num;i>=2;i--)
    {
        flag=0;
        for(j=1;j<i;j++)
        {
            if(R[j]>R[j+1])
            {
                tmp=R[j];
                R[j]=R[j+1];
                R[j+1]=tmp;
                flag=1;
            }
        }
        if(flag==0)
        {
            return;
        }
    }
}
void QuickSort(int R[], int l, int r)
{
    int i,j,tmp;
    i=l;
    j=r;
    if(i<j)
    {
        tmp=R[l];
        while(i!=j)
        {
            while(i<j && R[j]>tmp)
            {
                --j;
            }
            if(i<j)
            {
                R[i]=R[j];
                ++i;
            }
            while(i<j && R[i]<tmp)
            {
                ++i;
            }
            if(i<j)
            {
                R[j]=R[i];
                --j;
            }
        }
        R[i]=tmp;
        QuickSort(R,l,i-1);
        QuickSort(R,i+1,r);
    }
}

// 堆排序
void Sift(int R[],int low, int high)
{
    int i=low, j=2*i;
    int tmp=R[i];
    while(j<high)
    {
        if(j<high && R[j]<R[j+1])
        {
            ++j;
        }
        if(tmp<R[j])
        {
            R[i]=R[j];
            i=j;
            j=2*i;
        }
        else
            break;
    }
    R[i]=tmp;
}
void HeapSort(int R[], int num)
{
    int i;
    int tmp;
    for(i=num/2;i>=1;--i)
    {
        Sift(R,i,num);
    }
    for(i=num;i>=2;--i)
    {
        tmp=R[1];
        R[1]=R[i];
        R[i]=tmp;
        Sift(R,1,i-1);
    }
}