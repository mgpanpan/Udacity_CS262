function fib(n) {
    if (n == 0) {
        return 1;
    };
    return n * factorial(n - 1);
}
write(fib(10));
write(10);
