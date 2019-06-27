class CustomError(Exception):
    pass

# raise CustomError("dd")


try:
    print(x)
except(NameError):
    print('Name Error')