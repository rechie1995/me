# 卡尔曼滤波(KalmanFilter)  
整个卡尔曼滤波的过程就是个递推计算的过程，不断的“预测——更新——预测——更新……”  
## 编程步骤
Step1:定义kalmanFilter类并初始化
 ```C++
//构造KF对象  
KalmanFilter KF(DP, MP, 0);  
//初始化相关参数  
KF.transitionMatrix        转移矩阵 A  
KF.measurementMatrix       测量矩阵 H  
KF.processNoiseCov         过程噪声 Q  
KF.measurementNoiseCov     测量噪声 R
KF.errorCovPost            最小均方误差 P  
KF.statePost               系统初始状态 X(0)  
Mat measurement            定义初始测量值 Z(0)  
 ```
Step2:预测  
```  
KF.predict()               返回的是下一时刻的状态值KF.statePost(k + 1)  
```  
Step3:更新  
```  
更新measurement            注意measurement不能通过观测方程进行计算得到，要自己定义！  
更新KF KF.correct(measurement)  
```  
最终结果应该是更新后的statePost  
  
  
  ##  参考文献  

> 1. [卡尔曼滤波详解](http://blog.csdn.net/gdfsg/article/details/50904811)
