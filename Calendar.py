def program(year):
    jan = 31
    march = 31
    apr = 30
    may = 31
    june = 30
    july = 31
    august = 31
    sept = 30 
    oct = 31
    november = 30
    dec = 31
    if (year % 4 == 0):
        febru = 29
    else: febru = 28
    mesac = [jan, febru, march, apr, may, june, july, august, sept, oct, november, dec]
    i = 0
    result = 0
    for i in range(len(mesac)):
        result += sumMonth(mesac[i])
    return result

def sumMonth(mesac):
    i = 1
    mesac += 1
    result = 0
    for i in range(mesac):
        if (mesac < 10):
            result += i
        else: result += (i // 10) + (i % 10)
    return result

x = int(input("Введите год: "))
print(program(x))