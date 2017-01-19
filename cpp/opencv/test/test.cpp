#include <opencv/cv.h>
#include <opencv/highgui.h>
#include <opencv/cxcore.h>
int main(int argc, char*argv[]){
	IplImage*src = cvLoadImage("/home/rechie/Pictures/6.jpg", -1);
	cvNamedWindow("show_image", 0);
	cvShowImage("show_image", src);
	cvWaitKey(0);
	cvReleaseImage(&src);
	cvDestroyWindow("show_image");
	return 0;

}
