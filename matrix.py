import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
      
        if self.h == 1:
            return self.g[0]
        if self.h == 2:
            return  (self.g[0][0]*self.g[1][1]) -  (self.g[0][1]*self.g[1][0])
        if self.h == 3:
            return (self.g[0][0]*self.g[1][1]*self.g[2][2]) + (self.g[0][1]*self.g[1][2]*self.g[2][0]) + \
                   (self.g[0][2]*self.g[1][0]*self.g[2][1]) - (self.g[0][2]*self.g[1][1]*self.g[2][0]) - \
                   (self.g[0][1]*self.g[1][0]*self.g[2][2]) - (self.g[0][0]*self.g[1][2]*self.g[2][1])
        
        
                                                                                                          
                
                
        
        
    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")
     
        
        toni = 0
        for i in range(self.w):
            toni += self.g[i][i]
        return toni
            
    

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

       
        determinant = self.determinant()
        inv = []
        if self.w == self.h == 1:
            inv.append([ 1 / self.g[0][0]])
            return Matrix(inv)
        invv = zeroes(self.h, self.w)         
        if self.w == self.h == 2:
            alpha = self.g[0][0]
            beta = self.g[0][1]
            delta = self.g[1][0]
            gama = self.g[1][1]
        
            invv[0][0] = (1/ determinant) * gama
            invv[0][1] = (1/determinant) * (-1 * beta)
            invv[1][0] = (1/determinant) * (-1 * delta)
            invv[1][1] = (1/determinant) * alpha
            
        return invv
    
    
          
        
            

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        trans = zeroes(self.w, self.h)
        for j in range(self.w):
            for i in range(self.h):
                trans[i][j] = self.g[j][i]
        return trans
                

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        ad = zeroes(self.h, self.w)
        for i in range(self.h):
            for j in range(self.w):
                ad[i][j] = self[i][j] + other[i][j]
        return ad

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
       
        #
        n = zeroes(self.h, self.w)
        for i in range(self.h):
            for j in range(self.w):
                n[i][j] = self.g[i][j] * -1
        return n
               
        return self
    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #   
       
        #
        
        sub  = zeroes(self.h, self.w)
        for i in range(self.h):
            for j in range(self.w):
                sub[i][j] = self.g[i][j] -  other.g[i][j]
        return sub

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
       
        #
        multi = zeroes(self.h, other.w)
        for i in range(multi.h):
            for j in range(multi.w):
                partial_res = 0
                for a in range(self.w):
                    partial_res += self[i][a]*other[a][j]
                multi[i][j] = partial_res
        return multi
       
        
          
    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            rmulti = zeroes(self.h, self.w)
            for i in range(self.h):
                for j in range(self.w):
                    rmulti[i][j] = self.g[i][j] * other
            return rmulti

            
