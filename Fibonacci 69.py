list_length, fib_list=69,[1,1];
[fib_list.append(fib_list[-2]+fib_list[-1])
 for _ in range(list_length)];
print(*fib_list)
