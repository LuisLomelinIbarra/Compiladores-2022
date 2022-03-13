#ifndef __myscanner_hpp__
#define __myscanner_hpp__ 1
#if ! defined(yyFlexLexerOnce)
#include <FlexLexer.h>
#endif

#include "myparser.tab.hh"
#include "location.hh"

namespace com{
    class myscanner: public yyFlexLexer{
        public:
            myscanner(std::istream *ins) : yyFlexLexer(ins){
                loc = new com::myparser::location_type();
            }
            using FlexLexer::yylex;
            virtual int yylex(com::myparser::semantic_type * const lval, com::myparser::location_type *location);
        private:
            com::myparser::semantic_type *yyval = nullptr;
            com::myparser::location_type *loc = nullptr;

    };
}

#endif