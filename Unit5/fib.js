function fib(n) {
    if (n == 0) {
        return 1;
    };
    return n * fib(n - 1);
}
write(fib(10));
write("\n");
write(10);
