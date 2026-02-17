counter = 0  
def increase():
    global counter
    counter += 1
    print("Counter inside the function:", counter)

increase()
print("Counter outside the function:", counter)
