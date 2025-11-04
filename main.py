# Viết chương trình (có thể viết dưới dạng hàm nếu muốn) thực hiện thao tác sau:
# 	Yêu cầu người dùng nhập vào một số nguyên n > 0. Nếu số nhập vào không thỏa mãn điều kiện > 0, yêu cầu người dùng nhập lại.
# 	Sau khi người dùng nhập n > 0, tính giá trị biểu thức sau:
# S= {(1×3×…×n          "nếu n là số lẻ" @2×4×…×n     "nếu n là số chẵn" )


n = int(input("Nhập số N: "))
def checkN(n):
    if n > 0:
        s, arr = 1,[]
        if n%2 == 0:
            i = 2
            for i in range(i , n+1):
                if i%2 == 0:
                    arr.append(i)
                    s *= i
            print("Tich cac so chan",arr,"la",s)
        else:
            i = 0
            for i in range(i , n+1):
                if i%2 != 0:
                    arr.append(i)
                    s *= i
            print("Tich cac so le",arr,"la",s)
    else:
        n = int(input("N phải > 0: "))
        checkN(n)
checkN(n)

# 	Viết chương trình (có thể viết dưới dạng hàm nếu muốn) thực hiện các thao tác sau: 
# 	Yêu cầu người dùng nhập vào một số nguyên n > 0. Nếu số nhập vào không thỏa mãn điều kiện > 0, yêu cầu người dùng nhập lại.
# 	Sau khi người dùng nhập n > 0, yêu cầu nhập vào n số nguyên. Tính trung bình cộng của các số chẵn trong n số vừa nhập.

n = int(input("Nhập số N: "))
def checkN(n):
    if n > 0:
        s, arr = 0,[]
        if n%2 == 0:
            i = 2
            for i in range(i , n+1):
                if i%2 == 0:
                    arr.append(i)
                    s += i
            print("Trung binh cong của",arr,"la",(s/len(arr)))
        else:
            i = 0
            for i in range(i , n+1):
                if i%2 != 0:
                    arr.append(i)
                    s += i
            print("Trung binh cong của",arr,"la",(s/len(arr)))
    else:
        n = int(input("N phải > 0: "))
        checkN(n)
checkN(n)


# Phần 2. Viết hàm thực hiện các thao tác trong đề bài bên dưới. Yêu cầu: Bài sau sử dụng lại hàm của bài trước nếu có thể.
# Kiểm tra 3 số có phải là độ dài ba cạnh của tam giác.
# Tên hàm: is_triangle
# Tham số: 3 số thực
# Output: True nếu là ba cạnh của tam giác, False nếu ngược lại.
def is_triangle(a, b,c):
    if a>0 and b>0 and c>0:
        if a+b>c and a+c>b and b+c>a:
            print(True)
        else: print(False)
    else: print(False)

is_triangle(5,6,7)

# 	Tính diện tích của tam giác biết độ dài ba cạnh.
# Tên hàm: triangle_area
# Tham số: 3 số thực
# Output: Diện tích tính được. Hàm trả về -1 nếu không tính được.

def triangle_area(a, b,c):
    if a>0 and b>0 and c>0:
        p = (a+b+c)/2
        s = (p*(p-a)*(p-b)*(p-c))**(1/2)
        print(round(s))
    else: print(-1)

triangle_area(5,6,7)

# 	Nhập số nguyên dương n. Nếu người dùng nhập sai (n ≤ 0) thì yêu cầu nhập lại.
# Tên hàm: INPUT
# Tham số: Không có tham số
# Output: số nguyên dương thỏa mãn yêu cầu đề bài.

n = int(input("Nhập số N: "))
def checkN(n):
    if n > 0:
        print(n,"la so nguyen duong")
    else:
        n = int(input("N phải > 0: "))
        checkN(n)
checkN(n)

# 	Kiểm tra một số có phải là số nguyên tố hay không.
# Tên hàm: is_prime
# Tham số: số nguyên n
# Output: True nếu n là số nguyên tố, False nếu n không là số nguyên tố.

n = int(input("Nhập số N: "))
def is_prime(n):
    if n < 2:
        return print(False)
    arr = []
    for i in range(1, n + 1):
        if n % i == 0:
            arr.append(i)
    if len(arr) == 2:
        return print(True)
    else:
        return print(False)
is_prime(n)


# 	Tính tổng các số nguyên tố từ 1 đến n. 
# Tên hàm: sum_prime_numbers
# Tham số: số nguyên n
# Output: Tổng tính được. Hàm trả về -1 nếu không tính được.

n = int(input("Nhập số N: "))
def sum_prime_numbers(n):
    a = []
    def is_prime(n):
        if n < 2:
            return 0
        arr = []
        for i in range(1, n + 1):
            if n % i == 0:
                arr.append(i)
        if len(arr) == 2:
            a.append(n)
        else:
            return 0
    for i in range(1, n + 1):
        is_prime(i)
    S = 0
    for num in a:
        S += num
    if S == 0:
        return print(-1)
    else:
        return print(S)
sum_prime_numbers(n)

# Hướng dẫn: Cần xác định trường hợp khi nào không tính được tổng.
# 	Tính trung bình cộng các số nguyên tố từ 1 đến n. 
# Tên hàm: average_prime_numbers
# Tham số: số nguyên n
# Output: Trung bình cộng tính được. Hàm trả về -1 nếu không tính được.

n = int(input("Nhập số N: "))
def average_prime_numbers(n):
    a = []
    def is_prime(n):
        if n < 2:
            return 0
        arr = []
        for i in range(1, n + 1):
            if n % i == 0:
                arr.append(i)
        if len(arr) == 2:
            a.append(n)
        else:
            return 0
    for i in range(1, n + 1):
        is_prime(i)
    S = 0
    for num in a:
        S += num
    if S == 0:
        return print(-1)
    else:
        return print(S/len(a))
average_prime_numbers(n)

# Hướng dẫn: Cần xác định trường hợp khi nào không tính được trung bình cộng.


# 	Kiểm tra một số nguyên là số hoàn thiện hay không? (Số hoàn thiện là số có tổng các ước bằng chính nó).
# Tên hàm: is_perfect
# Tham số: số nguyên n
# Output: True nếu n là số hoàn hảo, False nếu n không là số hoàn hảo.

n = int(input("Nhập số N: "))
def is_perfect(n):
    a = []
    for i in range(1,n+1):
        if n%i == 0:
            a.append(i)
        else: return -1
    if len(a) == n:
        return True
    else: return False
print(is_perfect(n))

# 	Tính tổng các số hoàn hảo từ 1 đến n. 
# Tên hàm: sum_perfect_numbers
# Tham số: số nguyên n
# Output: Tổng tính được. Hàm trả về -1 nếu không tính được.

n = int(input("Nhập số N: "))

def is_perfect(n):
    a = []
    for i in range(1,n):
        if n%i == 0:
            a.append(i)
        else: return -1
    return a

def sum_perfect_numbers(nums):
    S = 0
    for num in nums:
        S += num
    return S

print(sum_perfect_numbers(is_perfect(n)))

# Hướng dẫn: Cần xác định trường hợp khi nào không tính được tổng.

# Tính trung bình cộng các số hoàn hảo từ 1 đến n. 
# Tên hàm: average_perfect_numbers
# Tham số: số nguyên n
# Output: Trung bình cộng tính được. Hàm trả về -1 nếu không tính được.

n = int(input("Nhập số N: "))

def is_perfect(n):
    a = []
    for i in range(1,n):
        if n%i == 0:
            a.append(i)
    return a

def average_perfect_numbers(nums):
    S = 0
    for num in nums:
        S += num
    return S/len(nums)

print(average_perfect_numbers(is_perfect(n)))

# Hướng dẫn: Cần xác định trường hợp khi nào không tính được trung bình cộng.
# 	Tính giá trị của biểu thức: 1^3+2^3+⋯+n^3
# Tên hàm: sum1
# Tham số: số nguyên n.
# Output: Tổng tính được. Trả về -1 trong trường hợp n <= 0.

n = int(input("Nhập số N: "))
def sum1(n):
    S = 0
    if n <= 0:
        return -1
    else:
        for i in range(1, n+1):
            S += i**3
    return S