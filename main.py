import another

a_dict = {
    'another.greet': another.greet,
    'another.multiply': another.multiply,
    'another.subtract': another.subtract,
}

result = a_dict['another.greet']('bobby hadz')
print(result)  # 👉️ hello bobby hadz

result = a_dict['another.multiply'](5, 5)
print(result)  # 👉️ 25

result = a_dict['another.subtract'](100, 20)
print(result)  # 👉️ 80
