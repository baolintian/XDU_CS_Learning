# 对图像的基本操作
## 加载、修改和保存图像

### 加载图像（cv::imread）

**imread**功能是加载图像文件成为一个**Mat**对象，其中第一个参数表示图像文件名称

第二个参数，表示加载的图像是什么类型，支持常见的三个参数值：

- IMREAD_UNCHANGED (<0) 表示加载原图，不做任何改变
- IMREAD_GRAYSCALE ( 0)表示把原图作为灰度图像加载进来

- IMREAD_COLOR (>0) 表示把原图作为RGB图像加载进来

**注意**：OpenCV支持JPG、PNG、TIFF等常见格式图像文件加载

## 显示图像（cv::namedWindos 与cv::imshow）

namedWindos功能是创建一个OpenCV窗口，它是由OpenCV自动创建与释放，你无需取销毁它

常见用法namedWindow("Window Title", WINDOW_AUTOSIZE)

- WINDOW_AUTOSIZE会自动根据图像大小，显示窗口大小，不能人为改变窗口大小
- WINDOW_NORMAL,跟QT集成的时候会使用，允许修改窗口大小

**imshow**根据窗口名称显示图像到指定的窗口上去，第一个参数是窗口名称，第二参数是Mat对象


### 修改图像（cv::cvtColor）

cvtColor的功能是把图像从一个彩色空间转换到另外一个色彩空间，有三个参数，第一个参数表示源图像、第二参数表示色彩空间转换之后的图像、第三个参数表示源和目标色彩空间如：COLOR_BGR2HLS 、COLOR_BGR2GRAY等


```c++
cvtColor( image, gray_image, COLOR_BGR2GRAY );
```


### 保存图像（cv::imwrite）

保存图像文件到指定目录路径

只有8位、16位的PNG、JPG、Tiff文件格式而且是单通道或者三通道的BGR的图像才可以通过这种方式保存

保存PNG格式的时候可以保存透明通道的图片

可以指定压缩参数


```c++
#include <opencv2/opencv.hpp>
#include <iostream>

using namespace cv;

int main(int argc, char** argv) {
	Mat src = imread("D:/1.jpg");
	if (src.empty()) {
		printf("Could not load image...\n");
		return -1;
	}

	namedWindow("test opencv setup", CV_WINDOW_AUTOSIZE);
	imshow("test opencv setup", src);

	namedWindow("output windows", CV_WINDOW_AUTOSIZE); //自动形式图像大小，而且不可改变 
	Mat output_image;
	cvtColor(src, output_image, CV_BGR2HLS);
	imshow("output windows", output_image);

	imwrite("D:/2.png", output_image);

	waitKey(0);
	return 0;
}
```


## Mat对象
Mat对象OpenCV2.0之后引进的图像数据结构、自动分配内存、不存在内存泄漏的问题，是面向对象的数据结构。Mat的主要作用是操作图像和矩阵。Mat对象用来存储图像矩阵的各种信息。（大小、值、数字通道等）

cv::Mat分为两个部分，头部与数据部分。头部包含了矩阵的所有相关信息（大小、通道数量、数据类型等）。头部有一个指向数据块的指针，即data属性，也就是我们有明确要求的时候，内存块才会被复制。实际上，大多数操作仅仅复制了cv::Mat的头部，因此多个对象会指向同一个数据块。这种内存管理模式可以提高应用程序运行效率，避免内存泄露。

数据块包含了图像中所有像素的值。

### Mat对象构造函数与常用方法

#### 常用构造函数

![image](https://github.com/Einstellung/OpenCV_learning/blob/master/OpenCV/images/Basic%20Image%20Operation/1.png?raw=true)

最主要的是前面两三个，常用。

#### 常用方法

- **Mat clone()：完全拷贝**
首先src通过imread读取一张图像，接下来：

```c++
Mat dst = src.clone();
imshow("output", dst);
```
就会完全克隆一张一模一样的图像。

- **void copyTo(Mat mat)：完全拷贝**

```c++
Mat dst;
src.copyTo(dst);
imshow("output", dst);
```
**部分复制**一般情况下只会复制Mat对象的头和指针部分，不会复制数据部分。比如下面情况：

```c++
Mat A= imread(imgFilePath);
Mat B(A);
```
**完全复制**如果想把Mat对象的头部和数据部分一起复制，可以通过上面两个API实现，即

```c++
Mat F = A.clone(); 或 Mat G; A.copyTo(G);
```


- **void convertTo(Mat dst, int type)：用于进行数据类型转换**
- 
如把CV_8UC1转换到CV32F1实现如下：

```c++
src.convertTo(dst, CV_32F);
```



- **int channels()：查看图像通道情况**

```c++
Mat dst;
cvtColor(src, dst, CV_BGR2GRAY);
printf("input image channels : %d\n", src.channels());
printf("output image channels : %d", dst.channels());
imshow("output", dst);
```
可以发现变成灰度图像之后输出通道数变为1

- **uchar\* ptr(i=0)：获取图片像素具体值，i表示行数**

```c++
Mat dst;
cvtColor(src, dst, CV_BGR2GRAY);
const uchar *firstRow = dst.ptr<uchar>(0);
printf("first pixel value : %d", *firstRow);
imshow("output", dst);
```
这样我们就可以获取第一行第一个像素的灰度值信息了。

- **.cols, .rows：获取行数和列数**

```c++
Mat dst;
cvtColor(src, dst, CV_BGR2GRAY);
int cols = dst.cols;
int rows = dst.rows;
printf("rows = %d cols = %d", rows, cols);
imshow("output", dst);
```

#### 构造函数继续举例(Mat对象创建)

如果是三个通道：

```c++
Mat M(3, 3, CV_8UC3, Scalar(0, 0, 255));  //scale要和通道数目一致
cout << "M:" << endl << M << endl;
```
**其中前两个参数分别表示行(row)跟列(column)、第三个CV_8UC3中的8表示每个通道占8位、U表示无符号、C表示Char类型、3表示通道数目是3，第四个参数是向量表示初始化每个像素值是多少，向量长度对应通道数目一致**

**Scalar**给每一个通道赋一个值，第一个和第二个通道的值全部都是0，第三个通道的值是255。


```c++
[  0,   0, 255,   0,   0, 255,   0,   0, 255;
   0,   0, 255,   0,   0, 255,   0,   0, 255;
   0,   0, 255,   0,   0, 255,   0,   0, 255]
```

如果变成了一个通道：

```c++
Mat M(100, 100, CV_8UC1, Scalar(127));  //scale要和通道数目一致
```
##### creat创建对象
```c++
Mat m1;
m1.create(src.size(), src.type());
m1 = Scalar(0, 0, 255);
imshow("output", m1);
```

##### 零初始化

```c++
Mat m2 = Mat::eye(2, 2, CV_8UC1);
cout << "m2 = " << endl << m2 << endl;
```

## 对像素的操作

### 读写像素

#### 读写单通道像素
- **读一个GRAY像素点的像素值（CV_8UC1）**

```c++
Scalar intensity = img.at<uchar>(y, x); 
//或者
Scalar intensity = img.at<uchar>(Point(x, y));
```

具体代码：

```c++
	//单通道
	Mat gray_src;
	cvtColor(src, gray_src, CV_BGR2GRAY);
	int height = gray_src.rows;
	int width = gray_src.cols;
	for (int row = 0; row < height; row++) {
		for (int col = 0; col < width; col++) {
			int gray = gray_src.at<uchar>(row, col);
			gray_src.at<uchar>(row, col) = 255 - gray;
		}
	}
	imshow("output", gray_src);
```
这个代码实现每个像素的像素值得翻转操作。

#### 读写三通道像素

```c++
Vec3f intensity = img.at<Vec3f>(y, x); 
float blue = intensity.val[0]; 
float green = intensity.val[1]; 
float red = intensity.val[2];
```
**Vec3b对应三通道的顺序是blue、green、red的uchar类型数据。**

**Vec3f对应三通道的float类型数据**


具体代码如下：

```c++
	//三通道
	Mat dst;
	dst.create(src.size(), src.type());
	int height = src.rows;
	int width = src.cols;
	int nc = src.channels();

	for (int row = 0; row < height; row++) {
		for (int col = 0; col < width; col++) {
			if (nc == 1) //如果是单通道，按照原先的方式进行处理
			{
				int gray = dst.at<uchar>(row, col);
				dst.at<uchar>(row, col) = 255 - gray;
			}
			else if (nc == 3)  //如果是三通道
			{
				int b = dst.at<Vec3b>(row, col)[0];
				int g = dst.at<Vec3b>(row, col)[1];
				int r = dst.at<Vec3b>(row, col)[2];
				dst.at<Vec3b>(row, col)[0] = 255 - b;
				dst.at<Vec3b>(row, col)[1] = 255 - g;
				dst.at<Vec3b>(row, col)[2] = 255 - r;
			}

		}
	}
```
当然，有更为简单的操作，用于实现图像像素255 - pixel

```c++
	//三通道
	Mat dst;
	dst.create(src.size(), src.type());
	bitwise_not(src, dst);
```
bitwise是位操作，not是非操作。也就是1变成0,0变成1。