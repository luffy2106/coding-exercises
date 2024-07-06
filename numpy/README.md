# numpy_datascience

The Top 10 NumPy Functions You need to know

#### 1. Create array from list
```
my_list = [1, 2, 3, 4, 5]
my_array = np.array(my_list)
```

#### 2. np.arange(): Generate Sequences Like a Pro
```
my_range = np.arange(0, 10, 2) # Creates [0, 2, 4, 6, 8]
```

#### 3. Create matrix of zero and one
```
zeros_array = np.zeros((2, 3)) # Creates a 2x3 array of zeros
ones_array = np.ones((3, 2)) # Creates a 3x2 array of ones
```

#### 4. np.linspace(): Precision in Sequence Generation
Create arrays with finely spaced values using np.linspace(). Perfect for creating smooth, continuous ranges for your data.
```
linspace_array = np.linspace(0, 1, 5) # Creates [0.0, 0.25, 0.5, 0.75, 1.0]
```

#### 5. np.random.rand(): Embrace Randomness
```
random_array = np.random.rand(3, 3) # Creates a 3x3 array of random numbers
```

#### 6. np.shape(): Unravel the Dimensions
```
my_array = np.array([[1, 2], [3, 4]])
shape = np.shape(my_array) # Returns (2, 2)
```

#### 7. np.reshape(): Shape-Shifting Arrays
Mold your data into the desired shape using np.reshape(). Perfect for rearranging data for modeling and analysis.
```
my_array = np.arange(1, 10) # Creates [1, 2, 3, …, 9]
reshaped_array = np.reshape(my_array, (3, 3))
```

#### 8. Slicing and Dicing: The array[start:end] Technique
slicing and dicing arrays to extract precisely the data you need
```
my_array = np.array([1, 2, 3, 4, 5])
sliced_array = my_array[1:4] # Creates [2, 3, 4]
```
#### 9. np.concatenate(): Unite Arrays Seamlessly
Combine arrays effortlessly with np.concatenate()
```
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
concatenated_array = np.concatenate((array1, array2))
```

#### 10. Element-Wise Operations
Add, subtract, multiply, and divide arrays element by element, giving you fine-grained control over your data.
```
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
sum_array = array1 + array2 # Element-wise addition
product_array = array1 * array2 # Element-wise multiplication
```
- np.power(arr, n)
```
arr = np.array([1,2,3,4,5]) 
# for finding an array raised to some power
print(np.power(arr, 3))  #  [  1   8  27  64 125]
arr1 = np.array([1,2,3,4,5]) 
print(np.power(arr, arr1)) #  [   1    4   27  256 3125]
```
- Addition/Subtraction one by one
```
# for adding subtracting
print(np.add(arr,[5,4,3,2,1])) #  [6 6 6 6 6]
print(np.subtract(arr,[5,4,3,2,1]))  #  [-4 -2  0  2  4]
```
-  Multiplication 
```
#for multiplying
print(3*a)  #  [ 3  6  9 12 15]
```

#### 11. np.unique Operations
Get the unique value and its index in an array
```
arr = np.array([2, 3, 2, 4, 5, 3, 8])
unique_values = np.unique(arr)
print(unique_values) # return (array([2, 3, 4, 5, 8]), array([0, 1, 3, 4, 6]))
```

#### 12. Dot product 
For example, if a = [a1, a2, a3] and b = [b1, b2, b3], the dot product (a · b) is computed as:
a · b = a1 * b1 + a2 * b2 + a3 * b3
```
print(np.dot([[1,2],[3,4]],[5,6]))  #  [17 39]
```

#### 13. Cross product
The cross product of two vectors a and b is denoted by a x b and is calculated using the following formula:

a x b = (a2 * b3 - a3 * b2)i + (a3 * b1 - a1 * b3)j + (a1 * b2 - a2 * b1)k

where i, j, and k are the unit vectors along the x, y, and z axes respectively.
```
#cross product
print(np.cross([1,2,3],
               [4,5,6]))  
# the result is [-3  6 -3]
```
Here's a breakdown of how the result [-3, 6, -3] is obtained:

Given vectors a = [1, 2, 3] and b = [4, 5, 6], the cross product operation can be calculated as follows:

1. Calculate the cross product formula for each component:
- i component: (2 * 6) - (3 * 5) = 12 - 15 = -3
- j component: (3 * 4) - (1 * 6) = 12 - 6 = 6
- k component: (1 * 5) - (2 * 4) = 5 - 8 = -3
2. Combine the results into a new vector:
- The cross product of vectors [1, 2, 3] and [4, 5, 6] is [-3, 6, -3].

Therefore, when you run print(np.cross([1, 2, 3], [4, 5, 6])), the output will be [-3, 6, -3].

#### 14. Broadcasting
Broadcasting is a powerful feature in NumPy that allows arrays of different shapes to be combined together for arithmetic operations. This eliminates the need for explicit loops and makes the code more concise and readable.

Here's how broadcasting works in NumPy:

1. Rule 1: Dimensions Compatibility
- If the arrays have a different number of dimensions, the shape of the array with fewer dimensions is padded with ones on its left side.
- The dimensions are then compared element-wise, starting from the trailing dimensions. The two dimensions are compatible when:
* They are equal, or
*  One of them is 1.
2. Rule 2: Array with Size 1
If one of the arrays has a size of 1 in a particular dimension, it "broadcasts" across that dimension to match the size of the other array.

3. Broadcasting Example
```
import numpy as np

a = np.array([1, 2, 3])  # Shape: (3,)
b = np.array([[4], [5], [6]])  # Shape: (3, 1)

result = a * b
print(result)
```
In this example, even though a and b have different shapes, broadcasting allows us to multiply them element-wise. The array b is broadcasted to shape (3, 3) to match the shape of a. The result will be
```
[[ 4  8 12]
 [ 5 10 15]
 [ 6 12 18]]
```


Reference :
```
https://www.interviewbit.com/courses/data-science-and-machine-learning/data-analysis/numpy/ 
```
```
https://medium.com/@trilogicalshelp/data-science-essentials-the-top-10-numpy-functions-you-cant-ignore-7a8a3b5c42a3
```