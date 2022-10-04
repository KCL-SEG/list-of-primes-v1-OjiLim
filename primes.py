"""List of prime numbers generator."""
import math
def primes(number_of_primes):
    list = Sieve_Of_Eratosthenes_Number_Of_Primes(number_of_primes)
    return list

#complicated way for learning syntax!!
def Sieve_Of_Eratosthenes(largestNumber):
    numbers = [True] * (largestNumber+1) #making list with all true values
    numbers[0] = False
    numbers[1] = False
    for i in range(2,math.ceil(largestNumber**0.5),1):
        if numbers[i] == True:
            for j in range(i**2,largestNumber,i): #removes numbers via i**2+ni where n is an integer
                numbers[j] = False
    primeNumbers = []
    for index, value in enumerate(numbers): #gets index of true values which equate to prime
        if value == True:
            primeNumbers.append(index)
    return primeNumbers

#Same as above but uses number of primes in list instead(Brute force method used, prime number theorem could be used as basis instead reducing complexity)
def Sieve_Of_Eratosthenes_Number_Of_Primes(numberOfPrimes):
    primeNumbers = []
    largestNumber = 2
    while len(primeNumbers) != numberOfPrimes:
        primeNumbers = []
        numbers = [True] * (largestNumber+1)
        numbers[0] = False
        numbers[1] = False
        for i in range(2,math.ceil(largestNumber**0.5),1):
            if numbers[i] == True:
                for j in range(i**2,largestNumber+1,i):
                    numbers[j] = False
        for index, value in enumerate(numbers):
            if value == True:
                primeNumbers.append(index)
        largestNumber+=1
    return primeNumbers
