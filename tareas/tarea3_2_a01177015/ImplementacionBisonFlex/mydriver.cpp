/*
    Nombre: mydriver
    Descripción: Una implementación de una clase driver para 
    utlizar de manera más sencilla el lexer y parser generado 
    por flex y bison.
    Por: Luis Fernando Lomelín Ibarra
*/

//Codigo basado en: https://github.com/jonathan-beard/simple_wc_example/blob/master/mc_driver.cpp
//Se usa como referencia para construir un driver para mi caso especifico

#include <cctype>
#include <fstream>
#include <cassert>

#include "mydriver.hpp"

com::mydriver::~mydriver(){
   delete(scanner);
   scanner = nullptr;
   delete(parser);
   parser = nullptr;
}

void com::mydriver::parse( const char * const filename ){
   assert( filename != nullptr );
   std::ifstream in_file( filename );
   if(!in_file.good()){
       exit( EXIT_FAILURE );
   }
   parser_helper( in_file );
   return;
}

/*

//Aunque se mantubo la funcipin del tutorial, se decidio no impelemntar dado que no hay forma actual de terminar de leer un lenuaje de little duck 2020

void com::mydriver::parse( std::istream &stream ){
   if( ! stream.good()  && stream.eof() )
   {
       return;
   }
   //else
   parser_helper( stream ); 
   return;
}
*/

void com::mydriver::parser_helper( std::istream &stream ){
   
   delete(scanner);
   try{
      scanner = new com::myscanner( &stream );
   }catch( std::bad_alloc &ba ){
      std::cerr << "Failed to allocate scanner: (" <<
         ba.what() << "), exiting!!\n";
      exit( EXIT_FAILURE );
   }
   
   delete(parser); 
   try{
      parser = new com::myparser( (*scanner) /* scanner */, 
                                  (*this) /* driver */ );
   }catch( std::bad_alloc &badalloc ){
      std::cerr << "Failed to allocate parser: (" << 
         badalloc.what() << "), exiting!!\n";
      exit( EXIT_FAILURE );
   }
   const int accept = 0;
   if( parser->parse() != accept ){
      std::cerr << "Parse failed!!\n";
   }
   return;
}

void com::mydriver::accept(){
    message = "apropiado";

}

void com::mydriver::reject(){
    message = "rechazado";
}

/*

//Forma tentativa de los errores

void com::mydriver::reject(int cause){
    / *
        Tratar de listar y dar un mensaje apropiado del error detectado
        0: Error en la definición de programa
        1: Error de declaración de variable
        2: Error en la declaración de un bloque
        3: Error de assignación
        4: Error de condición
        5: Error de escritura
        6: Error de Expresión
        7: Error de Termino
        8: Error de Factor
        9: Error de variable cte

    * /
    
    switch(cause){
        case 0:{
            message = "Hay un error en la definicion de programa /// checa que la estructura de la definicion del programa";
            break;
        }
        case 1:{
            message = "Hay un error en declaracion de variable /// checa que hayas escrito bien los nombres de variables o que siguas la definicion correcta de las mismas";
            break;
        }
        case 2:{
            message = "Hay un error en la declaracion de un bloque /// checa que tengas una serie de estatuos encerrado entre llaves";
            break;
        }
        case 3:{
            message = "Hay un error de assignacion /// checa las asignaciones en el codigo";
            break;
        }
        case 4:{
            message = "Hay un error de condicion /// checa que las condiciones tengan la estructura correcta";
            break;
        }
        case 5:{
            message = "Hay un error de escritura /// checa que el print tenga la forma correcta";
            break;
        }
        case 6:{
            message = "Hay un error en expresion /// checa que las expresiones esten bien escritas";
            break;
        }
        case 7:{
            message = "Hay un error en la escritura de terminos /// checa que los terminos esten bien escritos";
            break;
        }
        case 8:{
            message = "Hay un error en la escritura de factores /// checa que los factores esten correctamente escritos";
            break;
        }
        case 9:{
            message = "Hay un error en la escrituras de variables contsantes /// checa que los valores de variables constantes esten bien escritas";
            break;
        }
        
    }
    message += "\n******El código NO se acepta*******";
} */

std::ostream& com::mydriver::print( std::ostream &stream ){
   stream << "Analizer::: " <<message<<"\n";
   return(stream);
}