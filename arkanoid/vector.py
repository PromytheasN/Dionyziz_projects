class Vector:
    """Represent a vector in multidimensional space."""

    def __init__(self, d):
        """Create d-dimensional vector of zeros or of certain dimentional coordinates"""
        try:
            if int(d):
                self._coords = [0]*d
        except:
            if list(d):
                self._coords = d

    def __len__(self):
        """Return the dimension of the vector."""
        return len(self._coords)

    def __getitem__(self,j):
        """Return the coordinate of vector."""
        return self._coords[j]

    def __setitem__(self, j , val):
        """Set the coodrinate of vector to given value."""
        self._coords[j] = val

    def __sub__(self, other):
        """Return sub of two vectors."""
        if len(self) != len(other):
            raise ValueError("dimensions must agree!")
        result = Vector(len(self))
        for i in range(len(self)):
            result[i] = self[i] - other[i]
        return result    

    def __add__(self, other):
        """Return sum of two vectors."""
        if len(self) != len(other): #relies on __len__ method
            raise ValueError("dimensions must agree!")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j]=self[j] + other[j]
        return result

    def __eq__(self, other):
        """Return True if vector has same coordinates as other."""
        return self._coords == other._coords

    def __ne__(self,other):
        """Return True if vector differs from other."""
        return not self == other #rely on existing __eq__ definition

    def __str__(self):
        """Produce string representation of vector"""
        return "<" + str(self._coords)[1:-1] + ">" # adapt list representation

    def __neg__(self):
        """Return new Vector instance whose coordinates are all negated values of the original ones"""
        result = Vector(len(self)) + self
        for i in range(len(self)):
            result[i] *= -1
        return result

    def __radd__(self, other):
        """Returns Vectors sum with other coordinates of object with same dimentions"""
        return self.__add__(other)

    def __mul__(self, other):
        """Return new Vector instance whose coordinates are x(other) times of the original"""
        if type(other) == int or type(other) == float:
            result = Vector(len(self))
            for i in range(len(self)):
                result[i] = self[i]*other
            return result
        else:
            len(other)
            print(len(other), len(self))
            if len(other) != len(self):
                raise ValueError("Vector's dimentions do not match")
            sum = 0
            for i in range(len(self)):
                sum += self[i]*other[i]
            return sum

     def __rmul__(self, other):
        """Return new vector instance whose coordinates are x times of the original with the first factor being an x value and second the Vector"""
        return self.__mul__(other)

    def __mul__(self, other):
        """Return a scalar that represents the dot product of 2 vectors"""
        result = Vector(len(self)) + self
        for i in range(len(self)):
            result[i] = result[i] * other[i]
        return result