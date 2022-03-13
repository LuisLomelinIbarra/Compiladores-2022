#include <iostream>
#include "Stack.h"
#include "Queue.h"
using namespace std;

int main(){
    
    cout << "Este programa va a correr las estructuras de datos y va a probarlos, mostrando sus resultados en esta pantalla\n";
    
    /* Pruebas Stack:
        -Declaración vacio
        -Declaración con un item
        -Push a una lista vacia
        -Push a una lista con un item
        -Push a una lista que a pasado por una operación exitosa
        -Pop a una lista con 1 item
        -Pop a una lista sin items
        -Pop a una lista de multiples items
    */
    cout << "********************\n***** Stack\n*******************"<<endl;
    cout << "- Declaración vacio";
    Stack<char> st;
    cout << "\n- Declaración con un item";
    Stack<int> st2(3);
    cout << "\n- Push a una lista vacia";
    st.push('a');
    cout << "\t Se metio: " << st.top();
    cout <<"\n- Push a una lista con un item";
    st2.push(43);cout << "\t Se metio: " << st2.top();
    cout <<"\n- Push a una lista que a pasado por una operación exitosa";
    cout << "\t top: " << st2.top();
    st2.push(4);
    cout << "\t Se metio: " << st2.top();
    cout <<"\n- Pop a una lista con 1 item:  ";
    cout << "\t Top: " << st.top();
    char printstackch = st.pop();
    long long int intTest = st.getSize();
    try{
        if(intTest <= 0){
            throw intTest;
            cout << " (Size funciono y detecto que estaba vacio)";
            cout << printstackch;
        }
        
    }catch(long long int intTest){
        cout << "\t Nuevo Top: " << "\t";
    }
    
    cout << printstackch;
    cout <<"\n- Pop a una lista sin items";
    intTest = st.getSize();
    try{
        if(intTest <= 0){
            throw intTest;
            printstackch = st.pop();
            cout << printstackch;
        }
        
    }catch(long long int intTest){
        cout << " (Size funciono y detecto que estaba vacio)";
    }
    cout <<"\n- Pop a una lista de multiples items: ";
    cout << "\t Top: " << st2.top();
    int testStackint = st2.pop();
    cout << "\t Top: " << st2.top();
    cout << "\t"<<testStackint;

    cout << "\n:::: Simple for loop que mete numeros del 1 al 10 y les hace pop\n";
    Stack<int> st3;
    for (int i =1; i <=10; i++){
        st3.push(i);
    }

    for(int i = 1; i <=10; i++){
        cout << st3.pop()<< " ";
    }
    
    /* Pruebas Queue:
        -Declarar una queue vacia
        -Declarar una queue con un valor
        -Push a una queue vacia
        -Push a una queue con un elemento
        -Push a una queue que ha pasado por una operación exitosa
        -Pop a una queue con un elemento
        -Pop a una queue vacia
        -Pop a una queue con más de  un elemento
    */
    cout << "\n********************\n***** Queue\n*******************"<<endl;
    cout <<"\n- Declarar una queue vacia";
    Queue<int> que;
    cout <<"\n- Declarar una queue con un valor";
    Queue<char> que2('B');
    cout << "\t Contiene "<<que2.top();
    cout <<"\n- Push a una queue vacia";
    que.push(10);
    cout << "\t Se metio "<<que.top();
    cout <<"\n- Push a una queue con un elemento";
    que2.push('2');
    cout << "\t Se metio "<<que2.top();
    cout <<"\n- Push a una queue que ha pasado por una operación exitosa";
    que2.push('A');
    cout << "\t Se metio "<<que.top();
    cout <<"\n- Pop a una queue con un elemento";
    cout << "\t Top: " << que.front();
    que.pop();
    bool isEmpty = que.empty();
    try{
        if(isEmpty){
            throw isEmpty;
            que.pop();
        }
    }catch(bool isEmpty){
        cout << "\t Detecto que el queue esta vacio";
    }
    
    cout <<"\n- Pop a una queue vacia";
    
    isEmpty = que.empty();
    try{
        if(isEmpty){
            throw isEmpty;
            que.pop();
        }
    }catch(bool isEmpty){
        cout << "\t Detecto que el queue esta vacio";
    }
    
    cout <<"\n- Pop a una queue con más de  un elemento";
    cout << "\t Top: " << que2.front();
    que2.pop();
    cout << "\t Nuevo Top: " << que2.top()<<"\t";

    cout << "\n:::: Simple for loop que mete numeros del 1 al 10 y les hace pop\n";
    Queue<int> que3;
    for (int i =1; i <=10; i++){
        que3.push(i);
    }

    for(int i = 1; i <=10; i++){
        cout << que3.pop()<< " ";
    }
    /* Pruebas Table:
        
    */
    cout <<endl << "\n********************\n***** Table\n*******************"<<endl;



    return 0;
}