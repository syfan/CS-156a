n = 0;
er = 1.0;
a = 0.1;
x = [1.0;1.0];

while er > 10^-14
    gradf = [2 * (x(1) * exp(x(2)) - 2*x(2)*exp(-x(1))) * (exp(x(2)) + 2 * x(2) * exp(-x(1)));
        2 * (x(1) * exp(x(2)) - 2*x(2)*exp(-x(1))) * (x(1) * exp(x(2)) - 2 * exp(-x(1)))];
    y = x - a*gradf;
    er = norm(y - x);
    x = y;
    n = n + 1;
end
n, x