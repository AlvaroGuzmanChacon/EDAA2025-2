#include <iostream>
#include "Boletin_2.hpp"

int main (int argc, char *argv[]) {
  vector<int> v({3, 1, 4, 1, 5, 9, 2});
  BinaryHeap bh(v);
  bh.print();
  std::cout << "\n.";

  binomial_heap binh(v);
  binh.print();
  std::cout << "\n.";

  FibonacciHeap fh(v);
  fh.dump();
  std::cout << "\n.";
  return 0;
}

