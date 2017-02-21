#include"stdio.h"
#include"stdarg.h"
void simple_va_fun(int start, ...)
{
    va_list arg_ptr;
    int nArgValue = start;
    int nArgCout = 0;  //可变参数的数目
    va_start(arg_ptr, start);  //以固定参数的地址为起点确定变参的内存起始地址。
    do
    {
        ++nArgCout;
        printf("the %dth arg: %d.\n", nArgCout, nArgValue);  //输出各参数的值
        nArgValue = va_arg(arg_ptr,int);  //得到下一个可变参数的值
    }while(nArgValue != -1);
    return;
}

int main(int argc, char* argv[])
{
    simple_va_fun(100, -1);
    simple_va_fun(100, 200, -1);
    return 0;
}
