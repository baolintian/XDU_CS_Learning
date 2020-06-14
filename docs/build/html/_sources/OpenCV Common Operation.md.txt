# OpenCV常用操作
## 获取执行时间
**getTickCount()：用于返回从操作系统启动到当前所经的计时周期数**

**getTickFrequency()：用于返回CPU的频率。get Tick Frequency。这里的单位是秒，也就是一秒内重复的次数。**


```c++
double t = getTickCount();
Mat kernal = (Mat_<char>(3, 3) << 0, -1, 0, 
								-1, 5, -1, 
							    0, -1, 0);
filter2D(src, dst, src.depth(), kernal);
double timecousume = (getTickCount() - t) / getTickFrequency();
printf("time consume %.3f", timecousume);
```
这里是对矩阵掩膜操作的一个时间统计，其中src和dst都是之前定义用Mat对象定义的。