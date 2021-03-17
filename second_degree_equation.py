# second_degree_equation.py
import math
print("Please Enter the coefficients in role :")
a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))
delta = (b**2-4*a*c)
if delta == 0:
   x = (-b)/(2*a)
   print("This equation has got 1 real root(Double root):")
   print("x = ",x)
else :
   if delta < 0:
       print("This equation does not have any real root.")

   else :
       x_alfa = (-b-(math.sqrt(delta)))/(2*a)
       x_beta = (-b+(math.sqrt(delta)))/(2*a)
       print("This equation ha got 2 real roots:")
       print("x(1) = ",x_alfa)
       print("x(2) = ",x_beta)
