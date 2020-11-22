#ifndef __MATRIX_OBJECT__
#define __MATRIX_OBJECT__

#include "params/MatrixObject.hh"
#include "sim/sim_object.hh"

class MatrixObject : public SimObject
{
  private:
    int input_matrix[3][3] ={{1,2,1},{2,1,3},{4,5,1}};
    int matrix_size=3;
    void mainEvent();
    double** inverse();
    EventFunctionWrapper event;
  public:
    MatrixObject(MatrixObjectParams *p);
    void startup();
};

#endif
