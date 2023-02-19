using namespace std;

double dydx(double x, double y){
    return -x*y;
}
extern "C" double* rk4(double x0, double y0, double xf, double h) {
    int N = (xf - x0) / h;
    double *x = new double[N];
    double *y = new double[N];
    x[0] = x0;
    y[0] = y0;
    for (int i = 1; i < N; i++) {
        x[i] = x[i - 1] + h;
        double k1 = dydx(x[i - 1], y[i - 1]);
        double k2 = dydx(x[i - 1] + 0.5 * h, y[i - 1] + 0.5 * h * k1);
        double k3 = dydx(x[i - 1] + 0.5 * h, y[i - 1] + 0.5 * h * k2);
        double k4 = dydx(x[i - 1] + h, y[i - 1] + h * k3);
        y[i] = y[i - 1] + h / 6.0 * (k1 + 2.0 * k2 + 2.0 * k3 + k4);
    }
    return y;
}



