#include "movedetect.h"
//#include "global.h"

static void helpinfo()
{
    cout <<"当前使用的OpenCV版本为："<< CV_VERSION << endl;
}

int main(int argc, char const *argv[])
{
    //string videofilepath = "/home/rechie/Videos/test/Main1.MP4";
    //configread();
    helpinfo();
    video();
}