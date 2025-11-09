#include <bits/stdc++.h>
#include "../sparse_table.cpp"

int UPPER = 10000;

int main() {

  // Ingresamos de 0 hasta el valor que se desea
  std::vector<int> vec(UPPER);
  std::iota(vec.begin(), vec.end(), 1);
  int i;
  int n = UPPER;
  for (i = 1; i < n; ++i) {
    // Aquí insertas elementos en la EDD para ver como va creciendo
    sparse_table<int> sp_table(std::vector(vec.begin(), vec.begin()+i));
  }

  return 0;
}
