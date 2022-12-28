"""-----------------------------     Conditionals and Loops      -----------------------------"""
""""Task #1"""


def rectangle(n):
    for k in range(n, 0, -1):
        print(("* " * k).center(n * 2))


rectangle(6)
# -----------------------------------------------------------------------
"""Task #2"""
print("-" * 15)


def rectangle(n):
    for k in range(0, 1):  # does not make anything only nested
        for i in range(1, n + 1):
            print(("* " * i))
        for j in range(n - 1, 0, -1):
            print("* " * j)


rectangle(6)
# -----------------------------------------------------------------------
"""Task #3"""
print("-" * 15)


def reverse(word):
    for i in range(len(word) - 1, -1, -1):
        print(word[i], end="")


reverse('hallo world')
# -----------------------------------------------------------------------
"""Task #4"""
print("-" * 15)


def schedule(m, n):
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            print(i * j, end=" ")
        print()


schedule(6, 3)
# -----------------------------------------------------------------------
"""Task #5"""
print("-" * 15)


def calculate(word):
    x = 0
    y = 0
    for i in word:
        if i.isalpha():
            x += 1
        elif i.isdigit():
            y += 1
        else:
            pass
    return print("and number of letters is", x, "number of digits is", y)


calculate('sadfsadf@gffa21')
# -----------------------------------------------------------------------
"""Task #6"""
print("-" * 15)


def pas(wo):
    u = 0
    l = 0
    d = 0
    s = 0
    for i in wo:
        if i.isupper():
            u += 1
        elif i.islower():
            l += 1
        elif i.isdigit():
            d += 1
        elif i in "$#@":
            s += 1
        else:
            pass
    if u >= 1 and l >= 1 and d >= 1 and s >= 1 and len(wo) >= 6 and len(wo) <= 16:
        print("your password is correct")
    else:
        print("your password is not correct")


pas("Hi man1@")
# -----------------------------------------------------------------------
"""Task #7"""
print("-" * 15)


def even(s, e):
    for i in range(s, e + 1):
        t = str(i)
        if int(t[0]) % 2 == 0 and int(t[1]) % 2 == 0 and int(t[2]) % 2 == 0:
            print(t, end=", ")
        else:
            pass


even(100, 400)
# -----------------------------------------------------------------------
"""Task #8"""
print("-" * 15)

for i in range(100, 401):
    k = str(i)
    if int(k[0]) % 2 == 0 and int(k[1]) % 2 == 0 and int(k[2]) % 2 == 0:
        item.append(k)
    else:
        pass
print(",".join(item))
# -----------------------------------------------------------------------
"""Task #8"""
print("-" * 15)
x = input("Enter your born year")


def Chinese(x):
    x = str(x)
    if x in "1924, 1936, 1948, 1960, 1972, 1984, 1996, 2008, 2020, 2032":
        return "Rat	鼠 (shǔ)"
    elif x in "1925, 1937, 1949, 1961, 1973, 1985, 1997, 2009, 2021, 2033":
        return "Ox	牛 (niú)"
    elif x in "1926, 1938, 1950, 1962, 1974, 1986, 1998, 2010, 2022, 2034":
        return "Tiger	虎 (hǔ)"
    elif x in "1927, 1939, 1951, 1963, 1975, 1987, 1999, 2011, 2023, 2035":
        return "Rabbit	兔 (tù)"
    elif x in "1928, 1940, 1952, 1964, 1976, 1988, 2000, 2012, 2024, 2036":
        return "Dragon	龙 (lóng)"
    elif x in "1929, 1941, 1953, 1965, 1977, 1989, 2001, 2013, 2025, 2037":
        return "Snake	蛇 (shé)"
    elif x in "1930, 1942, 1954, 1966, 1978, 1990, 2002, 2014, 2026, 2038":
        return "Horse	马 (mǎ) "
    elif x in "1931, 1943, 1955, 1967, 1979, 1991, 2003, 2015, 2027, 2039":
        return "Sheep	羊 (yáng)"
    elif x in "1932, 1944, 1956, 1968, 1980, 1992, 2004, 2016, 2028, 2040":
        return "Monkey	猴 (hóu)"
    elif x in "1933, 1945, 1957, 1969, 1981, 1993, 2005, 2017, 2029, 2041":
        return "Rooster	鸡 (jī)"
    elif x in "1934, 1946, 1958, 1970, 1982, 1994, 2006, 2018, 2030, 2042":
        return "Dog	狗 (gǒu)"
    elif x in "1935, 1947, 1959, 1971, 1983, 1995, 2007, 2019, 2031, 2043":
        return "Pig	猪 (zhū)"
    else:
        print("out of the range")


print(Chinese(1950))
# -----------------------------------------------------------------------
"""Task #9"""
print("-" * 15)


def findTraingleKind(a, b, c):
    if a == b and a == c:
        return "This is an equilateral triangle."
    elif a != b and a != c and b != c:
        return "This is a scalene triangle."
    elif a == b or c == b or c == a:
        return "This is an isosceles triangle."
    else:
        pass


a = int(input("Enter the side:"))
b = int(input("Enter the side:"))
c = int(input("Enter the side:"))

findTraingleKind(a, b, c)
# -----------------------------------------------------------------------
"""Task #10"""
print("-" * 15)

# paper

# -----------------------------------------------------------------------
"""Task #11"""
print("-" * 15)


def out(a, b, c):
    for a in range(10):
        for b in range(10):
            for c in range(10):
                print(a, b, c, sep="", end=",")


out(0, 0, 0)
# -----------------------------------------------------------------------
"""Task #12"""
print("-" * 15)


def multiplication(X, no_numbers):
    for i in range(1, no_numbers + 1):
        print(X, "X", i, "=", X * i)


e = int(input("Enter the number"))
c = int(input("Enter the number"))
multiplication(e, c)
# -----------------------------------------------------------------------
"""Task #13"""
print("-" * 15)


def sum(x):
    p = 0
    while x.lower() not in "done":
        x = input("Enter the number: ")
        if x.lower() in "done":
            return p
        else:
            p = int(x) + int(p)


sum("start")
# -----------------------------------------------------------------------
"""Task #14"""
print("-" * 15)


def factorial(n):
    t = 1
    f = 1
    for i in range(1, n + 1):
        f = i
        t *= f
    return t


factorial(7)
# # -----------------------------------------------------------------------
"""Task #15"""
print("-" * 15)

# Recursion
# -----------------------------------------------------------------------
"""Task #16"""
print("-" * 15)


def sum(n):
    y = 0
    for i in range(n):
        x = int(input("Enter the number here: "))
        y += x
    return "sum of numbers is", y, "average of numbers is", y / 10


sum(10)
# -----------------------------------------------------------------------
"""Task #17"""
print("-" * 15)


def evenodd(n):
    odd = 0
    even = 0
    for i in range(n + 1):
        if i % 2 == 0:
            even += i
        elif i % 2 == 1:
            odd += i
        else:
            pass
    return even / odd


evenodd(10)
# -----------------------------------------------------------------------
"""Task #18"""
print("-" * 15)


def Number_of_rows(n):
    for i in range(1, n + 1):
        for g in range(0, i):
            print((g + i) % 2, end="")
        print()


Number_of_rows(5)
# -----------------------------------------------------------------------
"""Task #19"""
print("-" * 15)


def perfect(n):
    k = []
    l = 0
    for i in range(1, n):
        if n % i == 0:
            x = i
            k.append(x)
    for j in range(len(k)):
        l += k[j]
    if l == n:
        return "This is perfect number"
    else:
        return "This is not perfect number"


perfect(27)
# -----------------------------------------------------------------------
"""Task #20"""
print("-" * 15)


def perfect(x, y, z):
    a = 0
    k = 0
    for i in range(x, y + 1):
        if i % z == 0:
            a += i
            k += 1
        else:
            continue
    return "The sum of numbers is", a, "and the number of numbers is ", k


perfect(10, 100, 5)
# -----------------------------------------------------------------------
"""Task #21"""
print("-" * 15)

def prime(n):
    x = 1000
    list1 = [2,]
    for i in range(3, x):
        for g in range(2, i):
            if (i % g) == 0:
                break
        else:
            list1.append(i)
    for j in range(len(list1)):
        if j == len(list1)-1:
            return False
        else:
            list2 = list1[j+1] + list1[j]
            if list2 == n:
                return True
    return False
print(prime(7))
# -----------------------------------------------------------------------
"""Task #22"""
print("-" * 15)


def triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "This is not a triangle"
    elif (a ** 2 + b ** 2) ** 0.5 == c:
        return "This is a right angled triangle"

    else:
        return "This is not a right angled triangle"


triangle(4, 3, 5)
# -----------------------------------------------------------------------
"""Task #23"""
print("-" * 15)


def lill(n):
    e = 0
    o = 0
    t = 0
    for i in range(1, n + 1):
        if (i % 2) == 0:
            e += 1
        elif (i % 2) == 1:
            o += 1
    for j in range(1, e + 1):
        if (j % 2) == 0:
            t += (10 * j)
    return str(t) + "+" + str(o) + "p"


lill(10)
# -----------------------------------------------------------------------
"""Task #24"""
print("-" * 15)

# on paper
# -----------------------------------------------------------------------
"""Task #25"""
print("-" * 15)


def sumproduct(m):
    odd = 0
    even = 1
    while m != 0:
        if m % 2 == 0:
            even *= m
        elif m % 2 == 1:
            odd += m
        else:
            pass
        m = int(input("Enter any number: "))
    return "The product of all even numbers is", even, "and the sum of all odd numbers is", odd


sumproduct(int(input("Enter the number:")))
# -----------------------------------------------------------------------
"""Task #26"""
print("-" * 15)
import random


def rand(s, e, g):
    x = random.randrange(s, e)
    if x == g:
        return "congratulations, your guess was right"
    elif g <= x + 3:
        return "Warm"
    else:
        return "Cold"


s = int(input("Enter the start range: "))
e = int(input("Enter the end range: "))
g = int(input("Enter your guess number: "))
rand(s, e, g)
"""-----------------------------     Logic and Functions      -----------------------------"""
"""Task #27"""
print("-" * 15)

v = 0
n = 0
x = 1
k = 0
while x != "":
    if k != 0:
        v += len(x)
        n += 1
    x = input("Enter the word: ")
    k += 1

if n == 0:
    n += 1
print("the average is", v // n)
# -----------------------------------------------------------------------
"""Task #28"""
print("-" * 15)

# paper

# -----------------------------------------------------------------------
"""Task #29"""
print("-" * 15)

# paper

# -----------------------------------------------------------------------
"""Task #30"""
print("-" * 15)


def cigar_party(m, n):
    if n == True:
        return True
    else:
        pass
    if m > 40 and m < 60:
        return True
    else:
        return False


print(cigar_party(30, False))
print(cigar_party(50, False))
print(cigar_party(70, True))
# -----------------------------------------------------------------------
"""Task #31"""
print("-" * 15)


def squirrel_play(m, n):
    if n == True:
        if m < 101 and m > 60:
            return True
        else:
            return False
    if n != True:
        if m < 91 and m > 60:
            return True
        else:
            return False


print(squirrel_play(70, False))
print(squirrel_play(95, False))
print(squirrel_play(95, True))
# -----------------------------------------------------------------------
"""Task #32"""
print("-" * 15)


def caught_speeding(m, n):
    if n == False:
        if m <= 60:
            return 0
        elif 61 <= m <= 80:
            return 1
        elif m >= 81:
            return 2
        else:
            pass
    else:
        if m <= 60 + 5:
            return 0
        elif 61 + 5 <= m <= 80 + 5:
            return 1
        elif m >= 81 + 5:
            return 2


print(caught_speeding(60, False))
print(caught_speeding(65, False))
print(caught_speeding(65, True))
# -----------------------------------------------------------------------
"""Task #33"""
print("-" * 15)


def sorta_sum(m, n):
    y = m + n
    if 10 <= y <= 19:
        return 20
    else:
        return y


print(sorta_sum(3, 4))
print(sorta_sum(9, 4))
print(sorta_sum(10, 11))
# -----------------------------------------------------------------------
"""Task #34"""
print("-" * 15)


def alarm_clock(day, vacation):
    #    Sun, Mon, Tue, Wed, Thr, Fri, sat = 0, 1, 2, 3, 4, 5, 6
    if vacation:
        return '10:00'
    elif day == 0 or day == 6:
        return '10:00'
    else:
        return '7:00'


print(alarm_clock(1, False))
print(alarm_clock(5, False))
print(alarm_clock(0, False))
# -----------------------------------------------------------------------
"""Task #35"""
print("-" * 15)


def love6(num1, num2):
    if num1 == 6 or num2 == 6:
        return True
    elif (num1 - num2) == 6:
        return True
    elif (num1 + num2) == 6:
        return True
    else:
        return False


print(love6(6, 4))
print(love6(4, 5))
print(love6(1, 5))
# -----------------------------------------------------------------------
"""Task #36"""
print("-" * 15)


def in1to10(n, outside_mode):
    if outside_mode:
        return True
    elif 1 <= n <= 10:
        return True
    else:
        return False


print(in1to10(5, False))
print(in1to10(11, False))
print(in1to10(11, True))
# -----------------------------------------------------------------------
"""Task #37"""
print("-" * 15)


def near_ten(n):
    if n > 7:
        x = n % 10
        if x > 7 or x < 3:
            return True
        else:
            return False
    else:
        return False


print(near_ten(12))
print(near_ten(17))
print(near_ten(19))
# -----------------------------------------------------------------------
"""Task #38"""
print("-" * 15)


def make_bricks(s, b, l):
    if type(l) == float:
        return False
    if l > 5 and b > 0:
        while b != 0 and l >= 5:
            l -= 5
            b -= 1
    l -= s
    if l > 0:
        return False
    else:
        return True


print(make_bricks(3, 1, 8))
print(make_bricks(3, 1, 9))
print(make_bricks(3, 2, 10))
# -----------------------------------------------------------------------
"""Task #39"""
print("-" * 15)


def lucky_sum(a, b, c):
    if a == 13:
        return 0
    elif b == 13:
        return a
    elif c == 13:
        return a + b
    else:
        return a + b + c


print(lucky_sum(1, 2, 3))
print(lucky_sum(1, 2, 13))
print(lucky_sum(1, 13, 3))
# -----------------------------------------------------------------------
"""Task #40"""
print("-" * 15)


def lucky_sum(a, b, c):
    if a < 13 and b < 13 and c < 13:
        return a + b + c
    elif b == 13:
        return a
    elif c == 13:
        return a + b


print(lucky_sum(1, 2, 3))
print(lucky_sum(1, 2, 13))
print(lucky_sum(1, 13, 3))
# -----------------------------------------------------------------------
"""Task #41"""
print("-" * 15)


def round_sum(a, b, c):
    a1 = a % 10
    b1 = b % 10
    c1 = c % 10
    if 10 > a1 > 4:
        a = ((a // 10)+1)*10
    else:
        a = (a // 10)*10
    if 10 > b1 > 4:
        b = ((b // 10)+1)*10
    else:
        b = (b // 10)*10
    if 10 > c1 > 4:
        c = ((c // 10)+1)*10
    else:
        c = (c // 10)*10
    return a + b + c


print(round_sum(16, 17, 18))
print(round_sum(12, 13, 14))
print(round_sum(6, 4, 4))
# -----------------------------------------------------------------------
"""Task #42"""
print("-" * 15)


def even(n):
    x = 0
    n = str(n)
    z = "246"
    for i in range(len(n)):
        if n[i] in z:
            x += 1
    return x


even(69982)
# -----------------------------------------------------------------------
"""Task #43"""
print("-" * 15)


def blackjack(a, b):
    if a > 0 and b > 0:
        if a == 21:
            return a
        elif b == 21:
            return b
        if a > 21 and b > 21:
            return 0
        elif a > 21 > b:
            return b
        elif b > 21 > a:
            return a
        elif b < 21 and a < 21:
            b2, a2 = b, a
            while a2 < 21 and b2 < 21:
                a2 += 1
                b2 += 1
            if a2 > b2:
                return b
            else:
                return a
    else:
        return "Out of range"


print(blackjack(19, 21))
print(blackjack(21, 19))
print(blackjack(19, 22))
print(blackjack(19, 17))
# -----------------------------------------------------------------------
"""Task #44"""
print("-" * 15)


def loneSum(a, b, c):
    if a == b != c:
        return c
    elif a == b == c:
        return 0
    elif a == c != b:
        return b
    elif b == c != a:
        return a
    elif a != b != c:
        return a + b + c


print(loneSum(1, 2, 3))
print(loneSum(3, 2, 3))
print(loneSum(3, 3, 3))
# -----------------------------------------------------------------------
"""Task #45"""
print("-" * 15)


def twoAsOne(a, b, c):
    if (a + b) == c:
        return True
    elif (b + c) == a:
        return True
    elif (a + c) == b:
        return True
    else:
        return False


print(twoAsOne(1, 2, 3))
print(twoAsOne(3, 1, 2))
print(twoAsOne(3, 2, 2))
# -----------------------------------------------------------------------
"""Task #46"""
print("-" * 15)


def leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


print(leap_year(2020))
print(leap_year(2024))
print(leap_year(2000))
print(leap_year(2400))
print(leap_year(1800))
print(leap_year(1900))
print(leap_year(2100))
print(leap_year(2200))
print(leap_year(2300))
print(leap_year(2500))
# -----------------------------------------------------------------------
"""Task #47"""
print("-" * 15)


def make_chocolate(s, b, t):
    x = 0
    if b > 0:
        while b != 0 and t != 0:
            t -= 5
            b -= 1
    if t == 0:
        return 0
    else:
        while t != 0:
            x += 1
            t -= 1
            s -= 1
    if s < 0:
        return -1
    elif s >= 0:
        return x


print(make_chocolate(4, 1, 9))
print(make_chocolate(4, 1, 10))
print(make_chocolate(4, 1, 7))
# -----------------------------------------------------------------------
"""Task #48"""
print("-" * 15)


def function(a, b):
    x = []
    for i in range(a, b+1):
        if i % 7 == 0:
            if i % 5 != 0:
                x.append(i)
    return x


function(1, 36)
# -----------------------------------------------------------------------
"""Task #49"""
print("-" * 15)


def sum(n):
    b = [2,]
    z = 0
    i = 3
    flag = True
    while flag:
        for j in range(2, i):
            if i % j == 0:
                i += 1
                break
        else:
            b.append(i)
            i += 1
        if len(b) == n:
            flag = False
    for l in range(len(b)):
        z += b[l]
    return "Sum of first", n, "prime numbers:", z


a = int(input("Enter the number: "))
sum(a)
# -----------------------------------------------------------------------
"""Task #50"""
print("-" * 15)


def is_happy2(n):
    n = str(n)
    l = 0
    if len(n) == 1:
        if int(n) == 1:
            return True
        else:
            return False
    else:
        for i in range(len(n)):
            l += int(n[i]) ** 2
    return is_happy2(l)


def is_happy(n):
    n = str(n)
    z = 0
    for i in range(len(n)):
        z += int(n[i]) ** 2
    return is_happy2(z)


print(is_happy(7))
print(is_happy(932))
print(is_happy(6))
# -----------------------------------------------------------------------
"""Task #51"""
print("-" * 15)


def number_of_primes(n):
    if n > -1:
        b = []
        for i in range(2, n + 1):
            for k in range(2, i):
                if i % k == 0:
                    break
            else:
                b.append(i)
        return len(b)
    else:
        return "Out of range"


print(number_of_primes(10))
print(number_of_primes(100))
# -----------------------------------------------------------------------
"""Task #52"""
print("-" * 15)


def is_palindrome(n):
    z = ""
    if n < 0:
        return False
    else:
        n = str(n)
        for i in range(len(n)-1, -1, -1):
            z += n[i]
        if z == n:
            return True
        else:
            return False


print(is_palindrome(100))
print(is_palindrome(252))
print(is_palindrome(-838))
# -----------------------------------------------------------------------
"""Task #53"""
print("-" * 15)


def largest_smallest_digit(n):
    n = str(n)
    z = []
    for i in range(len(n)):
        z.append(int(n[i]))
    s = z[0]
    for s1 in z:
        if s1 < s:
            s = s1
    l = z[0]
    for l1 in z:
        if l1 > l:
            l = l1
    print("Largest: ", l, ",", " Smallest: ", s, sep="")
largest_smallest_digit(9387422)
# -----------------------------------------------------------------------
"""Task #54"""
print("-" * 15)


def is_abundant(n):
    z = 0
    for i in range(1, n):
        if n % i == 0:
            z += i
    if z > n:
        return True
    else:
        return False


print(is_abundant(12))
print(is_abundant(13))
# -----------------------------------------------------------------------
"""Task #55"""
print("-" * 15)

def amicable_numbers_sum(n):
    list1 = 0
    sum1 = 0
    for i in range(1, n+1):
        divisori = 0
        divisori1 = 0
        for j in range(1, i):
            if i % j == 0:
                divisori += j
        if divisori != i:
            for i1 in range(1, divisori):
                if divisori % i1 == 0:
                    divisori1 += i1
            if divisori1 == i:
                sum1 += i
    return sum1


amicable_numbers_sum(9999) 
# -----------------------------------------------------------------------
"""Task #56"""
print("-" * 15)


def next_smallest_palindrome(n):
    flag = True
    while flag:
        n = str(n+1)
        h = ""
        for i in range(len(n)-1, -1, -1):
            h += n[i]
        h = int(h)
        n = int(n)
        if n == h:
            flag = False
    return h
print(next_smallest_palindrome(99))
print(next_smallest_palindrome(1221))
# -----------------------------------------------------------------------
"""Task #57"""
print("-" * 15)


def disarium(n):
    l = 1
    s = 0
    n = str(n)
    for i in range(len(n)):
        s += int(n[i]) ** l
        l += 1
    if s == int(n):
        return "True this is a disarium number "
    else:
        return "False this is a disarium number "


disarium(135)
# -----------------------------------------------------------------------
"""Task #58"""
print("-" * 15)


def is_harsad(n):
    n = str(n)
    l = 0
    for i in range(len(n)):
        l += int(n[i])
    if int(n) % l == 0:
        return True
    else:
        return False


print(is_harsad(666))
print(is_harsad(11))
"""---------------------------------      strings       --------------------------------------"""
"""Task #1"""
print("-" * 15)


def check(str1, str2):
    x = ""
    z = ""
    f = ""
    for i in str1:
        if i.isalpha and i not in x:
            x += i
    for j in str2:
        c = 0
        for k in x:
            if k == j:
                z += k
    for _ in z:
        if _ not in f:
            c = list(z).count(_)
            if c > 1:
                f += _
    return f


word1 = "aaddffgghhjjkkl"
word2 = "asdfghjklz"
check(word2, word1)
# -----------------------------------------------------------------------
"""Task #2"""
print("-" * 15)

def Pig_Latin(n):
    z = n.split(" ")
    z1 = ""
    for i in z:
        z1 += i[1:] + i[0] + "AY" + " "
    return z1
    
    
print(Pig_Latin("I SLEPT MOST OF THE NIGHT")) #"IAY LEPTSAY OSTMAY FOAY HETAY IGHTNAY"
# -----------------------------------------------------------------------
"""Task #3"""
print("-" * 15)


def countYZ(m):
    s = 0
    for i in range(len(m)):
        if m[i] == " ":
            if m[i - 1] in "zy":
                s += 1
            else:
                pass
        else:
            pass
    if m[len(m) - 1] in "zy":
        s += 1
    return s


print(countYZ("gray day thiz Monday"))
print(countYZ("gray day this Tuesday"))
print(countYZ("day fyyyz"))
# -----------------------------------------------------------------------
"""Task #4"""
print("-" * 15)


def countTriple(n):
    m = 0
    for i in n:
        count = 0
        k = ""
        k += i
        for i in n:
            if i == k:
                count += 1
                if count >= 3:
                    m += 1
    return m // 3


print(countTriple("abcXXXabc"))
print(countTriple("xxxabyyyycd"))
print(countTriple("a"))
# -----------------------------------------------------------------------
"""Task #5"""
print("-" * 15)

#paper
# -----------------------------------------------------------------------
"""Task #6"""
print("-" * 15)


def removedup(n):
    s = ""
    for i in n:
        if i not in s:
            s += i
    return s


removedup("aabbbbbbbbbbbyyyyyyyyyyyyyrr")
# -----------------------------------------------------------------------
"""Task #7"""
print("-" * 15)


def remove(s, p):
    z = ""
    n = 0
    for i in s:
        if p != i:
            z += i
        else:
            n += 1
    if n == 0:
        return z[1:]
    else:
        return z


remove("aabaabaabaabaa", "z")
# -----------------------------------------------------------------------
"""Task #8"""
print("-" * 15)


#paper
# -----------------------------------------------------------------------
"""Task #9"""
print("-" * 15)


#paper
# -----------------------------------------------------------------------
"""Task #10"""
print("-" * 15)


def removes2(n, g):
    a = ""
    z = 0
    for i in n:
        if i != g:
            a += i
        else:
            z += 1
    if z == 0:
        return n[1: -1]
    else:
        return a


removes2("aavbcaa", "a")
# -----------------------------------------------------------------------
"""Task #11"""
print("-" * 15)


def make_abba(a, b):
    z = ""
    n = 1
    while n < 5:
        if n == 1:
            z += a
            n += 1
        elif n == 2:
            z += b
            n += 1
        elif n == 3:
            z += b
            n += 1
        else:
            z += a
            n += 1
    return z


print(make_abba('Hi', 'Bye'))
print(make_abba('Yo', 'Alice'))
print(make_abba('What', 'Up'))
# -----------------------------------------------------------------------
"""Task #12"""
print("-" * 15)


def make_out_word(a, b):
    a1 = a[:2]
    a2 = a[2:]
    n = 1
    z = ""
    if len(a) == 4:
        while n <= 3:
            if n == 1:
                z += a1
                n += 1
            elif n == 2:
                n += 1
                z += b
            else:
                n += 1
                z += a2
        return z
    else:
        return "The first string should be 4 length"


print(make_out_word('<<>>', 'Yay'))
print(make_out_word('<<>>', 'WooHoo'))
print(make_out_word('[[]]', 'word'))
# -----------------------------------------------------------------------
"""Task #13"""
print("-" * 15)


def extra_end(n):
    if len(n) >= 2:
        n1 = n[-2:]
        return n1 * 3
    else:
        return "The length of the string less than 2"


print(extra_end('Hello'))
print(extra_end('ab'))
print(extra_end('Hi'))
# -----------------------------------------------------------------------
"""Task #14"""
print("-" * 15)


def first_two(n):
    l = len(n)
    if l == 0:
        return " yields the empty string "
    elif l == 1:
        return n
    elif l > 1 :
        return n[:2]


print(first_two('Hello'))
print(first_two('abcdefg'))
print(first_two('ab'))
# -----------------------------------------------------------------------
"""Task #15"""
print("-" * 15)


def first_half(n):
    l = len(n) // 2
    return n[:l]


print(first_half('WooHoo'))
print(first_half('HelloThere'))
print(first_half('abcdef'))
# -----------------------------------------------------------------------
"""Task #16"""
print("-" * 15)


def without_end(n):
    if len(n) < 2:
        return False
    else:
        return n[1:-1]

print(without_end('Hello'))
print(without_end('java'))
print(without_end('coding'))
# -----------------------------------------------------------------------
"""Task #17"""
print("-" * 15)


def combo_string(n, n1):
    if len(n) > len(n1):
        return n1 + n + n1
    elif len(n1) > len(n):
        return n + n1 + n
    else:
        return "Those have same length"


print(combo_string('Hello', 'hi'))
print(combo_string('hi', 'Hello'))
print(combo_string('aaa', 'b'))
# -----------------------------------------------------------------------
"""Task #18"""
print("-" * 15)


def non_start(n, n1):
    if len(n) >= 1 and len(n1) >= 1:
        return n[1:] + n1[1:]
    else:
        return "One from the strings is empty"

print(non_start('Hello', 'There'))
print(non_start('java', 'code'))
print(non_start('shotl', 'java'))
# -----------------------------------------------------------------------
"""Task #19"""
print("-" * 15)


def left2(n):
    if len(n) >= 2:
        n = n[2:] + n[:2]
        return n
    else:
        return "The length of the code is less than 2"

print(left2('Hello'))
print(left2('java'))
print(left2('Hi'))
# -----------------------------------------------------------------------
"""Task #20"""
print("-" * 15)


def double_char(n):
    z = ""
    for i in range(len(n)):
        z += (n[i] * 2)
    return z


print(double_char('The'))
print(double_char('AAbb'))
print(double_char('Hi-There'))
# -----------------------------------------------------------------------
"""Task #21"""
print("-" * 15)


def count_hi(n):
    count = 0
    for i in range(2, len(n) + 1):
        z = n[(i - 2):i]
        if z == "hi":
            count += 1
    return count


print(count_hi('abc hi ho'))
print(count_hi('ABChi hi'))
print(count_hi('hihi'))
# -----------------------------------------------------------------------
"""Task #22"""
print("-" * 15)


def cat_dog(n):
    c = "cat"
    d = "dog"
    countd, countc = 0, 0
    for i in range(len(c), len(n) + 1):
        z = n[(i - len(c)):i]
        if z == c:
            countc += 1
    for i in range(len(d), len(n) + 1):
        a = n[(i - len(d)):i]
        if a == d:
            countd += 1
    if countd == countc:
        return True
    else:
        return False


print(cat_dog('catdog'))
print(cat_dog('catcat'))
print(cat_dog('1cat1cadodog'))
# -----------------------------------------------------------------------
"""Task #"23"""
print("-" * 15)


def count_code(n):
    z = 0
    a = "qwertyuiopasdfghjklzxcvbnm"
    c = "code"
    for i in range(len(c), len(n)+1):
        v = n[i-len(c):i]
        for j in range(len(a)):
            c1 = c[0:2] + a[j] +c[3]
            if c1 == v:
                z += 1
    return z


print(count_code('aaacodebbb'))
print(count_code('codexxcode'))
print(count_code('cozexxcope'))
# -----------------------------------------------------------------------
"""Task #24"""
print("-" * 15)


def end_other(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    if len(str1) > len(str2):
        if str1[-len(str2):] == str2:
            return True
    elif len(str2) > len(str1):
        if str2[-len(str1):] == str1:
            return True
    elif str2 == str1:
        return True
    else:
        return False
    

print(end_other('Hiabc', 'abc'))
print(end_other('AbC', 'HiaBc'))
print(end_other('abc', 'abXabc'))
# -----------------------------------------------------------------------
"""Task #"25"""
print("-" * 15)

def xyz_there(str1):
    if "xyz" in str1:
        if ".xyz" in str1:
            return False
        else:
            return True
    else:
        return False
    

print(xyz_there('abcxyz'))
print(xyz_there('abc.xyz'))
print(xyz_there('xyz.abc'))
# -----------------------------------------------------------------------
"""Task #26"""
print("-" * 15)

def change(str1):
    n = str1[0]
    n1 = str1[1:]
    z = "" + n
    for i in range(len(n1)):
        if n == n1[i]:
            z += "$"
        else:
            z += n1[i]
    return z

    
change('restart')
# -----------------------------------------------------------------------
"""Task #27"""
print("-" * 15)

def swap(str1, str2):
    x1 = str2[:2] + str1[2:]
    x2 = str1[:2] + str2[2:]
    x3 = x1 + " " +x2
    return x3
    
    
swap('abc', 'xyz')
# -----------------------------------------------------------------------
"""Task #28"""
print("-" * 15)

def add(str1):
    if len(str1) > 2:
        if str1[-3:] == "ing":
            return str1 + 'ly'
        else:
            return str1 + 'ing'
    else:
        return str1
    
print(add('string'))
print(add('abc'))
# -----------------------------------------------------------------------
"""Task #29"""
print("-" * 15)

def replace(str1):
    x1 = "not"
    x2 = "poor"
    if x1 in str1 and x2 in str1:#I want make sure those are in the string
        for i in range(3, len(str1)+1):#because the last one does not include in range and index[:]
            if str1[i-3:i] == x1:#now i make shore this is the position of not
                i1 = i#because the i will change after it and i want memorize it
        for j in range(4, len(str1)+1):#same the last
            if str1[j-4:j] == x2:#same step
                j1 = j#same step
        return str1[:i1-3] + "good" + str1[j1:]
        """
        Same calculus 
        I now the position of n's not has position (i1-3) and t has (i1-1)
        the last one does not include if i put position's (n), n will not include
        same thing in poor
        """
    else:#those are not in the string because of that i return the string without any change
        return str1


print(replace("The lyrics is not that poor!")) #'The lyrics is good!'
print(replace('The lyrics is poor!')) #'The lyrics is poor!'
# -----------------------------------------------------------------------
"""Task #30"""
print("-" * 15)

def non_repeating(n):
    for i in n:
        x = ""
        for j in n:
            if i != j:
                x += j
            x1 = len(x)
            n1 = len(n) - 1
            if x1 == n1:
                return i
# -----------------------------------------------------------------------
"""Task #30, other simple solve"""
print("-" * 15)

def non_repeating(n):
    j = list(n)
    for i in n:
        if j.count(i) == 1:
            return i
        
            
print(non_repeating("hhhaaaaalloooowwwwwzbb"))
# -----------------------------------------------------------------------
"""Task #31"""
print("-" * 15)

def repeating(n):
    j = list(n)
    for i in n:
        if j.count(i) > 1:
            return i
        
            
print(non_repeating("zhhhaaaaalloooowwwwwbb"))
# -----------------------------------------------------------------------
"""Task #32"""
print("-" * 15)

def remove_spaces(n):
    s = " "
    n2 = ''
    for i in n:
        if s != i:
            n2 += i
    return n2

print(remove_spaces("fjasdfs      kalsjdfkl f af "))
# -----------------------------------------------------------------------
"""Task #33"""
print("-" * 15)

def max_consecutive_0(n):
    x = 0
    z = n.split("1")
    for i in z:
        if len(i) > x:
            x = len(i)
    return x
    

print(max_consecutive_0('111000010000110')) # 4
print(max_consecutive_0('111000111')) # 3
# -----------------------------------------------------------------------
"""Task #34"""
print("-" * 15)

def replace_words(n):
    z = n.split(" ")
    q = z[-1]
    p = ""
    for i in z:
        if len(i) >= 5 and i != q:
            p += (("#" * len(i))+" ")
        elif q == i:
            if len(i) >= 5:
                p += ("#" * len(i))
            else:
                p += i
        else:
            p += (i + " ")  
    return p

replace_words('Count the lowercase letters in the said list of words')
# """
# ##### the ######### ####### in the said list of ######
# """
# -----------------------------------------------------------------------
"""Task #35"""
print("-" * 15)

def digit_sum(n):
    s = 0
    for i in n:
        s += int(i) 
    return s
    
digit_sum("123") # 6
# -----------------------------------------------------------------------
"""Task #36"""
print("-" * 15)

def lower_n_letters(s,n):
    s1 = s[:n]
    s2 = s[n:]
    s3 = s1.lower() + s2
    return s3
    
    
lower_n_letters('W3RESOURCE.COM', 4) # w3reSOURCE.COM 