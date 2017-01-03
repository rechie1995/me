// 十进制转十六进制
// author:rechie
#include "stdio.h"
#include "stdlib.h"
#define MAX 50

int main()
{
	int n, a[MAX], i = 0, sign = 0;
	//system("clear");
	printf("Please input the decimal num:");
	scanf("%d", &n);

	if(n == 0)
	{
		printf("HEX= %d", n);
		printf("\n\n\nPress any key to exit...\n\n");
		getchar();
		exit(0);
	}
	if(n < 0)
	{
		sign=1;
		n=-n;
	}
	while(n!=0)
	{
		a[i++]=n%16;
		n=n/16;
	}
	printf("HEX=%cx",sign?'-':' ');
	for(; i>0; i--)
	{
		switch(a[i-1])
		{
			case 10: printf("a"); break;
			case 11: printf("b"); break;
			case 12: printf("c"); break;
			case 13: printf("d"); break;
			case 14: printf("e"); break;
			case 15: printf("f"); break;
			default: printf("%d", a[i-1]);
		}
	}
	printf("\n\nPress any key to exit...\n\n");
	getchar();
}
