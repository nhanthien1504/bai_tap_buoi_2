# a = int(input('nhập số a: '))
# b = int(input('nhập số b: '))
# if a > 0 and b > 0:
#   print ( a+b)
# elif a < 0 and b < 0:
#   print (a*b)
# else:
#   print (min(a,b))
'''
in các số chẵn trong chuỗi
'''
# for i in range(0, 10, 2):
#     print(i, end=' ') # end= để kết quả không xuống dòng
#
# a = int(input('mời nhập a: '))
# b= int(input('mời nhập b: '))
# for i in range(a+1, b):
#     print(i, end=' ')
# a = int(input('mời nhập a: '))
# giai_thua = 1
# for i in range (1, a+1):
#     giai_thua *= i
# print(giai_thua)
'''
Lập chương trình thực hiện các công việc sau:
    1. Nhập số epsilon < 1  từ bàn phím
    2. Tính e = 1 + 1/1! + 1/2! + ... + 1/n! quá trình dừng khi 1/n! <  epsilon.
    3. Đưa kết quả ra màn hình
'''
# while True:
#     print('nhap so nguyen ', end=' ')
#     n = int(input())
#     if n > 0:
#         fac = 1
#         eps = 0
#         for i in range(1, n + 1):
#             fac *= i
#             eps += 1 / fac
#         print(eps)
#         break
#     print('đã nhập sai')
'''
Lập trình thực hiện các công việc sau:
    1. Nhập 3 số a, b, c bất kì
    2. Hãy kiểm tra xem ba số đó có phải là độ dài của các cạnh của một tam giác hay không? 
    3. Nếu đúng là tam giác thì xác định là tam giác vuông hay không?

'''
# a=float(input("Nhap vao canh a: "))
# b=float(input("Nhap vao canh b: "))
# c=float(input("Nhap vao canh c: "))
#
# if (a+b>c) & (b+c>a) & (a+c>b) & (a>0) & (b>0) & (c>0):
#     if (a==b)&(b==c):
#         print ("Day la tam giac deu")
#     elif (a==b)& (a!=c) | (a==c)&(a!=b) | (b==c) & (b!=a):
#         print ("Day la tam giac can")
#     elif (a*a==b*b+c*c)|(b*b==a*a+c*c)|(c*c==a*a+b*b):
#         print("Day la tam giac vuong")
#     else:
#         print("Day la tam giac thuong")
# else:
#     print('đây không phải là độ dài các cạnh của tam giác')

'''
Lập chương trình thực hiện các công việc sau:
    1. Nhập 1 số nguyên dương n bất kì (n<1000). Yêu cầu kiểm tra dữ liệu đầu vào, nếu sai yêu cầu nhập lại.
    2. Tính tổng các chữ số của số đó.
    3. Hiển thị kết qủa ra màn hình
'''
# while True:
#     print('mời nhập vào một số nguyên dương')
#     n = int(input())
#     if n > 0:
#         tong = 0
#         for i in range(1, n+1):
#             tong += i
#         print(tong)
#     else:
#         print('nhập sai')
'''
Lập chương trình tính các tổng sau:
    1. S_1 = 1 + x + x^2 + x^3 + ... + x^n
    2. S_2 = 1 - x + x^2 - x^3 + ... + (-1)^n.x^n
    3. S_3 = 1 + x/1! + x/2! + ... + x^n/n!
Trong đó, n là số nguyên dương và x là một số thực bất kì (Cả 2 đều được nhập từ bàn phím).
'''
# cau 1 S_1 = 1 + x + x^2 + x^3 + ... + x^n
# while True:
#     print('mời nhập x, n là các số nguyên dương')
#     x = int(input('x: '))
#     n = int(input('n: '))
#     if x > 0 and n > 0:
#         s = 0
#         for i in range (1, n+1):
#             s += pow(x, i)
#         print('S = 1 - x + x^2 - x^3 + ... + (-1)^n.x^n = ',s)
#     else:
#         print('nhập sai!')
#

# '''Câu 2:  S_2 = 1 - x + x^2 - x^3 + ... + (-1)^n.x^n '''
import math
# x = int(input('mời nhập số x: '))
# n = int(input('mời nhập số n: '))
# s = 0
# for i in range (1, n+1):
#     s += pow(x,i)*pow(-1,i)
# print(s)
#

'''
Lập chương trình thực hiện công việc sau:
    1. Nhập ba số a, b, c bất kì từ bàn phím
    2. Giải nghiệm phương trình bậc 2: ax^2 + bx + c = 0  (Kể cả trường hợp a=0)
'''
# a = float(input('nhập a = '))
# b = float(input('nhập b = '))
# c = float(input('nhập c = '))
# if a ==0:
#     if (b==0):
#         print('phương trình vô nghiệm!')
#     else:
#         print('phương trình có một nghiêm x = ',(-c/b))
# elif a != 0:
#     delta = b * b - 4 * a * c
#     if delta > 0:
#         x1 = (float)((-b + math.sqrt(delta)) / (2 * a))
#         x2 = (float)((-b - math.sqrt(delta)) / (2 * a))
#         print("Phương trình có 2 nghiệm là: x1 = ", x1, " và x2 = ", x2)
#     elif delta == 0:
#         x = (-b / (2 * a))
#         print("Phương trình có nghiệm kép: x1 = x2 = ", x)
#     else:
#         print('phương trình vô nghiêm! ')
