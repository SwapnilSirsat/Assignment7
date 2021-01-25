import numpy as np
import matplotlib.pyplot as plt
import math


def line_gen(A,B):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB


def circ_gen(O,r):
	len = 50
	theta = np.linspace(0,2*np.pi,len)
	x_circ = np.zeros((2,len))
	x_circ[0,:] = r*np.cos(theta)
	x_circ[1,:] = r*np.sin(theta)
	x_circ = (x_circ.T + O).T
	return x_circ

#cordinates of the diameter whould be as
P = np.array([-7,0])
Q = np.array([7,0])
PO_mid = np.array([-3.5,0])
OQ_mid = np.array([3.5,0])

#calculation for the points of contact of the tangents
#the point of contact will be the point of intersection of the circles
#therefore we can obtain them by solving the system of eqution of circles
#the eqution of circles are as
# x^2 + y^2 = 9 and (x+3.5)**2 + y**2 = 3.5**2
#on putting first equation in second equation we get
x_1 = -9/7
y_1 = math.sqrt(9-((x_1)**2))
y_2 = -math.sqrt(9-((x_1)**2))

#similary for Q
x_2 = 9/7
y_3 = math.sqrt(9-((x_2)**2))
y_4 = -math.sqrt(9-((x_2)**2))

 #therefore the coordinates are
print(x_1," ",y_1)
print(x_1," ",y_2)
print(x_2," ",y_3)
print(x_2," ",y_4)




T_1 = np.array([x_1,y_1])
T_2 = np.array([x_1,y_2])
T_3 = np.array([x_2,y_3])
T_4 = np.array([x_2,y_4])


x_PQ = line_gen(P,Q)
x_PT_1 = line_gen(P,T_1)
x_PT_2 = line_gen(P,T_2)
x_QT_3 = line_gen(Q,T_3)
x_QT_4 = line_gen(Q,T_4)

#given Diameter of the circel is 6.1
r = 3
O = np.array([0,0])
x_circ = circ_gen(O,r)
x_circ_PO = circ_gen(PO_mid,3.5)
x_circ_OQ = circ_gen(OQ_mid,3.5)

plt.plot(x_circ[0,:],x_circ[1,:])
plt.plot(x_circ_PO[0,:],x_circ_PO[1,:])
plt.plot(x_circ_OQ[0,:],x_circ_OQ[1,:])
plt.plot(x_PQ[0,:],x_PQ[1,:])
plt.plot(x_PT_1[0,:],x_PT_1[1,:])
plt.plot(x_PT_2[0,:],x_PT_2[1,:])
plt.plot(x_QT_3[0,:],x_QT_3[1,:])
plt.plot(x_QT_4[0,:],x_QT_4[1,:])
plt.plot(P[0],P[1],'o')
plt.plot(Q[0],Q[1],'o')
plt.plot(O[0],O[1],'o')
plt.plot(PO_mid[0],PO_mid[1],'o')
plt.plot(OQ_mid[0],OQ_mid[1],'o')
plt.plot(T_1[0],T_1[1],'o')
plt.plot(T_2[0],T_2[1],'o')
plt.plot(T_3[0],T_3[1],'o')
plt.plot(T_4[0],T_4[1],'o')
plt.text(O[0]*(1+0.1),O[1]*(1+0.1),"O")
plt.text(P[0]*(1+0.1),P[1]*(1+0.1),"P")
plt.text(Q[0]*(1+0.1),Q[1]*(1+0.1),"Q")
plt.text(PO_mid[0]*(1+0.1),PO_mid[1]*(1+0.1),"R")
plt.text(OQ_mid[0]*(1+0.1),OQ_mid[1]*(1+0.1),"S")
plt.text(T_1[0]*(1+0.1),T_1[1]*(1+0.1),"T_1")
plt.text(T_2[0]*(1+0.1),T_2[1]*(1+0.1),"T_2")
plt.text(T_3[0]*(1+0.1),T_3[1]*(1+0.1),"T_3")
plt.text(T_4[0]*(1+0.1),T_4[1]*(1+0.1),"T_4")
plt.grid()
plt.axis("equal")
plt.show()
