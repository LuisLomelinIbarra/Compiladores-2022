#include <iostream>
#include <cstdlib>
#include <cstring>

#include "mydriver.hpp"

int main( const int argc, const char **argv ){
   /*checar que se de un nombre de archivo*/
   if(argc == 2){
      
      com::mydriver driver;
      
      if( std::strncmp( argv[ 1 ], "-h", 2 ) == 0 ){
         ;
         std::cout << "Dar el nombre de un archivo como segundo argumento para leer\n";
         std::cout << "PENDIENTE:: ACTUAL MENTE NO HAY FORMA DE LEER DIRECTAMENTE DE LA CONSOLA\n";
         return( EXIT_SUCCESS );
      }else{
         //Parsear archivo
         driver.parse( argv[1] );
      }
      //debera de imprimir aprobado si todo sale bien. sino debe de dar errores
      driver.print( std::cout ) << "\n";
   }else{
      std::cout << "Se debe de dar un archivo a leer";
      return(EXIT_FAILURE);
   }
   return(EXIT_SUCCESS);
}