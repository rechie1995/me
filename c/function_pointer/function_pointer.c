#include<stdio.h>

typedef void (*pfunc)();
typedef int *PacketTypeNum;
typedef struct PacketTypeItem
{
    pfunc packetfun;
}PacketTypeItem;

void fun1(){
    printf("you \n");
    return;
}

void fun2(){
    printf("are \n");
    return;
}

void fun3(){
    //int a = 1;
    //int b = 2;
    printf("this is func3.\n");
    return;
}

void fun4(){
    printf("what\n");
    return;
}

void fun8(){
    printf("This is func8. \n");
    return;
}


PacketTypeItem Type_table[10]={
    {&fun1},
    {&fun2},
    {&fun3},
    {&fun4},
    {&fun8}
};



int switch_method(int packetnum){
    
    //Type_table[3].packetfun = &fun3;
    Type_table[packetnum-1].packetfun();
    return 0;
}
int main(int *argc, char *argv[])
{
    switch_method(3);
    switch_method(1);
    return 0;
}
