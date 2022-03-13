/*
    Nombre: Queue
    Descripción: Una implementación de queue para la clase de compiladores
    Por: Luis Fernando Lomelín Ibarra
    Creado: 25/02/2022
*/

//Definición de nodos para crear listas para manejar de manera dinamica los datos del queue
//#include "Node.h"

template <typename T>
class Queue{
    protected:
    long long int size;
    Node<T>* last;
    Node<T>* first;

    public:
    //Constuctor
    Queue();
    Queue(T);
    //Operaciones
    void push(T);
    T pop();
    bool empty();
    long long int getSize();
    T top();
    T front();
    private:
    
    
};

//Definición de los constructores
template <typename T>
Queue<T>::Queue(){
    size = 0;
    last = NULL;
    first = NULL;
}
template <typename T>
Queue<T>::Queue(T item){
    Node<T>* newHead = new Node<T>(item);
    first = last = newHead;
    size++;
    
}

//Definición de las funciones del Queue
template <typename T>
void Queue<T>::push(T item){
    Node<T>* newHead = new Node<T>(item);
    if(size > 0){
        last->prev = newHead;
    }else{
        first = newHead;
    }
    newHead->next = last;
    last = newHead;
    size++;
}

template <typename T>
T Queue<T>::pop(){
        T item = first->data;
        Node<T>* old = first;
        first = first->prev;
        delete old;
        size--;
        return item;
}

template <typename T>
T Queue<T>::top(){
        T item = first->data;
        return item;
}

template <typename T>
T Queue<T>::front(){
    T item = first->data;
    return item;
}

template <typename T>
long long int Queue<T>::getSize(){
    return size;
}

template <typename T>
bool Queue<T>::empty(){
    if(size){
        return true;
    }else{
        return false;
    }
}