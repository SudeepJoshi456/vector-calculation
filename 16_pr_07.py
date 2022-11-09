class Vector:
    def __init__(self, vec):
        self.vec = vec
    
    def __str__(self):
        str1 = ""
        index = 0
        for i in self.vec:
            str1 += f" {i}a{index} +"
            index += 1
        return str1[:-1]

    def __add__(self,vec2):
        if len(self.vec) == len(vec2.vec):
            newList = []
            for i in range(len(self.vec)):
                newList.append(self.vec[i] + vec2.vec[i])
            return Vector(newList)
        else:
            return "addition failed! length of these vectors is not same"
    
    def __mul__(self,vec2):
        sum = 1
        if len(self.vec) == len(vec2.vec):
            for i in range(len(self.vec)):
                sum += self.vec[i] * vec2.vec[i]
            return sum
        else:
            return "multiplication not possible"
    
    def __len__(self):
            return len(self.vec)
        


v1 = Vector([1,4])
v2 = Vector([2, 8])
print(v1+v2)
print(v1*v2)
print(len(v1))
print(len(v2))










