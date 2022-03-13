%{
    #include <string>
    #include<iostream>
    #include "myscanner.hpp"
    #undef YY_DECL
    #define YY_DECL int com::myscanner::yylex(com::myparser::semantic_type * const lval, com::myparser::location_type *loc )    

    using token = com::myparser::token;

    

    #define YY_NO_UNISTD_H

    #define YY_USER_ACTION loc->step(); loc->columns(yyleng);
%}
%option debug

%option yyclass="com::myscanner"
%option noyywrap
%option c++

%%

%{          
            yyval = lval;
%}

":" {return(token::COLON);}
";" {return(token::SEMICOLON);}
"," {return(token::COMMA);}
"=" {return(token::EQ);}
"(" {return(token::OPENPAR);}
")" {return(token::CLOSEPAR);}
"<" {return(token::GT);}
">" {return(token::LT);}
"+" {return(token::PLUS);}
"-" {return(token::MINUS);}
"*" {return(token::MUL);}
"/" {return(token::DIV);}
"{" {return(token::OPENCUR);}
"}" {return(token::CLOSECUR);}

[pP][rR][oO][gG][rR][aA][mM] {return(token::PROGRAM);} 
[iI][fF] {return(token::IF);}
[eE][lL][sS][eE] {return(token::ELSE);}
[pP][rR][iI][nN][tT] {return(token::PRINT);}
[iI][nN][tT] {return(token::INT);}
[vV][aA][rR] {return(token::VAR);}
[fF][lL][oO][aA][tT] {return(token::FLOAT);}


[0-9]+ {return(token::CTE_INT);} 
[0-9]+\.[0-9]+([eE][+-]?[0-9]+)? {return(token::CTE_FLOAT);} 
\"[^"]+\" {return(token::CTE_STRING);} 
[a-zA-Z]([a-zA-Z]|[0-9])* {return(token::ID);} 
\n {loc->lines();}

%%
