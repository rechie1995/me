#include <stdio.h>
#include <stdlib.h>

#include "mysort.h"

#define N 100010

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

            case 3:
                BubbleSort(R,len);
                break;

            case 4:
                QuickSort(R,1,len);
                break;

            case 5:
                HeapSort(R,len);
                break;

            default:
                puts("程序错误！");
                return 0;
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
    return 0;
    
}