all: 
	make parser
	make lexer
	g++ -o lexparlittleduck main.cpp mydriver.cpp parser.o lexer.o 


parser: myparser.yy
	bison -d -v myparser.yy
	g++ -c -o parser.o myparser.tab.cc

lexer: mylexer.l
	flex --outfile=myscanner.yy.cc mylexer.l
	g++ -c myscanner.yy.cc -o lexer.o

clean:
	rm -rf mmain.o mydriver.o myparser.tab.cc myparser.tab.hh location.hh position.hh stack.hh myparser.output parser.o lexer.o myscanner.yy.cc lexparlittleduck 