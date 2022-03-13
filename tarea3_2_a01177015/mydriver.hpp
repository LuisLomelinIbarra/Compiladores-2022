#ifndef __MYSCANNER_HPP__
#define __MYSCANNER_HPP__ 1

#include <string>
#include <cstddef>
#include <istream>

#include "myscanner.hpp"
#include "myparser.tab.hh"

namespace com{

class mydriver{
public:
	mydriver() = default;
	virtual ~mydriver();

	//Para leer de archivo
	void parse(const char * const filename);

	void parse(std::istream &ins);
	
	
	void accept();
	void reject();

	
	std::ostream& print(std::ostream &stream);

private:
	void parser_helper(std::istream &stream);
		
	bool accepted = true;

	std::string message = "aceptado";

	com::myparser *parser = nullptr;
	com::myscanner *scanner = nullptr;

};

}

#endif
