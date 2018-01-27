cc = gcc 
exe = Sorting.exe
obj = main.o

$(exe):$(obj)
	$(cc) -o $(exe) $(obj)

$(obj):*.c
	$(cc) -c *.c

clean:
	rm -rf *.o $(exe)
