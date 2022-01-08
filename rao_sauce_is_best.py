param = ['ID', 'Title', 'Company', 'Link', 'Documents', 'Source', 'Date', 'DatePosted', 'Description']
# ID param should be automatically determined

# Accepts input from user
def accept_input():
    param_values = {}
    for item in param:
        if item == 'ID':
            param_values[item] = 1
            continue
        param_values[item] = input("Input value for " + item + ": ")
    return param_values

print(accept_input())

