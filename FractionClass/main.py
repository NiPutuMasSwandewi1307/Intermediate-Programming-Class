class Fraction :
    # Constructs a rational number initialized to zero or a user specified value
    def __init__(self, numerator = 0, denominator = 1) :

        # To ensure the method can be used to check the type of object referenced by a variable
        if (not isinstance(numerator, int) or not isinstance(denominator, int)) :
           raise TypeError ("The numerator and denominator must be integers.")
           
        # The denominator cannot be zero
        if denominator == 0:
            raise ZeroDivisionError("Denominator cannot be zero.")

            # Set the denominator to 1 if the rational number is 0
        if numerator == 0:
          self._numerator = 0
          self._denominator = 1
                          
            # Otherwise, store the rational number in reduced form
        else:
              # Determine the sign
              if (numerator < 0 and denominator >= 0 or numerator >= 0 and denominator < 0):
                sign = -1 
              else:
                sign = 1 
              
              # Reduce to smallest form
              a = abs(numerator)
              b = abs(denominator)
              while a% b != 0:
                tempA = a
                tempB = b
                a = tempB
                b = tempA % tempB

                self._numerator = abs(numerator) // b * sign
                self._denominator = abs(denominator) // b

    # Adds a fraction from this fraction
    def __add__(self, rhsValue):
      num = (self._numerator * rhsValue._denominator + self._denominator * rhsValue._numerator)
      den = self._denominator * rhsValue._denominator
      return Fraction(num, den)
              
    # Subtracts a fraction from this fraction
    def __sub__(self, rhsValue):
      num = (self._numerator * rhsValue._denominator - self._denominator * rhsValue._numerator)
      den = self._denominator * rhsValue._denominator
      return Fraction(num, den)

    # A fraction equals to this fraction
    def __eq__(self, rhsValue):
      return (self._numerator == rhsValue._denominator and self._denominator == rhsValue._numerator)

    # Determines if this fraction is less than another fraction
    def __lt__(self, rhsValue):
      return (self._numerator * rhsValue._denominator < self._denominator * rhsValue._numerator)
              
    # Determines if this fraction is not equal to another fraction
    def __ne__(self, rhsValue):
      return not self == rhsValue

    # Determines if this fraction is less than or equal to another fraction
    def __le__(self, rhsValue):
      return not rhsValue < self

    # Determines if this fraction is greater than another fraction
    def __gt__(self, rhsValue):
      return rhsValue < self

    # Determines if this fraction is greater than or equal to another fraction
    def __ge__(self, rhsValue):
      return not self < rhsValue

    # Gets a float representation of the fraction
    def __float__(self):
      return self._numerator / self._denominator

    # Gets a string representation of the fraction
    def __repr__(self):
      return str(self._numerator) + "/" + str(self._denominator)

