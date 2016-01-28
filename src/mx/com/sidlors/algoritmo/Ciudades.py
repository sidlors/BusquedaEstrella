'''
Created on 27/01/2016

@author: jhernandezn
'''

#Implementacion del Algoritmo A* para las ciudades de Francia
#hernandez Navarro Salud Juan Manuel
#Inteligencia Artificial

def k(m):
    return K[m]

def h(n,m):
    return 10*abs(K[n]-K[m])

def f(n,m):
    return g(n,m)+h(n,m)

def g(origen,m):
    r=[y for (x,y) in Relaciones[origen] if x==m]
    if r!=[]:
        return  r[0]
    return 0

Ciudades={1:'Avignon', 2:'Bordeaux', 3:'Brest', 4:'Caen', 5:'Calais', 6:'Dijon',
          7:'Grenoble',8:'Limoges', 9:'Lyon', 10:'Marsella', 11:'Montpellier',
          12:'Nancy', 13:'Nantes', 14:'Nice',15:'Paris',  16:'Rennes',
          17:'Strasbourg', 18:'Toulouse'}
cerrada=[]
K={1:48,2:-6,3:-45,4:-4,5:18,6:51,7:57,8:12,9:48,10:53,11:36,12:62,13:-16,14:73,
   15:23,16:-17,17:77,18:14}

Relaciones={1:[(7,227),(9,216),(10,99),(11,121)],
            2:[(8,220),(13,329),(18,253)],
            3:[(16,244)],
            4:[(5,120),(15,241),(16,176)],
            5:[(4,120),(12,534),(15,297)],
            6:[(9,192),(12,201),(15,313),(17,335)],
            7:[(1,227),(9,104)],
            8:[(2,220),(9,389),(13,329),(15,396),(17,313)],
            9:[(1,216),(6,192),(7,104),(8,389)],
            10:[(1,99),(14,188)],
            11:[(1,21),(18,240)],
            12:[(5,534),(6,201),(15,372),(17,145)],
            13:[(2,329),(8,329),(16,107)],
            14:[(10,188)],
            15:[(4,241),(5,297),(6,313),(8,396),(12,372),(16,348)],
            16:[(3,244),(4,176),(13,107),(15,348)],
            17:[(6,335),(12,145)],
            18:[(2,253),(8,313),(11,240)]
           }

def presentacion():

        print('*'*70) 
        print "Hola Bienvenido"
        print "Elija una ciudad de partida y una de destino\n\n"

        print("1. Avignon, 2. Bordeaux, 3. Brest, 4.Caen, 5. Calais, 6. Dijon, 7. Grenoble, 8. Limoges, 9. Lyon,")
        print("10. Marsella, 11. Montpellier, 12. Nancy, 13. Nantes, 14. Nice, 15. Paris, 16. Rennes,")
        print("17. Strasbourg, 18. Toulouse")
        print('*'*70+"\n")

        origen=input("Elige la Opcion del Origen \n")
        
        destino=input("Dame la Opcion del Destino\n")
        if(destino>18 or origen >18 or destino<1 or origen < 1):
            print "Esas ciudades no estas como opcion (1-18)"
        else:
            print Ciudades[origen],15*'-',Ciudades[destino]
            destinos(origen,destino)
        
def destinos(origen,destino):
    
    F=f(origen,destino)
    agenda=[[origen,F]]
    solucion=aEstrella(agenda,origen,destino)
    ruta=[x for [x,y]in solucion]
    if ruta!=[]:
     costo=[y for [x,y] in solucion if x==destino]
     print "\n\nLa ruta es:",Ciudades[origen],"->".join([Ciudades[c] for c in ruta ]), "Con un Costo Total de: ",costo[0]
    else:
     print "Lo Siento no hay Ruta"
     
def aEstrella(agenda,origen,destino):
    
   while(agenda!=[]):
       minimo=min([y for [x,y]in agenda])
       w=[x for x in agenda if x[1]<=minimo]
       nuevo=w[0] #Por si hubiera empates tome solo uno#
       agenda.remove(nuevo)
       cerrada.append(nuevo)
       n=nuevo[0]
      
       if (Ciudades[n]==Ciudades[destino]):
           return cerrada
       indicesDeVecinos=[w for w in [x for (x,y) in Relaciones[n] ] ]
       
       for i in range(len(indicesDeVecinos)):
           ghijos=g(origen,n)+g(n,indicesDeVecinos[i])
           nuevoNodo=[indicesDeVecinos[i],ghijos+h(indicesDeVecinos[i],destino)]
           
           anterior= [x for x in agenda if  nuevoNodo[0]==x[0]]
           enCerrada=[e for e in cerrada if nuevoNodo[0]==e[0]]

           if anterior!=[]:
             ant=anterior[0]
             if (ant[1]>=nuevoNodo[1]):
               
               agenda.remove(ant)
               continue
             

           if enCerrada!=[]:
             b=enCerrada[0]
             if (b[1]>=nuevoNodo[1]):
               
               cerrada.remove(b)
               cerrada.append(nuevoNodo)
               continue

           [cerrada.remove(x) for x in cerrada if x[0]==nuevoNodo[0]] 
           [agenda.remove(c) for c in  agenda if c[0]==nuevoNodo[0]] 
           
           agenda.append(nuevoNodo)
          
   return []

def main():
   presentacion()

main()


