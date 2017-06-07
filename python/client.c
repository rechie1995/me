#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <sys/time.h>
#include <unistd.h>
#include <netinet/in.h>
#include <arpa/inet.h>


int main(int argc, char ** argv)
{
    struct sockaddr_in addr_ser;
    int addr_len = 0;

    int fd = socket(AF_INET, SOCK_STREAM, 0);
    if (fd < 0) {
        printf("err:%s", strerror(errno));
        return -1;
    }
    
    memset(&addr_ser, 0, sizeof(struct sockaddr_in));
    addr_ser.sin_family = AF_INET;
    addr_ser.sin_port = htons(atoi(argv[2]));
    addr_ser.sin_addr.s_addr = (inet_addr(argv[1]));
    addr_len = sizeof(struct sockaddr);

    printf("ip : %s, port : %s\n", argv[1], argv[2]);
    printf("ip : %#x, port : %d\n", inet_addr(argv[1]), atoi(argv[2]));

    char * a = inet_ntoa(addr_ser.sin_addr);
    printf("ip : %s\n", a);

    int con_ret = connect(fd, &addr_ser, (socklen_t)addr_len);
    printf("con_ret = %d\n", con_ret);
    if (con_ret<0) {
        printf("err : %s\n", strerror(errno));
        close(fd);
    }
    
    while(1) {
        fd_set r_set;

        struct timeval timeout;
        timeout.tv_sec = 2;
        timeout.tv_usec = 500;

        FD_SET(fd, &r_set);
        int ret = select(fd+1, &r_set, NULL, NULL, &timeout);
        if (ret < 0) {
            printf(" err : %s\n", strerror(errno));
            break;
        } if (ret == 0) {
            printf(" timeout !!!\n");
            continue;
        } else {
            if (FD_ISSET(fd, &r_set)) {
                int length = 0;
                char * data = (char*)malloc(640*480*2*sizeof(char));
                while (length != 640*480*2) {
                    length = recv(fd, data, 640*480*2, 0);
                    printf("recv %d\n", length);
                }
                //int index = 0;
                //for (index=0; index<length; index++) {
                //    printf("%d ", data[index]);
                //}
                free(data);
            }
        }
    }

    close(fd);


    

    return 0;
}

