#! /usr/bin/python

import math

#ENTRADA 1: Definimos funciones extremos de la integral mas interna  
def c(t): r=t**2; return r;
def d(t): r=2*t; return r;

#ENTRADA 2: Funcion de f(x,y) a integrar
def f(x,y):
	r= (x**3) + (y*4);	
	return r;
	
#ENTRADA 3:
#Extremos a y b de la integral mas externa.
a=0; b=2; 
#Enteros positivos pares para subdividir los intervalos.
n=2**4; m=2**4;

#PASO1
h = (b-a)*(n**-1);
J1 = 0;	#terminos extremos
J2 = 0;	#terminos pares
J3 = 0;	#terminos impares

print ""
print "Valores aproximados de la integral doble dado por las sucesivas iteraciones"
print " "

#PASO 2
for i in range(1,n+1,1):
	#PASO 3
	x = a + (i*h);			#Metodo compuesto de Simpson para x.
	HX = (d(x) - c(x))/m;
	K1 = f(x,c(x)) + f(x,d(x));	#terminos extremos
	K2 = 0;				#terminos pares
	K3 = 0;				#terminos impares
	J = h*(J1+2*J2+4*J3)*(3**-1)	
	print "El valor aproximado de la integral es J"+str(i)+"= "+str(J)  	
	#PASO 4	
	for j in range(1,m,1):
		#PASO 5
		y = c(x) + j*HX;
		Q = f(x,y);
		#PASO 6
		if j%2==0:
			K2 += Q;
		else:
			K3 += Q;

	#PASO 7	
	L = (K1+2*K2+4*K3)*HX*(3**-1);
	
	#PASO 8	
	if i==0 or i==n:
		J1 += L;
	if i%2==0:
		J2 += L;
	elif i%2==1:
		J3 += L;
	
#PASO 9: La f
J = h*(J1+2*J2+4*J3)*(3**-1);

#PASO 10: Imprimir en consola el resultado aproximado de la integral
print ""
print "La integral doble tiene como valor aproximado: " + str(J);		
print ""
#Comparar con el valor analitico
def Error (valor,aprox):
	e_abs = math.fabs(valor - aprox)
	e_rel = e_abs/valor
	return [e_abs, e_rel]
	
print "El error absoluto es " + str(Error((32*(3**-1)),J)[0])
print "El error relativo es " + str(Error((32*(3**-1)),J)[1])

