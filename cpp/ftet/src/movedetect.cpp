// 运动物体检测——帧差算法
#include "movedetect.h"
//#include "global.h"

string videopath = "/home/rechie/Videos/test/Main1.MP4";
//string cascadepath = "/home/rechie/Documents/me/cpp/ftet/conf/haarcascade_frontalface_alt2.xml";
double framex = 800.00;

string window_name = "optical flow tracking";
Mat gray;
Mat gray_prev;
vector<Point2f> points[2];
vector<Point2f> initial;
vector<Point2f> features;
int maxCount = 500;
double qLevel = 0.01;
double minDist = 10.0;
vector<uchar> status;
vector<float> err;

string intToString(int number)
{
    stringstream ss;
    ss << number;
    return ss.str();
}

int video()
{
    /* video */
    VideoCapture video(videopath);
    if(!video.isOpened())
    {
        cout << "Video open error!" << endl;
        return -1;
    }
    while(1)
    {
        int frameCount = video.get(CV_CAP_PROP_FRAME_COUNT);
        double FPS = video.get(CV_CAP_PROP_FPS);
        Mat frame;
        Mat temp;
        Mat result;
        Mat result2;
        Mat up;
        Mat down;
        for(int i=0; i<frameCount; i++)
        {
            video >> frame; // 读帧进frame
            if(frame.empty()) // 对帧进行异常检测
            {
                cout << "frame is empty!" << endl;
                destroyAllWindows();
                return 0;
            }
            
            resize(frame,frame,Size(framex, framex*frame.rows/frame.cols),0,0, INTER_LINEAR);
            tracking(frame, result2);
            //up = frame(Rect(0, 40, framex, 10));
            //down = frame(Rect(0, 55, framex, 10));
            //rectangle(frame, Rect(0, 40, framex, 10), Scalar(0, 255, 0),2);
            //rectangle(frame, Rect(0, 55, framex, 10), Scalar(0, 255, 0),2);
            imshow("frame", frame);
            //imshow("up", up);
            //imshow("down", down);
            //imshow("result2", result2);
            if (i == 0) //如果是第一帧（temp还为空）
            {
                result = MoveDetect(frame, frame); //调用MoveDetect()进行运动物体检测，返回值存入result
                temp = frame.clone();
            }
            else
            {
                result = MoveDetect(temp, frame);
                addWeighted(temp,0.8,frame,0.2,0.0,temp);
            }
            imshow("result", result);
            
            if (waitKey(100.0/ FPS) == 27)
            {
                cout << "ESC退出！" << endl;
                destroyAllWindows();
                return 0;
            }
            //temp = frame.clone();
        }
    }
    return 0;
}

Mat MoveDetect(Mat temp, Mat frame)
{
    Mat result = frame.clone();
    //1.将background和frame转为灰度图  
    Mat gray1, gray2;  
    cvtColor(temp, gray1, CV_BGR2GRAY);  
    cvtColor(frame, gray2, CV_BGR2GRAY);  
    //2.将background和frame做差  
    Mat diff;  
    absdiff(gray1, gray2, diff);  
    //imshow("diff", diff);  
    //3.对差值图diff_thresh进行阈值化处理  
    Mat diff_thresh;  
    threshold(diff, diff_thresh, 45, 255, CV_THRESH_BINARY);  
    //imshow("diff_thresh", diff_thresh);
    // 中值滤波
    //medianBlur(diff_thresh, diff_thresh, 5);
    //imshow("medianBlur", diff_thresh);
    //4.腐蚀  
    Mat kernel_erode = getStructuringElement(MORPH_RECT, Size(1, 1));
    Mat kernel_dilate = getStructuringElement(MORPH_RECT, Size(18, 18));
    erode(diff_thresh, diff_thresh, kernel_erode);  
    //imshow("erode", diff_thresh);  
    //5.膨胀  
    dilate(diff_thresh, diff_thresh, kernel_dilate);  
    imshow("dilate", diff_thresh);  
    //6.查找轮廓并绘制轮廓  
    vector<vector<Point> > contours;  
    findContours(diff_thresh, contours, CV_RETR_EXTERNAL, CV_CHAIN_APPROX_NONE);  
    drawContours(result, contours, -1, Scalar(0, 0, 255), 2);//在result上绘制轮廓  
    //7.查找正外接矩形  
    int x0=0, y0=0, w0=0, h0=0;
    vector<Rect> boundRect(contours.size());  
    for (unsigned int i = 0; i < contours.size(); i++)  
    {  
        boundRect[i] = boundingRect(contours[i]);
        
        x0 = boundRect[i].x;
        y0 = boundRect[i].y;
        w0 = boundRect[i].width;
        h0 = boundRect[i].height;
        if(w0>30 && h0>30)
        {
            circle(result, Point(x0+w0/2, y0+h0/2), 3, Scalar(0, 255, 0), 2, 8);
            rectangle(result, boundRect[i], Scalar(0, 255, 0), 2);//在result上绘制正外接矩形
            putText(result,"(" + intToString(x0+w0/2)+","+intToString(y0+h0/2)+")",Point(x0+w0/2+15, y0+h0/2), 1, 1,Scalar(255,0,0),2);
        }
        
          
    }  
    return result;//返回result
}

void detectFaces(Mat &img, CascadeClassifier &cascade, double scale)
{

	const static Scalar colors[] =
	{
		Scalar(255, 0, 0),
		Scalar(255, 128, 0),
		Scalar(255, 255, 0),
		Scalar(0, 255, 0),
		Scalar(0, 128, 255),
		Scalar(0, 255, 255),
		Scalar(0, 0, 255),
		Scalar(255, 0, 255)
	};
	double t = 0;
	vector<Rect> faces;
	Mat gray;
	cvtColor(img, gray, CV_BGR2GRAY);

	Mat smallImg(cvRound(img.rows / scale), cvRound(img.cols / scale), CV_8UC1);
	Size smallImgSize = smallImg.size();

	resize(gray, smallImg, smallImgSize, 0, 0, INTER_LINEAR);
	equalizeHist(smallImg, smallImg);

	t = (double)getTickCount();
	cascade.detectMultiScale(smallImg, faces, 1.1, 2, CV_HAAR_SCALE_IMAGE, Size(30, 30));
	t = (double)getTickCount() - t;
	printf("detection time = %g ms\n", t*1000/getTickFrequency());;
	int i = 0;
	for (vector<Rect>::const_iterator r = faces.begin(); r != faces.end(); r++, i++){
		Scalar color = colors[i%8];
		Rect rect = faces[i];
		printf(
				"face;x=%f&y=%f&width=%f&height=%f\n",
				(float)r->x / smallImgSize.width,
				(float)r->y / smallImgSize.height,
				(float)r->width / smallImgSize.width,
				(float)r->height / smallImgSize.height
				);
		rectangle(img, cvPoint(cvRound(rect.x*scale), cvRound(rect.y*scale)), cvPoint(cvRound((rect.x + rect.width-1)*scale), cvRound((rect.y + rect.height-1)*scale)), color, 3, 8, 0);
	}
	imshow("result2", img);
}

void tracking(Mat frame, Mat output)
{
    cvtColor(frame, gray, CV_BGR2GRAY);
    
    frame.copyTo(output);
    //添加特征点
    if(addNewPoints())
    {
        goodFeaturesToTrack(gray, features, maxCount, qLevel, minDist);
        points[0].insert(points[0].end(), features.begin(),features.end());
        initial.insert(initial.end(), features.begin(), features.end());
    }
    if(gray_prev.empty())
    {
        gray.copyTo(gray_prev);
    }
    calcOpticalFlowPyrLK(gray_prev, gray, points[0], points[1], status, err);
    // 去掉一些不好的特征点
    int k = 0;
    for (size_t i=0; i<points[1].size(); i++)
    {
        if (acceptTrackedPoint(i))
        {
            initial[k] = initial[i];
            points[1][k++] = points[1][i];
        }
    }
    points[1].resize(k);
    initial.resize(k);
    // 显示特征点和运动轨迹
    for (size_t i=0; i<points[1].size(); i++)
    {
        line(output, initial[i], points[1][i], Scalar(0, 0, 255));
        circle(output, points[1][i], 3, Scalar(0, 255, 0), -1);
        if(abs(points[1][i].y - initial[i].y) > 25)
        {
            cout << "有人站起" << endl;
            putText(output,"HAVE",Point(50,60),FONT_HERSHEY_COMPLEX,1,Scalar(255,23,0));
        }
        else
        {
            cout << "无人站起" << endl;
            //putText(output,"NONE",Point(50,60),FONT_HERSHEY_SCRIPT_SIMPLEX,1,Scalar(255,23,0));
        }
    }
    
    // 把当前跟踪结果作为下一此参考
    swap(points[1], points[0]);
    swap(gray_prev, gray);
    imshow(window_name, output);
}

bool addNewPoints()
{
    return points[0].size() <= 10;
}

//决定哪些跟踪点被接受
bool acceptTrackedPoint(int i)
{
    return status[i] && ((abs(points[0][i].x - points[1][i].x) + abs(points[0][i].y - points[1][i].y)) > 2);
    //return status[i] && (abs(points[0][i].x - points[1][i].x) < 10) && (abs(points[0][i].y - points[1][i].y) > 2);
}