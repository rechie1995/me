/** 
 * @file main.cpp
 * @brief 程序的主函数
 * @author rechie
 * @date 2019-01-28
 * 
 * 主函数是程序的入口
 * 运行于程序启动时
 * 
 */ 

#include<iostream>
#include<thread>
#include<mutex>
#include<condition_variable>
#include<opencv2/opencv.hpp>

// 命名空间
using namespace std;
using namespace cv;

Mat frame;
Mat image_catch;
Mat display_mat_origin;
Mat display_mat_process;
mutex m;
condition_variable thcv;
vector<Mat> v_frames;
double framex = 800.00;
string filename = "/home/rechie/Videos/Westworld.S02E02.mp4";

volatile bool thread_all_exit = false;

void processThread()
{
    Mat img;
    while(1)
    {
        unique_lock<mutex> lck(m);
        thcv.wait(lck);
        cout << "this is process thread! " << "\n" << endl;
        if(!image_catch.empty())
        {
            img = image_catch.clone();
            if(img.channels()==3)
            {
                cvtColor(img, img, CV_BGR2GRAY);
            }
            Canny(img, img, 100, 200);
            threshold(img, img, 128, 255, THRESH_BINARY_INV);
            display_mat_process = img.clone();
            if(thread_all_exit)
            {
                break;
            }
        }
    }
}

void imshowThread()
{
    int n = 0 ;
    while(1)
    {
        unique_lock<mutex> lck(m);
        thcv.wait(lck);
        cout << "this is show thread! " << n << "\n" << endl;
        if(!display_mat_origin.empty())
        {
            imshow("origin", display_mat_origin);
            
        }
        if(!display_mat_process.empty())
        {
            imshow("process", display_mat_process);
        }
        const char key = (char)waitKey(30);
        if(key == 27 || key == 'q')
        {
        cout << "退出视频" << endl;
        thread_all_exit = true;
        break;
        }
        n++;
    }
}

int main(int argc, char const *argv[])
{
    thread *th1 = new thread(imshowThread);
    thread *th2 = new thread(processThread);
    th1->detach();
    th2->detach();
    Mat frame;
    VideoCapture cap;
    cap.open(filename);
    if (!cap.isOpened())
    {
        lock_guard<mutex> guard(m);
        cerr << "ERROR! Unable to open capture !\n";
        thread_all_exit = true;
        return -1;
    }
    int i = 0;
    while(1)
    {
        cap.read(frame);
        if(frame.empty())
        {
            lock_guard<mutex> guard(m);
            cerr << "ERROR! blank frame grabbed\n";
            cap.release();
            thread_all_exit = true;
            break;
        }
        resize(frame, frame, Size(320, 240), 0, 0, CV_INTER_LINEAR);
        unique_lock<mutex> lck(m);
        cout << "catch frame: " << i << endl;
        image_catch = frame.clone();
        display_mat_origin = frame.clone();
        thcv.notify_one();
        i++;
        if(thread_all_exit)
        {
            cap.release();
            destroyWindow("frame");
            break;
        }
    }
    cap.release();
    return 0;
}
