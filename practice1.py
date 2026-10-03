numbers =[]
for i in range(5):
    x=float(input("Enter number:"))
    numbers.append(x)

sum=sum(numbers)
print("Sum:",sum)
avg=sum/len(numbers)
print("Average:",avg)
max=max(numbers)
print("Largest value:",max)
min=min(numbers)
print("Least value:",min)