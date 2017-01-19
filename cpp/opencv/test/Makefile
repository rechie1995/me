cc = g++
exe = test.out
obj = test.o

$(exe):$(obj)
	$(cc) -o $(exe) $(obj) -lopencv_core -lopencv_highgui
test.o:test.cpp
	$(cc) -c test.cpp
clean:
	rm -rf *.o $(exe)
