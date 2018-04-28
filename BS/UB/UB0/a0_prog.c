#include <stdio.h>
#include <stdlib.h>

int num_primes(int n){
    if(n <= 2){
        return 1;
    }
    int c = 1;
    for(int i=3; i<n; ++i){
        for(int j=2; j<=i; ++j){
            if(i % j == 0 && i != j){
                break;
            }else if(i == j){
                ++c;
            }
        }
    }
    return c;
}

void fill_primes(int *p_list, int n){
    if(n >= 2){
        p_list[0] = 2;
        int c = 1;
        for(int i=3; i<n; ++i){
            for(int j=2; j<=i; ++j){
                if(i % j == 0 && i != j){
                    break;
                }else if(i == j){
                    p_list[c++] = j;
                }
            }
        }
    }
}

int main(){
    int limit = 20;
    int len = num_primes(limit);
    int prime_list[len];
    fill_primes(prime_list, limit);
    for(int i=0; i<len; ++i){
        printf("%d,", prime_list[i]);
    }
    return 0;
}
