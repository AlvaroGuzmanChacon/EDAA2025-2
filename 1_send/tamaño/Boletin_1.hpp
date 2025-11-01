#ifndef BOLETIN_1
#define BOLETIN_1

#include <iostream>
#include <vector>
#include <algorithm>

int busqueda_secuencial(std::vector<int> &sorted_array, int element){
  for(int i=0; i<sorted_array.size(); i++){
    if(element < sorted_array[i]) return -1;
    if(sorted_array[i] == element) return i;
  }
  return -1;
}

int busqueda_binaria(std::vector<int> &sorted_array, int element){
  int start = 0;
  int end = sorted_array.size()-1;
  int mid;
  while(start <= end){
    mid = (start + end)/2;
    if (sorted_array[mid] == element) return mid;
    if (sorted_array[mid] < element){
      start = mid+1;
    } else {
      end = mid-1;
    }
  }
  return -1;
}

int busqueda_exponencial(std::vector<int> &sorted_array, int element){
  if (sorted_array[0] == element) return 0;
  int index = 1;

  while(index <= sorted_array.size()-1){
    if(element < sorted_array[index]){
      break;
    }
    index *= 2;
  }

  int start = index/2;
  int end = std::min(index, (int)sorted_array.size()-1);
  int mid;
  while(start <= end){
    mid = (start + end)/2;
    if (sorted_array[mid] == element) return mid;
    if (sorted_array[mid] < element){
      start = mid+1;
    } else {
      end = mid-1;
    }
  }
  return -1;
  
}

#endif
