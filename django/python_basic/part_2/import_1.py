def func():
    print('this is import_1 file')

print(__name__)
print('This is inside Import 1')
if __name__ == "__main__":
    print("This is not imported")
else:
    print("This is imported")