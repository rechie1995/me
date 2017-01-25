cc = g++
exe = kalman.out
obj = kalman.o

$(exe):$(obj)
	$(cc) -o $(exe) $(obj) -lopencv_core -lopencv_highgui -lopencv_imgproc -lopencv_video

kalman.o:kalman.cpp
	$(cc) -c kalman.cpp

clean:
	rm -rf *.o $(exe)
