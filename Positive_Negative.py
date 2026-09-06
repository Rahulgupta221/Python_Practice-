num = int(input("Enter Your Number: "))
if num < 0:
    print(f"{num} Sorry,does not exist negative numbers")
elif num == 0:
    print(f"{num} The Number is Neutral")
else:
    print(f"{num} The Number is Positive")