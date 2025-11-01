#include "Boletin_1.hpp"
#include <iostream>
#include <cstdlib>
#include <numeric>
#include <algorithm>

int main (int argc, char *argv[]) {
    std::vector<int> vec(20);
    std::iota(vec.begin(), vec.end(), 1);
    for(auto i : vec) std::cout << i << ", ";
  std::cout << "\n";
  int e=1, pos;
  while(e){
    std::cout << "\nElemento a buscar e=";
    std::cin >> e;
    std::cout << "\n\n";
    pos = busqueda_secuencial(vec,e);
    std::cout << "Búsqueda secuencial: e=A[" << pos << "].\n";
    pos = busqueda_binaria(vec,e);
    std::cout << "Búsqueda binaria: e=A[" << pos << "].\n";
    pos = busqueda_exponencial(vec,e);
    std::cout << "Búsqueda exponencial: e=A[" << pos << "].\n";
  }
  return 0;
}
