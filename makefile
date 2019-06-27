#.PHONY:all say_hello generate clean
all:say_hello generate

say_hello:
	@echo "Hello World"

generate:
	@echo "Creating empty text files..."
	touch file-{1..10}.txt

clean:
	@echo "Cleaning up..."
	rm *.txt

CC=gcc

hello:hello.c
	${CC} hello.c -o hello

venv:
#	virtualenv venv1
	. venv1/bin/activate