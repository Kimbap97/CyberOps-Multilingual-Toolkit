// src/memory_buffer.cpp
#include <iostream>
#include <cstring>

void vulnerable_function(char* str) {
    char buffer[16];
    // PELIGRO: strcpy no verifica el tamaño del destino
    strcpy(buffer, str); 
    std::cout << "Buffer guardado: " << buffer << std::endl;
}

int main(int argc, char** argv) {
    if (argc > 1) {
        vulnerable_function(argv[1]);
    } else {
        std::cout << "Uso: ./memcheck [input_string]" << std::endl;
    }
    return 0;
}