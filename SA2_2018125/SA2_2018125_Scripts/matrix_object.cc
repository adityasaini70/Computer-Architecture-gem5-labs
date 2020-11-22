#include "learning_gem5/SA2_2018125/matrix_object.hh"
#include <iostream>
#include "base/trace.hh"
#include "debug/MATRIX.hh"
#include "debug/RESULT.hh"
#include <string>
MatrixObject::MatrixObject(MatrixObjectParams *params) : 
	SimObject(params), event([this]{mainEvent();}, name())
{
    std::cout << "Matrix object constructed!" << std::endl;
}


void
MatrixObject::startup()
{

    schedule(event, 100);
}


double**
MatrixObject::inverse(){
   //The code is useable for 3x3 matrices only
   //Inverse(Matrix A)=adjoint(A)/determinant(A)
 
   //Finding determinant
   double determinant = 0;
   for(int row=0;row<this->matrix_size;row++){
    	determinant += this->input_matrix[0][row] * (this->input_matrix[1][(row+1)%this->matrix_size]*this->input_matrix[2][(row+2)%this->matrix_size]-this->input_matrix[1][(row+2)%this->matrix_size]*this->input_matrix[2][(row+1)%this->matrix_size]);
   }
   
   
   //Finding result by dividing adjoint by determinant
   
   double** ans=new double*[this->matrix_size];
   for(int i = 0; i<this->matrix_size;i++){
	ans[i]=new double[this->matrix_size];
   	for(int j=0;j<this->matrix_size;j++){
		double  adj  =	(this->input_matrix[(j+1)%3][(i+1)%3]*this->input_matrix[(j+2)%3][(i+2)%3]) - (this->input_matrix[(j+1)%3][(i+2)%3]*this->input_matrix[(j+2)%3][(i+1)%3]);
		ans[i][j] = adj/determinant;
	}
   }

   return ans;
}


void
MatrixObject::mainEvent()
{ 
   if(DTRACE(MATRIX)){
	   std::cout<<"Input Matrix:\n";
	   for(int i =0;i<this->matrix_size;i++){
	   	for(int j=0;j<this->matrix_size;j++){
			std::cout<<this->input_matrix[i][j]<<"\t";
		}
		std::cout<<"\n";
	   }
	   std::cout<<"Size = "<< this->matrix_size << "x" << this->matrix_size << "\n";

   }
   else if(DTRACE(RESULT)){
	   double** inverted_ans = inverse();
	   std::cout<<"Inverted matrix:"<<"\n";
	   for(int i = 0; i<this->matrix_size;i++){
       		for(int j=0;j<this->matrix_size;j++){
                	std::cout<< inverted_ans[i][j] <<"\t\t\t";
       		}
        	std::cout<<"\n";
  	   }
   }

}

MatrixObject*
MatrixObjectParams::create()
{
    return new MatrixObject(this);
}
