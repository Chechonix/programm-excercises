keys_to_remove = ['access_level', 'age']

employee = {
    'name': 'John',
    'email': 'john@ecorp.com',
    'access_level': 5,
    'age': 28
}

for key in keys_to_remove:
    if key in employee:
        del employee[key]

print(employee)
