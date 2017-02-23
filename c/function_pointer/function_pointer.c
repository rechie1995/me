#include<stdio.h>

typedef void (*pfunc)();
typedef int *PacketTypeNum;
typedef struct PacketTypeItem
{
    pfunc packetfun;
}PacketTypeItem;

PacketTypeItem Type_table[10];

void func1(){
    printf("you \n");
    return;
}

void func2(){
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

int switch_method(int packetnum){
    
    Type_table[3].packetfun = &fun3;
    Type_table[packetnum].packetfun();
    return 0;
}
int main(int *argc, char *argv[])
{
    switch_method(3);
    return 0;
}
