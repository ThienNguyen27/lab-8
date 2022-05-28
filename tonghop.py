def checknumber(user_input): # hàm kiểm tra số
    number=["0","1","2","3","4","5","6","7","8","9","."]
    low = user_input.lower() 
    num=0  
    for input_length in range(len(user_input)+1): 
        for cut_place in range(1,input_length+1): 
            digit_cut=slice(cut_place-1,cut_place)
            if low[digit_cut] not in number:
                num=1
    return num

def is_int(user_input): # hàm kiểm tra số nguyên
    if float(user_input)%1==0:
        return print(int(user_input),"is an integer")
    else:
        return print(user_input, "is not an integer")

def is_prime(num): #hàm kiểm tra snt
    int(num)
    so_uoc=0
    for i in range (1,num+1): 
        if num%i==0:
            so_uoc+=1
    if num<2: 
        return print(f"{num} is not a prime")
    else: 
        if so_uoc==2: 
            return print(f"{num} is a prime")
        elif so_uoc>2: 
            return print(f"{num} is not a prime ")

def dem_uoc(num): # hàm đếm ước
    so_uoc=0
    for ước in range (1,num+1):
        if num%ước==0:
            so_uoc+=1
    return so_uoc

def in_ra_n_snt_dau(num): # hàm in ra n snt đầu
    snt=2
    count=0
    while count!=num:
        if dem_uoc(snt)==2:
            print(snt, end =" ")
            count+=1
        snt+=1
def tonggiaithua(n): #hàm tính tổng giai thừa
    sum=0
    def giaithua(n): #hàm tính giai thừa
        giai_thua = 1;
        if n==0 or n == 1:
            return giai_thua;
        else:
            for i in range(2, n + 1):
                giai_thua = giai_thua * i;
            return giai_thua;
    for i in range(0,int(n)):
        sum+=giaithua(i)
    return sum
from datetime import datetime
def time_now():
    now = datetime.now()
    return print(f"Today is", now.strftime("%21/%07/%2021") + "\n" + "Time right now:", now.strftime("%13:%36:%10"), "\n")

def main():
    #câu 1:
    user_input = input("Input a number: ")
    checknumber(user_input) # kiểm tra số

    while(checknumber(user_input) != 0):
        print("Invalid input. Please input again ")
        user_input=input("Input: ")

    is_int(user_input) # kiểm tra số nguyên
    #  câu 2:
    print("\n")
    a = input("Input a number: ")
    while(checknumber(a) != 0): #kiểm tra số 
        print("Invalid input. Please input again ")
        a=input("Input: ")

    is_prime(int(a)) # kiểm tra số nguyên tố
    
    # câu 3:
    print("\n")
    n=input("Input a number: ")
    while(checknumber(n) != 0): #kiểm tra số 
        print("Invalid input. Please input again ")
        n=input("Input: ")
    while int(n)<=0: 
        n=int(input("Input number: "))
    print("First",n,"prime(s): ", end ="")
    in_ra_n_snt_dau(int(n))
    # câu 4:
    print("\n")
    n=input("Input a number: ")
    while(checknumber(n) != 0): #kiểm tra số 
        print("Invalid input. Please input again ")
        n=input("Input: ")
    while int(n)<=0: 
        n=int(input("Input number: "))
    print("Result", tonggiaithua(n))
    
    # câu 5
    print("\n")
    time_now()
if __name__=="__main__":
    main()