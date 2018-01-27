#include <stdio.h>
#include <stdlib.h>

#define N 100010

// 插入排序
void InsertSort(int R[], int n)
{
    int i,j,tmp;
    for(i=2;i<=n;i++)
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
void SelectSort(int R[], int n)
{
    int i,j,k,tmp;
    for(i=1;i<=n;i++)
    {
        k=i;
        for(j=i+1;j<=n;j++)
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

int main(int argc, char * argv[])
{
    int len,i,sort;
    int R[N];
        
    puts("欢迎来到排序算法演示程序");    
    while(1)
    {
        printf("请输入需要排序的值的数量：");
        if(scanf("%d", &len) == EOF)
        {
            break;
        }
        printf("请输入需要排序的%d个数字：",len);
        for(i=1;i<=len;i++)
        {
            scanf("%d",&R[i]);
        }
        
        printf("请输入想使用的算法：");
        scanf("%d", &sort);
        switch(sort)
        {
            case 1:
            InsertSort(R,len);
            break;

            case 2:
            SelectSort(R,len);
            break;

            default:
            break;
        }
        printf("排序结果为：");
        for(i=1;i<=len;i++)
        {
            printf("%d ",R[i]);
        }
        puts("");
        break;
    }
    
}