# try:
#     f = open('work.txt', 'r')
#     f.write('hello world')
# except IOError:
#     print('An error occured')
# else:
#     print('This was successful')

# try:
#     f = open('work.txt', 'r')
#     f.write('hello world')
# except:
#     print('An error occured')
# else:
#     print('This was successful')   

# try:
#     f = open('work.txt', 'r')
#     f.write('hello world')
# finally:
#     print('This was successful')    


# def getNumber(var):
#     try:
#         return int(var)
#     except ValueError as Argument:
#         print(f'the error occurred because of {Argument.args}')

# getNumber('THIS')        

# def getNumber(var):
#     try:
#         var < 1
#         raise IOError
#     except IOError:
#         print('Error')

# getNumber(0)        

class NumberlessthanError(ZeroDivisionError):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

try:
    raise NumberlessthanError(23,12,25)
except NumberlessthanError as e:
    print(e)