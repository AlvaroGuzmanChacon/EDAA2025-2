#ifndef BOLETIN_2
#define BOLETIN_2

#include <iostream>
#include <vector>
#include <list>
#include <algorithm>
#include <functional>

using namespace std;

struct Node
{
    int data, degree; // data es la llave y degree el orden
    Node *child, *sibling, *parent;
};

class BinaryHeap{
private:
  vector<int> heap;
public:
  BinaryHeap(){
  }
  /*
  BinaryHeap(vector<int> data) :
    heap(data){
    make_heap(heap.begin(), heap.end(), greater<int>{});
  }
  */ 

  BinaryHeap(const vector<int> &data){
    for(int k: data){
      this->push(k);
    }
  }
  int min(){
    if(!heap.empty()) return heap.front();
    cerr << "Heap vacío." << endl;
    exit(EXIT_FAILURE);
  }

  int pop(){
    int min = this->min();
    pop_heap(heap.begin(), heap.end(), greater<int>{});
    heap.pop_back();
    return min;
  }

  void push(int key){
    heap.push_back(key);
    push_heap(heap.begin(), heap.end(), greater<int>{});
  }

  void print(){
    for (const auto& e : heap)
    cout << e << ' ';
    cout << '\n';
  }
};


class BinomialHeap
{
protected:
  list<Node *> roots;

private:
  // crea un nuevo nodo sin referencias
  Node* newNode(int key)
  {
    Node *temp = new Node;
    temp->data = key;
    temp->degree = 0;
    temp->child = temp->parent = temp->sibling = NULL;
    return temp;
  }

  // This function merge two Binomial Trees.
  Node* mergeBinomialTrees(Node *b1, Node *b2)
  {
    // Make sure b1 is smaller
    if (b1->data > b2->data) // preservar la propiedad de heap
      swap(b1, b2);

    // We basically make larger valued tree
    // a child of smaller valued tree
    b2->parent = b1;
    b2->sibling = b1->child;
    b1->child = b2;
    b1->degree++;
    // lo anterior reestructuro el arbol en tiempo constante

    return b1;
  }

  // This function perform union operation on two
  // binomial heap i.e. l1 & l2
  // en realidad no hace la union de tal manera que el resultado es un heap binomial
  // lo unico que hace es colocar las raices de los heaps en una lista enlazada de
  // tal manera que los ordenes sean no decrecientes
  // en terminos de estilo los push_back y los incrementos se podian hacer todos en
  // una linea con (*it++) pero acepto esto porque podria decirse que es mas claro :P
  list<Node*> unionBionomialHeap(list<Node*> l1, list<Node*> l2)
  {
    // _new to another binomial heap which contain
    // new heap after merging l1 & l2
    list<Node*> _new;
    list<Node*>::iterator it = l1.begin();
    list<Node*>::iterator ot = l2.begin();
    while (it!=l1.end() && ot!=l2.end())
    {
      // if D(l1) <= D(l2)
      if((*it)->degree <= (*ot)->degree)
      {
        _new.push_back(*it);
        it++;
      }
      // if D(l1) > D(l2)
      else
    {
        _new.push_back(*ot);
        ot++;
      }
    }

    // if there remains some elements in l1
    // binomial heap
    while (it != l1.end())
    {
      _new.push_back(*it);
      it++;
    }

    // if there remains some elements in l2
    // binomial heap
    while (ot!=l2.end())
    {
      _new.push_back(*ot);
      ot++;
    }
    return _new;
  }

  // adjust function rearranges the heap so that
  // heap is in increasing order of degree and
  // no two binomial trees have same degree in this heap
  // DEBE SER LLAMADO DESPUES DE unionBionomialHeap
  list<Node*> adjust(list<Node*> _heap)
  {
    if (_heap.size() <= 1) // nada que ajustar, _heap ya es un heap
      return _heap;
    list<Node*> new_heap;
    list<Node*>::iterator it1,it2,it3;
    it1 = it2 = it3 = _heap.begin();

    // alinear los iteradores para que it2 = it1 + 1 y que it3 = it1 + 2
    if (_heap.size() == 2)
    {
      it2 = it1; // redundante
      it2++;
      it3 = _heap.end();
    }
    else
  {
      it2++;
      it3=it2;
      it3++;
    }
    while (it1 != _heap.end())
    {
      // if only one element remains to be processed
      if (it2 == _heap.end())
        it1++;

        // If D(it1) < D(it2) i.e. merging of Binomial
        // Tree pointed by it1 & it2 is not possible
        // then move next in heap
      else if ((*it1)->degree < (*it2)->degree) // solo hay que avanzar pues no hay que unir
      {
      it1++;
      it2++;
      if(it3!=_heap.end())
        it3++;
    }

      // if D(it1),D(it2) & D(it3) are same i.e.
      // degree of three consecutive Binomial Tree are same
      // in heap
      else if (it3!=_heap.end() &&
        (*it1)->degree == (*it2)->degree &&
        (*it1)->degree == (*it3)->degree)
      {
        // como en unionBionomial heap, los input eran ya heaps, a lo mas
        // hay tres arboles del mismo orden en cualquier momento de la computacion
        // asi que en el siguiente paso se pasara a la siguiente condicion de este
        // if y se hara el merge que corresponde para que solamente haya un arbol de
        // cada orden en todo el bosque
        it1++;
        it2++;
        it3++;
      }

      // if degree of two Binomial Tree are same in heap
      else if ((*it1)->degree == (*it2)->degree) // unir en un arbol del siguiente orden
      {
        //Node *temp; // variable inutilizada
        *it1 = mergeBinomialTrees(*it1,*it2);
        it2 = _heap.erase(it2);
        if(it3 != _heap.end())
          it3++;
      }
    }
    return _heap;
  }

  // inserting a Binomial Tree into binomial heap
  // esto es hacer meld, pero con un heap de tamanyo igual a una potencia de 2
  list<Node*> insertATreeInHeap(list<Node*> _heap, Node *tree)
  {
    // creating a new heap i.e temp
    list<Node*> temp;

    // inserting Binomial Tree into heap
    temp.push_back(tree);

    // perform union operation to finally insert
    // Binomial Tree in original heap
    temp = unionBionomialHeap(_heap,temp);

    return adjust(temp);
  }

  // removing minimum key element from binomial heap
  // this function take Binomial Tree as input and return
  // binomial heap after
  // removing head of that tree i.e. minimum element
  list<Node*> removeMinFromTreeReturnBHeap(Node *tree)
  {
    list<Node*> heap;
    Node *temp = tree->child;
    Node *lo;

    // making a binomial heap from Binomial Tree
    while (temp)
    {
      // esto elimina la raiz de tree y luego, sus hijos quedan
      // disconexos en un bosque que es un un heap binomial
      // asi que hay que guardar estos nodos como raices en
      // la lista enlazada y eliminar referencias a sus siblings
      // pues ahora no estan en el mismo arbol
      lo = temp;
      temp = temp->sibling;
      lo->sibling = NULL;
      heap.push_front(lo);
    }
    return heap;
  }

  // inserting a key into the binomial heap
  list<Node*> insert(list<Node*> _head, int key)
  {
    // unir key como un arbol de orden 0 y agregarlo a todo el heap
    Node *temp = newNode(key);
    return insertATreeInHeap(_head,temp);
  }

  // return pointer of minimum value Node
  // present in the binomial heap
  // ESTO NO TOMA TIEMPO CONSTANTE COMO SE DIJO EN EL ANALISIS TEORICO
  // TOMA TIEMPO LOGARITMICO PUES RECORRE TODAS LAS RAICES
  Node* getMin(list<Node*> _heap)
  {
    list<Node*>::iterator it = _heap.begin();
    Node *temp = *it;
    while (it != _heap.end())
    {
      if ((*it)->data < temp->data)
        temp = *it;
      it++;
    }
    return temp;
  }

  list<Node*> extractMin(list<Node*> _heap)
  {
    list<Node*> new_heap,lo;
    Node *temp;

    // temp contains the pointer of minimum value
    // element in heap
    temp = getMin(_heap); // ubicar nodo a eliminar
    list<Node*>::iterator it;
    it = _heap.begin();
    while (it != _heap.end()) // agregar el resto del bosque a una lista enlazada
    {
      if (*it != temp)
      {
        // inserting all Binomial Tree into new
        // binomial heap except the Binomial Tree
        // contains minimum element
        new_heap.push_back(*it);
      }
      it++;
    }
    lo = removeMinFromTreeReturnBHeap(temp); // este es un heap con los hijos del nodo que eliminamos
    new_heap = unionBionomialHeap(new_heap,lo);
    new_heap = adjust(new_heap);
    return new_heap;
  }
  //
  // print function for Binomial Tree
  void printTree(Node *h)
  {
    while (h)
    {
      cout << h->data << " ";
      printTree(h->child);
      h = h->sibling;
    }
  }

  // print function for binomial heap
  void printHeap(list<Node*> _heap)
  {
    list<Node*> ::iterator it;
    it = _heap.begin();
    while (it != _heap.end())
    {
      printTree(*it);
      cout << " - ";
      it++;
    }
  }

  /* Este es el wrap que sirve como interfaz */
public:
  /* Empty constructor to make an empty heap */
  BinomialHeap(void)
  {
  }

  BinomialHeap(const vector<int> &v)
  {
    for (int k : v)
    roots = insert(roots, k);
  }

  int top(void)
  {
    return getMin(roots)->data;
  }

  void push(int key)
  {
    roots = insert(roots, key);
  }

  void pop(void)
  {
    roots = extractMin(roots);
  }

  void meld(const BinomialHeap &h)
  {
    roots = adjust(unionBionomialHeap(roots, h.roots));
  }

  bool empty(void)
  {
    return roots.empty();
  }

  void print(void)
  {
    printHeap(roots);
  }
};


////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////
///
///


template <class V> class FibonacciHeap;

template <class V> struct node {
private:
	node<V>* prev;
	node<V>* next;
	node<V>* child;
	node<V>* parent;
	V value;
	int degree;
	bool marked;
public:
	friend class FibonacciHeap<V>;
	node<V>* getPrev() {return prev;}
	node<V>* getNext() {return next;}
	node<V>* getChild() {return child;}
	node<V>* getParent() {return parent;}
	V getValue() {return value;}
	bool isMarked() {return marked;}

	bool hasChildren() {return child;}
	bool hasParent() {return parent;}
};

template <class V> class FibonacciHeap {
protected:
	node<V>* heap;
public:

	FibonacciHeap() {
		heap=_empty();
	}
  FibonacciHeap(const vector<V> &v)
  {
		heap=_empty();
    for (auto k : v)
      push(k);
  }
	virtual ~FibonacciHeap() {
		if(heap) {
			_deleteAll(heap);
		}
	}
	void push(V value) {
		node<V>* ret=_singleton(value);
		heap=_merge(heap,ret);
		//return ret;
	}
	void merge(FibonacciHeap& other) {
		heap=_merge(heap,other.heap);
		other.heap=_empty();
	}

	bool isEmpty() {
		return heap==NULL;
	}

	V getMinimum() {
		return heap->value;
	}

	void pop() {
		node<V>* old=heap;
		heap=_removeMinimum(heap);
		//V ret=old->value;
		delete old;
		//return ret;
	}

	void decreaseKey(node<V>* n,V value) {
		heap=_decreaseKey(heap,n,value);
	}

	node<V>* find(V value) {
		return _find(heap,value);
	}
  void print(){
    node<V>* c = heap;
      std::cout << c->value << ", ";
    while(c->hasChildren()){
      std::cout << c->value << ", ";
      c = c->getNext();
    }
  }
  void dump() {
		printf("digraph G {\n");
		if(heap==NULL) {
			printf("empty;\n}\n");
			return;
		}
		printf("minimum -> \"%p\" [constraint=false];\n",heap);
		node<int>* c=heap;
		do {
			_dumpChildren(c);
			c=c->getNext();
		} while(c!=heap);
		printf("}\n");
	}
private:
	void _dumpChildren(node<int>* n) {
		printf("\"%p\" -> \"%p\" [constraint=false,arrowhead=lnormal];\n",n,n->getNext());
		printf("\"%p\" -> \"%p\" [constraint=false,arrowhead=ornormal];\n",n,n->getPrev());
		if(n->isMarked())printf("\"%p\" [style=filled,fillcolor=grey];\n",n);
		if(n->hasParent()) {
			printf("\"%p\" -> \"%p\" [constraint=false,arrowhead=onormal];\n",n,n->getParent());
		}
		printf("\"%p\" [label=%d];\n",n,n->getValue());
		if(n->hasChildren()) {
			node<int>* c=n->getChild();
			do {
				printf("\"%p\" -> \"%p\";\n",n,c);
				_dumpChildren(c);
				c=c->getNext();
			} while(c!=n->getChild());
		}
	}
	node<V>* _empty() {
		return NULL;
	}

	node<V>* _singleton(V value) {
		node<V>* n=new node<V>;
		n->value=value;
		n->prev=n->next=n;
		n->degree=0;
		n->marked=false;
		n->child=NULL;
		n->parent=NULL;
		return n;
	}

	node<V>* _merge(node<V>* a,node<V>* b) {
		if(a==NULL)return b;
		if(b==NULL)return a;
		if(a->value>b->value) {
			node<V>* temp=a;
			a=b;
			b=temp;
		}
		node<V>* an=a->next;
		node<V>* bp=b->prev;
		a->next=b;
		b->prev=a;
		an->prev=bp;
		bp->next=an;
		return a;
	}

	void _deleteAll(node<V>* n) {
		if(n!=NULL) {
			node<V>* c=n;
			do {
				node<V>* d=c;
				c=c->next;
				_deleteAll(d->child);
				delete d;
			} while(c!=n);
		}
	}
	
	void _addChild(node<V>* parent,node<V>* child) {
		child->prev=child->next=child;
		child->parent=parent;
		parent->degree++;
		parent->child=_merge(parent->child,child);
	}

	void _unMarkAndUnParentAll(node<V>* n) {
		if(n==NULL)return;
		node<V>* c=n;
		do {
			c->marked=false;
			c->parent=NULL;
			c=c->next;
		}while(c!=n);
	}

	node<V>* _removeMinimum(node<V>* n) {
		_unMarkAndUnParentAll(n->child);
		if(n->next==n) {
			n=n->child;
		} else {
			n->next->prev=n->prev;
			n->prev->next=n->next;
			n=_merge(n->next,n->child);
		}
		if(n==NULL)return n;
		node<V>* trees[64]={NULL};
		
		while(true) {
			if(trees[n->degree]!=NULL) {
				node<V>* t=trees[n->degree];
				if(t==n)break;
				trees[n->degree]=NULL;
				if(n->value<t->value) {
					t->prev->next=t->next;
					t->next->prev=t->prev;
					_addChild(n,t);
				} else {
					t->prev->next=t->next;
					t->next->prev=t->prev;
					if(n->next==n) {
						t->next=t->prev=t;
						_addChild(t,n);
						n=t;
					} else {
						n->prev->next=t;
						n->next->prev=t;
						t->next=n->next;
						t->prev=n->prev;
						_addChild(t,n);
						n=t;
					}
				}
				continue;
			} else {
				trees[n->degree]=n;
			}
			n=n->next;
		}
		node<V>* min=n;
		node<V>* start=n;
		do {
			if(n->value<min->value)min=n;
			n=n->next;
		} while(n!=start);
		return min;
	}

	node<V>* _cut(node<V>* heap,node<V>* n) {
		if(n->next==n) {
			n->parent->child=NULL;
		} else {
			n->next->prev=n->prev;
			n->prev->next=n->next;
			n->parent->child=n->next;
		}
		n->next=n->prev=n;
		n->marked=false;
		return _merge(heap,n);
	}

	node<V>* _decreaseKey(node<V>* heap,node<V>* n,V value) {
		if(n->value<value)return heap;
		n->value=value;
		if(n->parent) {
			if(n->value<n->parent->value) {
				heap=_cut(heap,n);
				node<V>* parent=n->parent;
				n->parent=NULL;
				while(parent!=NULL && parent->marked) {
					heap=_cut(heap,parent);
					n=parent;
					parent=n->parent;
					n->parent=NULL;
				}
				if(parent!=NULL && parent->parent!=NULL)parent->marked=true;
			}
		} else {
			if(n->value < heap->value) {
				heap = n;
			}
		}
		return heap;
	}

	node<V>* _find(node<V>* heap,V value) {
		node<V>* n=heap;
		if(n==NULL)return NULL;
		do {
			if(n->value==value)return n;
			node<V>* ret=_find(n->child,value);
			if(ret)return ret;
			n=n->next;
		}while(n!=heap);
		return NULL;
	}
};

#endif
