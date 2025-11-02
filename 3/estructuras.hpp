// Construcción del FM index de un texto
//
// Prerrequisitos: Tener la biblioteca SDSL instalada
//
// Compilación: g++ -O3 -o fmi FM-index.cpp -lsdsl -ldivsufsort -ldivsufsort64

#ifndef estructuras
#define estructuras

#include <sdsl/suffix_arrays.hpp>
#include <string>

using namespace sdsl;

class FM_Index{
private:
  csa_wt<wt_int<>> fm_index;
public:
  FM_Index(std::string &texto){
    construct(fm_index, texto, 1);
  }

  size_t ocurrencias_patron(std::string &patron){
    return sdsl::count(fm_index, patron.begin(), patron.end());
  }
};


class KMP{
private:
  std::string _texto;
  size_t _n = _texto.length();

  std::vector<int> compute_pi(std::string &patron){
    std::vector<int> pi;
    int m = patron.length();
    int l = 0;
    pi[0] = 0;
    int i = 1;
    while (i < m) {
      if (patron[i] == patron[l]) {
        l++;
        pi[i] = l;
        i++;
      }
      else {
        if (l != 0) {
          l = pi[l - 1];
        }
        else {
          pi[i] = 0;
          i++;
        }
      }
    }
    return pi;
  }
public:
  KMP(std::string &texto) : _texto(texto) {
  }

  size_t ocurrencias_patron(std::string &patron){
    std::vector<int> pi = compute_pi(patron);
    int m = patron.length();

    int i = 0;
    int j = 0;
    size_t cuenta = 0;

    while (i < _n) {
      if (_texto[i] == patron[j]) {
        i++;
        j++;
        if (j == m) {
          cuenta ++;
          //res.push_back(i - j);
          j = pi[j - 1];
        }
      }
      else {
        if (j != 0)
          j = pi[j - 1];
        else
          i++;
      }
    }    
    return cuenta;
  }

};




#endif
