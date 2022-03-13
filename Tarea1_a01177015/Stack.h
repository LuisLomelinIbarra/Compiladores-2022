/*
    Nombre: Stack
    Descripción: Una implementación de stack para la clase de compiladores
    Por: Luis Fernando Lomelín Ibarra
    Creado: 25/02/2022
*/

//Definición de nodos para crear listas para manejar de manera dinamica los datos del stack
#include "Node.h"

//Definición de la clase del Stack
template <typename T>
class Stack{
    protected:
    long long int size;
    Node<T>* head;

    public:
    //Constuctor
    Stack();
    Stack(T);
    //Operaciones
    void push(T);
    T pop();
    bool empty();
    long long int getSize();
    T top();
    private:
    
};

//Definición de los constructores
template <typename T>
Stack<T>::Stack(){
    size = 0;
    head = NULL;
}
template <typename T>
Stack<T>::Stack(T item){
    Node<T>* newHead = new Node<T>(item);
    head = newHead;
    size++;
    
}
//Definición de las funciones del stack
template <typename T>
void Stack<T>::push(T item){
    Node<T>* newHead = new Node<T>(item);
    
    newHead->next = head;
    head = newHead;
    size++;
}

template <typename T>
T Stack<T>::pop(){
        T item = head->data;
        Node<T>* old = head;
        head = head->next;
        delete old;
        size--;
        return item;
}

template <typename T>
T Stack<T>::top(){
        T item = head->data;
        return item;
}

template <typename T>
long long int Stack<T>::getSize(){
    return size;
}

template <typename T>
bool Stack<T>::empty(){
    if(size){
        return true;
    }else{
        return false;
    }
}