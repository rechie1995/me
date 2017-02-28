cc = g++
exe = otsu.out
obj = otsu.o

$(exe):$(obj)
	$(cc) -o $(exe) $(obj) -lopencv_core -lopencv_highgui -lopencv_imgproc -lopencv_video -lopencv_imgcodecs

$(obj):otsu.cpp
	$(cc) -c otsu.cpp

clean:
	rm -rf *.o $(exe)
