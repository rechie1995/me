#include"stdio.h"
#include"stdarg.h"
#include"string.h"
typedef struct EnvArgs
{
    char a;
    char b;
    char c;
}EnvArgs;

EnvArgs *envArgs;



void simple_va_fun0(int start, ...)
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

void simple_va_fun1(char *msg, ...)
{
    va_list arg_ptr;
    char *nArgValue = msg;
    int nArgCout = 0;
    va_start(arg_ptr, msg);

    while(1)
    {
        if (strcmp(nArgValue,"/0") == 0)
            break;
        printf("Parameter %d is %s \n", nArgCout, nArgValue);
        nArgCout++;
        nArgValue = va_arg(arg_ptr, char *);
    }
    va_end(arg_ptr);
    return;
}

int main(int argc, char* argv[])
{
    simple_va_fun0(10, -1);
    simple_va_fun0(100, 200, -1);
    simple_va_fun1("DEMO", "2333", "you", "are", "hero", "/0");
    return 0;
}
