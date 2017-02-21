cc = gcc 
exe = simple_va_fun.exe
obj = simple_va_fun.o

$(exe):$(obj)
	$(cc) -o $(exe) $(obj)

$(obj):*.c
	$(cc) -c *.c

clean:
	rm -rf *.o $(exe)
