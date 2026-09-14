from functools import reduce
import time

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


