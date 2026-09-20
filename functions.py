from functools import reduce
import time
from datetime import datetime, timedelta
import math

##1

#1.1
linear_func = lambda x: x/2+2

newlist = list(map(linear_func, range(0,10001)))

#1.2
total = reduce(lambda x,y : x+y, newlist)

#1.3
# --- מדידת זמן בשיטה פונקציונלית ---
start_func = time.time()
sum_functional = reduce(lambda x,y : x+y, newlist)
end_func = time.time()
time_functional = end_func - start_func

# --- מדידת זמן בשיטה אימפרטיבית (לולאה) ---
start_imp = time.time()
sum_imperative = 0
for x in newlist:
    sum_imperative += x
end_imp = time.time()
time_imperative = end_imp - start_imp

#print(f"זמן ריצה פונקציונלי: {time_functional:.6f} שניות")
#print(f"זמן ריצה אימפרטיבי: {time_imperative:.6f} שניות")

#1.4
everything = reduce(lambda x,y : x+linear_func(y) , range(0, 10001) ,0)


##2

my_list = range(1, 1001)
odds  = list(filter(lambda x: x%2==1, my_list))
evens = list(filter(lambda x: x%2==0, my_list))

#2.1
# למבדה לזוגיים: מכפלת המצטבר באיבר הבא
even_lambda = lambda x, y: x * y

# למבדה לאי-זוגיים: חישוב ליניארי על המצטבר + האיבר הבא
odd_lambda = lambda x, y: (x / 2 + 2) + y

#2.2
even_func = reduce(even_lambda, evens , 1)
odd_func = reduce(odd_lambda, odds , 0)

#2.3
final_sum = reduce(lambda x,y : x+y , [even_func,int(odd_func)])


##3

#3.א
def is_armstrong(n):
    k = len(str(n))
    digits_sum = sum(int(digit)**k for digit in str(n))
    return digits_sum == n

#3.ב
def armstrong_range(n1, n2):
    return list(filter(is_armstrong, range(n1, n2+1)))

#3.ג
def main():
    my_input = input("Enter a number:\n")
    if not my_input.isdigit() or int(my_input)<=0:
        print("invalid input")
    else:
        print(armstrong_range(1,int(my_input)))

if __name__ == '__main__':
        main()

##4

#4.א
def dates(my_date, num1, num2):
    start_date = datetime.strptime(my_date, "%d/%m/%Y")
    return list(map(lambda i: (start_date + timedelta(days=i * num2)).strftime("%d/%m/%Y"),
        range(num1),))

##5
#5.א
def power_function(exponent):
    return lambda base: base**exponent

#5.ב
def get_power_functions(n):
    return map(power_function, range(n))


if __name__ == "__main__":
    n = int(input("Enter number of powers:\n"))
    result = get_power_functions(n)

    print(type(result))

    base = int(input("Enter base:\n"))

    print(tuple(map(lambda f: f(base), result)))


#5.ג
def taylor_e(x, n):
    terms = map(
        lambda k, f: f(x) / math.factorial(k), range(n), get_power_functions(n)
    )
    return sum(terms)