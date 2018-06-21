# Kip Fletcher   Math 4330   6/18/2018
# Quiz 3

# dot returns the dot product of two vectors.
def dot(vector01, vector02):
    '''
    This function takes two compatible vectors as its arguments and returns
    their dot product. It first uses an if-else statement to verify that both
    vectors are vectors. It utilizes an if-else statement to determine if the two
    vectors are compatible and a for loop computes the dot product of the two
    vectors. If the two vectors are not compatible it returns "Invalid
    Input."
    '''
    dot_prod = 0

    if type(vector01) != list or type(vector02) != list:
        print("Invalid Input")

    if len(vector01) == len(vector02):
        for i in range(len(vector01)): 
            dot_prod += vector01[i]*vector02[i]
        return dot_prod
    else:
        print("Invalid Input") 
        return None
    
# These are test variables initialized for the dot function.

testVector1a = [1,3,7]
testVector1b = [2,4,1]

testVector2a = [3,6]
testVector2b = [1,5]

testVector3a = [1,3,4]
testVector3b = [2,7]

#These are test cases for the dot function with only one in use at a time.

print(dot(testVector1a,testVector1b))
#print(dot(testVector2a,testVector2b))
#print(dot(testVector3a,testVector3b))
####################################################################################################

# vecSubtract returns the difference of two vectors as a vector.
def vecSubtract(vector01,vector02):
    '''
    This function takes two compatibe vectors as its arguments, subtracts them, and
    returns the new vector. It first uses an if-else statement to verify that both
    vectors are vectors. It uses an if-else statement to determine if the two vectors
    are compatible and a for loop to compute the difference between the two vectors. With each
    iteraion the for loop stores the differences in new_vec. If the two vectors are not compatible
    the function returns "Invalid Input." 
    '''
    new_vec = []

    if type(vector01) != list or type(vector02) != list:
        print("Invalid Input")

    if len(vector01) == len(vector02):
        for i in range (len(vector01)):  
            new_vec.append(vector01[i] - vector02[i]) 
        return new_vec
    else:
        print("Invalid Input")  
        return None

# These are test variables initialized for the vecSubtract function.

testVector4a = [2,-4,6]
testVector4b = [1,7,0]

testVector5a = [5,8]
testVector5b = [-1,4]

testVector6a = [1,2]
testVector6b = [3,6,0]

#These are test cases for the vecSubtract function with only one in use at a time.

print(vecSubtract(testVector4a,testVector4b))
#print(vecSubtract(testVector5a,testVector5b))
#print(vecSubtract(testVector6a,testVector6b))
###################################################################################################

# scalarVecMulti returns the product of a scalar and a vector.
def scalarVecMulti(scalar,vector):
    '''
    This function takes a scalar and a vector as its arguments, multiplies them, and returns
    the product as a new vector. It uses a for loop to compute each element of the new vector
    and store that element in new_vec with each iteration.
    '''
    new_vec = []
    
    for i in vector:  
         new_vec.append(i * scalar) 
    return new_vec

# These are test variables initialized for the scalarVecMulti function.

testScalar7 = 2
testVector7 = [2,4,6]

testScalar8 = 1
testVector8 = [3,5]

testScalar9 = [3,5,"sweet"]
testVector9 = [4,7,3,9,2]

#These are test cases for the scalarVecMulti function with only one in use at a time.

print(scalarVecMulti(testScalar7,testVector7))
#print(scalarVecMulti(testScalar8,testVector8))
#print(scalarVecMulti(testScalar9,testVector9))
###################################################################################################

# infNorm returns the infinity norm of a vector.
def infNorm(vector):
    '''
    This function takes a vector as its argument and returns its infinity norm. It uses a for loop
    to determine the vector element of greatest absolute value by comparison and returns the element
    of greatest absolute value.
    '''
    new_vec = abs(vector[0])

    for i in range(len(vector)): 
        if new_vec < abs(vector[i]):
            new_vec = abs(vector[i])
    return new_vec

# These are test variables initialized for the infNorm function.

testVector10 = [8,22,9]
testVector11 = [-7,0]
testVector12 = ["fantastic",4,8]

#These are test cases for the infNorm function with only one in use at a time.

print(infNorm(testVector10))
#print(infNorm(testVector11))
#print(infNorm(testVector12))
###################################################################################################

# normalize returns the normalized vector with respect to the infinity norm.
def normalize(vector):
    '''
    This function take a vector as an argument and normalizes the vector by multiplying
    it by the reciprocal of its infinity norm. It uses the function infNorm to determine the
    infinity norm and stores the reciprocal of the infinity norm in variable scalar. It then uses
    the function scalarVecMulti to multiply the variable scalar by the vector and return the normalized
    vector.
    '''
    scalar = 1/(infNorm(vector)) 

    return scalarVecMulti(scalar,vector) # uses the infinity norm reciprocal as a scalar to normalize the vector.

# These are test variables initialized for the normalize function.

testVector13 = [13,6,4]
testVector14 = [-9,8]
testVector15 = [7,2,"great"]

#These are test cases for the hormalize function with only one in use at a time.

print(normalize(testVector13))
#print(normalize(testVector14)) 
#print(normalize(testVector15))
