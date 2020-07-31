char bar(void) {
    return 'a';
}

int foo(void) {
    int x = 5;
    return x;
}

int main(int argc, char **argv) {
    if(argc < 4) {
        int i = foo();
        while(i > 0) {
            ;
            i--;
        }
    } else {
        do {
            continue;
        } while(0);
    }

    while(1) {
        bar();
        break;
    }

    return 0;
}