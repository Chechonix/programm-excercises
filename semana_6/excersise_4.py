def show_message():
    message = "Hello from inside the function"
    print(message)

show_message()

print(message)
counter = 0  
def increase():
    global counter
    counter += 1
    print("Counter inside the function:", counter)

increase()
print("Counter outside the function:", counter)