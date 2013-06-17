# -*- coding=utf-8 *-*

class TestClass:
	def __init__(self, p1, p2, p3):
		self.p1 = float(p1)
		self.p2 = int(p2)
		self.p3 = str(p3)
		print "p1 = %s, p2 = %s, p3 = %s" % (p1, p2, p3)
		print "adder = %s" % self.adder()
		print "divider = %s" % self.divider()

	def adder(self):
		return self.p1 + self.p2

	def divider(self):
		return self.p1 / self.p2

	
tc = TestClass(1.2, 3, u"hola")

