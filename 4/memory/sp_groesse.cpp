#include <bits/stdc++.h>
#include "../sparse_table.cpp"

int UPPER = 100000000;

int main() {

  // Ingresamos de 0 hasta el valor que se desea
  std::vector<int> vec(UPPER);
  std::iota(vec.begin(), vec.end(), 1);
  int i;
  int n = UPPER;
  for (i = 1; i < n; i*=2) {
    // Aquí insertas elementos en la EDD para ver como va creciendo
    sparse_table<int> sp_table(std::vector<int>(vec.begin(), vec.begin()+i));
  }

  return 0;
}
