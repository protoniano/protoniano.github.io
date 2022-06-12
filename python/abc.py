class Mueble:

    def __init__(self):
        self.nombreU = 'tenedor'

class Mesa(Mueble):


    def cosas(self):
        print('En esta mesa hay: '+self.nombreU)


#print('this is a {}'.format(input()))
for x in range(1, 11):
    print('{0} {1:3d} {2:4d}'.format(x, x*x, x*x*x))