def say_digit(n,arr):
    if n==0:
        print(arr[0])
        return 
    a = n%10
    n = n//10
    say_digit(n,arr)
    print(f"{a} ---> {arr[a]}")

arr = ['zero','one','two','Three','Four','five','six','seven','Eight','nine']

say_digit(412,arr)