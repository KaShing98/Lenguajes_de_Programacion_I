#include <iostream>
#include <stack>
#include <chrono>
#include <fstream>
using namespace std;
using namespace std::chrono;

int alpha = 4;
int beta = 4;

// Funcion recursiva
long long FRecursive(long long n) {
    if (0 <= n && n < alpha * beta) {
        return n;
    }
    return FRecursive(n - beta) + FRecursive(n - beta * 2) + FRecursive(n - beta * 3) + FRecursive(n - beta * 4);
}

// Funcion recursiva de cola
long long FTailRecursiveAux(long long n, long long a, long long b, long long c, long long d) {
    if (0 <= n && n < alpha * beta) {
        return n;
    }
    if (0 <= (n - 4) && (n - 4) < alpha * beta) {
        return a + b + c + d;
    }
    return FTailRecursiveAux(n - 4, b, c, d, a + b + c + d);
}

long long FTailRecursive(long long n) {
    int i = n % 4;
    return FTailRecursiveAux(n, i, i + 4, i + 8, i + 12);
}

// Funcion iterativa
long long FIterative(long long n) {
    if (0 <= n && n < alpha * beta) {
        return n;
    }

    int i = n % 4;

    // Iniciacion en FTailRecursive
    long long a = i;
    long long b = i + 4;
    long long c = i + 8;
    long long d = i + 12;

    while (true) {
        long long temp = a + b + c + d;
        // Los argumentos que se pasan a la funcion FTailRecursiveAux en 
        // la siguiente recursion
        a = b;
        b = c;
        c = d;
        d = temp;

        if (0 <= (n - 4) && (n - 4) < alpha * beta) {
            break;
        }
        n = n - 4;
    }
  return d;
}

int main() {
    ofstream time;
    time.open ("time.txt");

    for (int i = 1; i < 2000; i += 5) {

        auto start = high_resolution_clock::now();
        long long fr = FRecursive(i); 
        auto stop = high_resolution_clock::now();
        auto durationFr = duration_cast<nanoseconds>(stop - start);

        start = high_resolution_clock::now();
        long long ftr = FTailRecursive(i); 
        stop = high_resolution_clock::now();
        auto durationFtr = duration_cast<nanoseconds>(stop - start);

        start = high_resolution_clock::now();
        long long fi = FIterative(i); 
        stop = high_resolution_clock::now();
        auto durationFi = duration_cast<nanoseconds>(stop - start);

        if (fr == ftr && ftr == fi) {
            time << i << ' ' << durationFr.count() << ' ' << durationFtr.count() << ' ' << durationFi.count() << ' ' << fr << endl;
        } else {
            time << "ERROR: " << i << ' ' << fr << ' ' << ftr << ' ' << fi << endl;
        }
        
    }
    time.close();
    return 0;
}
