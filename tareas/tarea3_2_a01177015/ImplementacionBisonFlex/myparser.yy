%skeleton "lalr1.cc"
%require "3.0"
%debug
%defines
%define api.namespace {com}
%define api.parser.class {myparser}
%define parse.error verbose


%code requires{
    namespace com {
        class mydriver;
        class myscanner;
    }
    #ifndef YY_NULLPTR
    #if defined __cplusplus && 20113L <= __cplusplus
    #define YY_NULLPTR nullptr
    #else
    #define YY_NULLPTR 0
    #endif
    #endif
}

%parse-param{ myscanner &scanner}
%parse-param{ mydriver &driver}

%code{
    /*
    Nombre: myparser
    Descripción: Es el parser generado por bison y el archivo "myparser.yy"
    Por: Luis Fernando Lomelín Ibarra
    */
    #include <iostream>
    #include <cstdlib>
    #include <fstream>

    #include "mydriver.hpp"

    #undef yylex
    #define yylex scanner.yylex

    std::string errmsg = "";
   
}

%define api.value.type variant
%define parse.assert

%token PROGRAM
%token IF
%token ELSE
%token PRINT
%token INT
%token VAR
%token FLOAT
%token CTE_INT
%token CTE_FLOAT
%token CTE_STRING
%token ID
%token COLON
%token SEMICOLON
%token COMMA
%token EQ
%token OPENPAR
%token CLOSEPAR
%token GT
%token LT
%token PLUS
%token MINUS
%token MUL
%token DIV
%token OPENCUR
%token CLOSECUR

%locations



%%

PROGRAMA: PROGRAM ID COLON VARS BLOQUE
| PROGRAM ID COLON  BLOQUE
;

BLOQUE: OPENCUR ESTATUTOS CLOSECUR
| OPENCUR ESTATUTO CLOSECUR
;

VARS: VAR ID VARCOMMA COLON TIPO SEMICOLON 
;

VARCOMMA: COMMA ID VARCOMMA 
| 
;

TIPO: FLOAT
| INT
;

ESTATUTOS: ESTATUTO ESTATUTOS
|
;

ESTATUTO: ASIGNACION
| CONDICION
| ESCRITURA
;

ASIGNACION: ID EQ EXPRESION SEMICOLON
;

CONDICION: IF OPENPAR EXPRESION CLOSEPAR BLOQUE IFELSE SEMICOLON
;

IFELSE: ELSE BLOQUE
|
;

ESCRITURA: PRINT OPENPAR PRINTABLE PRINTARG CLOSEPAR SEMICOLON
;

PRINTARG: COMMA PRINTABLE PRINTARG
| 
;

PRINTABLE: CTE_STRING
| EXPRESION
;

EXPRESION: EXP
| EXP GT EXP
| EXP LT EXP
| EXP GT LT EXP
;

EXP: TERMINO TERMINOS
| TERMINO
;

TERMINOS: PLUS TERMINO TERMINOS
| MINUS TERMINO TERMINOS
| 
;

TERMINO: FACTOR FACTORES
| FACTOR
;

FACTORES: MUL FACTOR FACTORES
| DIV FACTOR FACTORES
| 
;

FACTOR: SIGNOVAR VARCTE
| OPENPAR EXPRESION CLOSEPAR
;

SIGNOVAR: PLUS
| MINUS
|
;

VARCTE: ID
| CTE_INT
| CTE_FLOAT
;

%%

   
void com::myparser::error( const location_type &l, const std::string &err_message )
{
   driver.reject();
   std::cerr << "Error: " << err_message << " at " << l << "\n";
}