#include "estructuras.hpp"



int main (int argc, char *argv[]) {
  std::string texto = "texto.txt";
  std::string patron;


  std::cout << "Texto: " << texto << ".\n\n";
  std::cout << "Ingrese patron a buscar: ";
  std::cin >> patron;

  std::cout << "\nOcurrencias detectadas del patron " << patron << ":\n";
  FM_Index fmi(texto);
  std::cout << "\tFMI: " << fmi.ocurrencias_patron(patron) << ".\n";
  KMP kmp(texto);
  std::cout << "\tKMP: " << kmp.ocurrencias_patron(patron) << ".\n";
  return 0;
}
