cc = gcc 
exe = dechex.exe
obj = dechex.o

$(exe):$(obj)
	$(cc) -o $(exe) $(obj)

dechex.o:dechex.c
	$(cc) -c dechex.c

clean:
	rm -rf *.o $(exe)
