class calculator:
    def sum(self,x,y):
        return x+y
    def sub(self,x,y):
        return x-y
    def mul(self,x,y):
        return x*y
    def div(self,x,y):
        return x/y
    def mod(self,x,y):
        return x%y
    def floor(self,x,y):
        return x//y
    def exp(self,x,y):
        return x**y
        
cal=calculator()
print("sum is:",cal.sum(4,5))
print("sub is:",cal.sub(5,6))
print("product is:",cal.mul(2,3))
print("division is:",cal.div(4,2))
print("remainder is:",cal.mod(6,3))
print("floor division is:",cal.floor(10,5))
print("exponent is:",cal.exp(2,3))