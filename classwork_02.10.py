# class Polygon:
#     def __init__(self, no_of_sides):
#         self.n = no_of_sides
#         self.sides = [0 for i in range(no_of_sides)]

#     def inputSides(self):
#         self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]

#     def dispSides(self):
#         for i in range(self.n):
#             print("Side",i+1,"is",self.sides[i])
# class Triangle(Polygon):
    # def __init__(self):
#         Polygon.__init__(self,3)  #super().__init__(3) 

#     def findArea(self):
#         a, b, c = self.sides
#         s = (a + b + c) / 2
#         area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
#         print('The area of the triangle is %0.2f' %area)
class Tvaryna:
    def __init__(self, holos):
        self.hol = holos
    def inputholos(self):
        self.hol = input("Enter holos: ")
    def disphol(self):
        print("I'm " + self + "my holos: "+ self.hol)

cat = Tvaryna()
cat.inputholos()
cat.disphol()
    

