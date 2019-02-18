# 多线程OpenCV

使用 C++ 11 的多线程库：`<thread>`、`<mutex>`、`<condition_variable>`

难点在于提取视频帧线程与处理视频帧线程之间的等待与协调。