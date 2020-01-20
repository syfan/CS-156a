n = 0;
maxn = 15;
ers = 1.0;
a = 0.1;
xx = 1.0;
yy = 1.0;
er1 = 1.0;
er2 = 1.0;

while n < maxn
    gradf = [2 * (xx * exp(yy) - 2*yy*exp(-xx)) * (exp(yy) + 2 * yy * exp(-xx));
        2 * (xx * exp(yy) - 2*yy*exp(-xx)) * (xx * exp(yy) - 2 * exp(-xx))];
    y1 = xx - a*gradf(1);
    y2 = yy - a*gradf(2);
    er1 = y1 - xx;
    er2 = y2 - yy;
    er1 = norm(y1 - xx);
    er2 = norm(y2 - yy);
    ers = (er1 + er2) / 2;
    xx = y1;
    yy = y2;
    n = n + 1;
end
ers