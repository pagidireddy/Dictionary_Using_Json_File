from src import utils

word = input("enter the Word: ")
output = utils.data(word)
if type(output) == list:
    for i in output:
        print(i)
else:
    print(output)
