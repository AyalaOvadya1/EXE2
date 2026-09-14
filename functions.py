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


