'''try:
    result = 14 / 0
    result + "100"
except (ZeroDivisionError, TypeError):
    print(f"process exception")
finally:
    print("process finished")
'''
    
try:
    result = 14 / 2
    result + "100"
except Exception as error:
    print(f"got an error => {error}")
finally:
    print("process finished")
