#include<opencv2/opencv.hpp>
#include<math.h>

using namespace std;
using namespace cv;

int Otsu(Mat src);

int main(int argc,  char* argv[])
{
	Mat img = imread("/home/rechie/Documents/me/data/Pictures/3.jpg", CV_LOAD_IMAGE_GRAYSCALE);
	Mat dst = Mat(img.rows, img.cols, CV_8UC1);

	int thresh = Otsu(img);
	
	threshold(img, dst, thresh, 255, CV_THRESH_BINARY);

	imshow("img", dst);

	waitKey(0);

	return 0;
}

int Otsu(Mat src)
{
	int height = src.rows;
	int width = src.cols;
	long size = height * width;
	unsigned char* data = src.data;

	//histogram
	float histogram[256] = {0};
	for (int m = 0; m < height; m++)
	{
		unsigned char* p = data + m * src.step;
		for(int n = 0; n < width; n++)
		{
			histogram[int(*p++)]++;
		}
	}

	int threshold;
	long sum0 = 0, sum1 = 0;  //存储前景的灰度总和和背景灰度总和
	long cnt0 = 0, cnt1 = 0;  //前景的总个数和背景的总个数
	double w0 = 0, w1 = 0;    //前景和背景所占整幅图像的比例
	double u0 = 0, u1 = 0;    //前景和背景的平均灰度
	double variance = 0;      //最大类间方差
	int i, j;
	double u = 0;
	double maxVariance = 0;
	for(i = 1; i < 256; i++)
	{
		sum0 = 0;
		sum1 = 0;
		cnt1 = 0;
		w0 = 0;
		w1 = 0;
		for(j = 0; j < i; j++)
		{
			cnt0 += histogram[j];
			sum0 += j * histogram[j];
		}

		u0 = (double)sum0 / cnt0;
		w0 = (double)cnt0 / size;

		for(j = i; j <= 255; j++)
		{
			cnt1 += histogram[j];
			sum1 += j * histogram[j];
		}

		u1 = (double)sum1 / cnt1;
		w1 = 1 - w0;  //(double)cnt1 / size

		u = u0 * w0 + u1 * w1;  //图像的平均灰度
		printf("u = %f\n", u);

		variance = w0 * w1 * (u0 - u1) * (u0 -u1);

		if(variance >maxVariance)
		{
			maxVariance = variance;
			threshold = i;
		}
	}

	printf("threshold = %d\n", threshold);
	return threshold;
}
