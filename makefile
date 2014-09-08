
ORDER ?= ASC

sort: sort.c
ifeq ($(ORDER),DSC)
	gcc -o sort sort.c read_data.a -DDSC=1
else
	gcc -o sort sort.c read_data.a -DASC=1
endif

.PHONY: clean
clean:
	rm sort
