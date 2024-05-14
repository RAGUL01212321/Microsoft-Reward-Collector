import webbrowser
num=str(input("enter the number of times you want to search: " ))
print('''
note :
for each search 2 edge coins will be awarded 
''')
for i in range(int(num)):
    webbrowser.open('https://www.bing.com/search?q='+str(i))
print('total number of coins got=',num*3)

