f = open ('coso.txt','r')
fx = open ('text.txt','w')
i=0
while i!=5:
    mensaje = f.readline()
    fx.readline
    vector =mensaje.split(" ")
    miniv= vector[2].split()
    if vector[1]=='+':
        print(vector[0],vector[1],miniv[0],"=",int(vector[0])+int(vector[2]))
        fx.write(vector[0])
        fx.write(vector[1])
        fx.write(miniv[0])
        fx.write("=")
        cositi=int(vector[0])+int(vector[2])
        fx.write(str(cositi))
        fx.write("\n")
        i=i+1
    if vector[1]=='-':
        print(vector[0],vector[1],miniv[0],"=",int(vector[0])-int(vector[2]))
        fx.write(vector[0])
        fx.write(vector[1])
        fx.write(miniv[0])
        fx.write("=")
        cositi=int(vector[0])-int(vector[2])
        fx.write(str(cositi))
        fx.write("\n")
        i=i+1
    if vector[1]=='X':
        print(vector[0],vector[1],miniv[0],"=",int(vector[0])*int(vector[2]))
        fx.write(vector[0])
        fx.write(vector[1])
        fx.write(miniv[0])
        fx.write("=")
        cositi=int(vector[0])*int(vector[2])
        fx.write(str(cositi))
        fx.write("\n")
        i=i+1    
f.close()
fx.close()