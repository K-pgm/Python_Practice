# 関数

# 華氏から摂氏に変換する

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


fahrenheit = 72
print(fahrenheit_to_celsius(fahrenheit))
