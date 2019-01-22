#include <opencv2/opencv.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/core/core.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/video/video.hpp>
#include "opencv2/objdetect/objdetect.hpp"

#include <iostream>
#include <cstdio>
using namespace cv;
using namespace std;

int opencamera();
int video();
Mat MoveDetect(Mat temp, Mat frame);
void detectFaces(Mat &img, CascadeClassifier &cascade, double scale);
void tracking(Mat frame, Mat output);
bool addNewPoints();
bool acceptTrackedPoint(int i);