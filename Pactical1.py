fh = open('practical1.txt','w')
F=int(input("Enter the temperature in Fahrenheit: ")) 
b = ( F - 32 ) * 5/9 
fh.write("The temperature in Celsius is: "+ str(b)+'\n')
C=int(input("Enter the temperature in Celsius: ")) 
d = ( C * 9/5 ) + 32 
fh.write("The temperature in Fahrenheit is: " + str(d)) 
fh.close()