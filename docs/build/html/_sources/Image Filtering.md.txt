# 图像滤波
## 自定义线性滤波
### Robert算子

```c++
	//Robert算子在x方向
Mat kernal_x = (Mat_<int>(2, 2) << 1, 0, 0, -1);
filter2D(src, dst, src.depth(), kernal_x, Point(-1, -1), 0.0);
imshow("output image", dst);

	//Robert算子在y方向
Mat kernal_y = (Mat_<int>(2, 2) << 0, 1, -1, 0);
filter2D(src, dst, src.depth(), kernal_y, Point(-1, -1), 0.0);
imshow("output image", dst);
```
### Sober算子

```c++
	// Sobel算子在x方向
Mat kernal_x = (Mat_<int>(3, 3) << -1, 0, 1, -2, 0, 2, -1, 0, 1);
filter2D(src, dst, src.depth(), kernal_x, Point(-1, -1), 0.0);

	// Sobel算子在y方向
Mat kernal_y = (Mat_<int>(3, 3) << -1, -2, -1, 0, 0, 0, 1, 2, 1);
filter2D(src, dst, src.depth(), kernal_y, Point(-1, -1), 0.0);
```

### 拉普拉斯算子

```c++
Mat kernal = (Mat_<int>(3, 3) << 0, -1, 0, -1, 4, -1, 0, -1, 0);
filter2D(src, dst, src.depth(), kernal, Point(-1, -1), 0.0);
```

### 自定义卷积filter2D

```c++
filter2D(
Mat src, //输入图像
Mat dst, // 模糊图像
int depth, // 图像深度32/8，如果不知道一般都写默认最大深度
Mat kernel, // 卷积核/模板，输入的卷积核大小一般都是基数3、5、7、9等等
Point anchor, // 锚点位置，锚点直接写（-1,-1）就会自动帮你找到锚点的中心位置
double delta // 计算出来的像素+delta
)
```
其中 kernal是可以自定义的卷积核

