int a = 0;
int b = 1;
int c = 0;
int i = 0;
if (n == 0) {
    write(a);
} else {
    for (i = 2; i <= n; i = i + 1) {
        c = a + b;
        a = b;
        b = c;
    }
    write(b);
}
