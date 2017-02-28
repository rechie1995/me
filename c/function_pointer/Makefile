cc = gcc 
exe = function_pointer.exe
obj = function_pointer.o

$(exe):$(obj)
	$(cc) -o $(exe) $(obj)

$(obj):*.c
	$(cc) -c *.c

clean:
	rm -rf *.o $(exe)
