"""
1. Question
https://rosalind.info/problems/iprb/

in a given population, where k,m,n represent the total population k +m +n ogarnims /
- k individuals are homozygous dominent for the brown eye color alle
- m are Heterozygous for the brown eye color allet 
- n are homozygous recessive(show blue eye color)

What is The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele(*) 
(and thus displaying the dominant phenotype). Assume that any two organisms can mate.

Note :
- Homozygous dominent mean they have one dominant allele (H) only
- Heterozygous mean they have one dominant allele (H) and one recessive allele (h) 
- homozygous recessive mean they have one recessive allele (h) only
The individual possessing a dominant allele is either homozygous dominent or Heterozygous(*) 

2. Solution
About the probability of offspring is homozygous dominent: 
- if homozygous dominent mate homozygous dominent
	 H	H
H	HH	HH
H	HH	HH
=> The probability of offspring being homozygous dominant (HH) is 100%
- if homozygous dominent mate Heterozygous
	 H	H
H	HH	HH
h	Hh	Hh
=> The probability of offspring being homozygous dominant (HH) is 0.5
- if Heterozygous meet Heterozygous
	 H	h
H	HH	Hh
h	Hh	hh
=> The probability of offspring being homozygous dominant (HH) is 0.25

Sumary:
Let X = the r.v. associated with the first person randomly selected
Let Y = the r.v. associated with the second person randomly selected without replacement
Then:
k = f_d => p(X=d) = k/a => p(Y=d| X=d) = (k-1)/(a-1) ,
                           p(Y=h| X=d) = (m)/(a-1) ,
                           p(Y=r| X=d) = (n)/(a-1)
                           
m = f_h => p(X=h) = m/a => p(Y=d| X=h) = (k)/(a-1) ,
                           p(Y=h| X=h) = (m-1)/(a-1)
                           p(Y=r| X=h) = (n)/(a-1)
                           
n = f_r => p(X=r) = n/a => p(Y=d| X=r) = (k)/(a-1) ,
                           p(Y=h| X=r) = (m)/(a-1) ,
                           p(Y=r| X=r) = (n-1)/(a-1)
Now the joint would be:(**)
                            |    offspring possibilites given X and Y choice
-------------------------------------------------------------------------
X Y |  P(X,Y)               |   d(dominant)     h(hetero)   r(recessive)
-------------------------------------------------------------------------
d d     k/a*(k-1)/(a-1)     |    1               0           0
d h     k/a*(m)/(a-1)       |    1/2            1/2          0
d r     k/a*(n)/(a-1)       |    0               1           0
                            |
h d     m/a*(k)/(a-1)       |    1/2            1/2          0
h h     m/a*(m-1)/(a-1)     |    1/4            1/2         1/4
h r     m/a*(n)/(a-1)       |    0              1/2         1/2
                            |
r d     n/a*(k)/(a-1)       |    0               0           0
r h     n/a*(m)/(a-1)       |    0               1/2        1/2
r r     n/a*(n-1)/(a-1)     |    0               0           1

Here what we don't want is the element in the very last column where the offspring is completely recessive.
so P = 1 - P(offspring=recessive)


- prob_kk(two type k mate) : (k / total_population) * ((k - 1) / (total_population - 1))
- prob_km(type k mate type m) : (k / total_population) * (m / (total_population - 1)) + (m / total_population) * (k / (total_population - 1))
- prob_kn(type k mate type n) : (k / total_population) * (n / (total_population - 1)) + (n / total_population) * (k / (total_population - 1))
- prob_mm(two type m mate) : (m / total_population) * ((m - 1) / (total_population - 1))
- prob_mn(type m mate type n) : (m / total_population) * (n / (total_population - 1)) + (n / total_population) * (m / (total_population - 1))

"""

def solution(k, m, n):
    total_population = k + m + n

    # Calculate the probabilities for each scenario
    # prob_kk = (k / total_population) * ((k - 1) / (total_population - 1))
    # prob_km = (k / total_population) * (m / (total_population - 1)) + (m / total_population) * (k / (total_population - 1)) 
    # prob_kn = (k / total_population) * (n / (total_population - 1)) + (n / total_population) * (k / (total_population - 1))
    prob_mm = (m / total_population) * ((m - 1) / (total_population - 1)) 
    prob_mn = (m / total_population) * (n / (total_population - 1)) 
    prob_nm = (n / total_population) * (m / (total_population - 1)) 
    prob_nn = (n / total_population) * ((n - 1) / (total_population - 1))



    # Calculate the overall probability of producing an individual completely recessive(take a look at the table **)
    prob_offspring_recessive = prob_mm * 0.25 + prob_mn * 0.5 + prob_nm * 0.5  +  prob_nn * 1

    prob_homozygous_dominent_or_heterozygous = 1 - prob_offspring_recessive
    return prob_homozygous_dominent_or_heterozygous




# Test the function with sample inputs
k = 29
m = 48
n = 68
# the expected result is 0.598467
print(solution(k, m, n))  # Output the overall probability
