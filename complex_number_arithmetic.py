from __future__ import division
import math


class complex:
	"""(higher)arithmetic with complex numbers"""


	def __init__(self, complex):
		self.real, self.imag = map(float, complex.split())


	def __add__(self, other):
		real = self.real + other.real
		imag = self.imag + other.imag

		return self.result(real, imag)  


	def __sub__(self, other):
		real = self.real - other.real
		imag = self.imag - other.imag

		return self.result(real, imag)  


	def __mul__(self, other):
		#(a+bi)(c+di) = (ac-bd) + (ad+bc)i

		real = (self.real * other.real) - (self.imag * other.imag)
		imag = (self.real * other.imag) + (self.imag * other.real)

		return self.result(real, imag)  


	def __truediv__(self, other):
		""" 
		multiply conjugate of devisor (other) in numerator and denominator of fraction,
		the numerator contains both the real part and the imaginary part,
		but both are divided by the denominator

		# (a + bi)(a - bi) = a^2 + b^2
		# (2 + 3i)(4 + 5i) = (8 + 10i + 12i + 15(i^2)) = (-7 + 22i)
		"""

		product_real = (self.real * other.real) - (self.imag * (-other.imag))
		product_imag = (self.real * (-other.imag)) + (self.imag * other.real)
		denom = other.real**2 + other.imag**2

		real = product_real / denom
		imag = product_imag / denom

		return self.result(real, imag) 


	def __mod__(self, other):
		""" 
		modulus of a complex number is different from regular mod in the way that
		you just use pythagorean theorm on the complex number:
		z = 4 + 3i
		mod(z) = sqrt(4^2 + 3^2)
		i.e. you find the length of the complex number
		"""

		mod = math.sqrt((self.real**2 + self.imag**2))
		return "%.2f" % mod


	def result(self, real, imag):
		epsilon = 0.009

		if (imag > 0 and imag < epsilon) or imag == 0:
			result = "%.2f" % real

		elif (real > 0 and real < epsilon) or real == 0:
			result = "%.2fi" % imag
		
		elif imag < 0:
			result = "%.2f - %.2fi" % (real, abs(imag))

		else:
			result = "%.2f + %.2fi" % (real, imag)

		return result


complex_in1 = "2 55"
complex_in2 = "-56 6"
# complex_in1 = raw_input()
# complex_in2 = raw_input()

complex1 = complex(complex_in1)
complex2 = complex(complex_in2)

print complex1 + complex2
print complex1 - complex2
print complex1 * complex2
print complex1 / complex2
print complex1 % complex1
print complex2 % complex2
