#for i in range(1,3):
 #if i%2==0:
  #print(i, "es par")
 #else:
  #print(i, "es impar")

def descompone(num):
 #self.num=num
  u=0 
  d=0 
  c=0 
  un=0

  while(num>=1000):
   un+=1
   num-=1000

  while(num>=100):
   c+=1
   num-=100

  while(num>=10):
   d+=1
   num-=10

  while(num>=1):
   u+=1
   num-=1

  print("El numero tiene ",u," unidades , ",d," decenas, ",c," centenas, ",un,"unidades de mil")

system("cls")
descompone(2234)
   



