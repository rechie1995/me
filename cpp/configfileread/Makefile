cc = g++ 
exe = main.exe
obj = configfileread.o

$(exe):$(obj)
	$(cc) -o $(exe) $(obj)

$(obj):*.cpp
	$(cc) -c *.cpp

clean:
	rm -rf *.o $(exe)
