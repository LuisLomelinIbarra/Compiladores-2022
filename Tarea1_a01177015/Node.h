template <typename T>
class Node{
    protected:
    public:
    

    long long int size;
    T data;
    Node* next;
    Node* prev;
    //Constructores
    Node();
    Node(T);
    private:
};

template <typename T>
Node<T>::Node(){
    size = 0;
    next = nullptr;
    prev = nullptr;
}

template <typename T>
Node<T>::Node(T item){
    size = 1;
    data = item;
    next = nullptr;
    prev = nullptr;
}

