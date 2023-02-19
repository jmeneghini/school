#include <blitz/array.h>
#include <gnuplot-iostream.h>
#include <math.h>


using namespace blitz;
using namespace std;


extern "C" double* euler(double x0, double y0, double xf, double h){
    int N = (xf-x0)/h;
    double *x = new double[N];
    double *y = new double[N];
    x[0] = x0;
    y[0] = y0;
    for (int i=1; i<N; i++){
        x[i] = x[i-1] + h;
        y[i] = y[i-1] + h*(-2*y[i-1] + -1*x[i-1]);
    }
    return y;

}
