from django.shortcuts import render
from scipy.optimize import linprog, milp, Bounds, LinearConstraint
import math

def Programacion(request):
    r1=''
    r2=''
    r3=''

    tipo='esto se muestra'
    preciotot='esto se muesta'

    try:
        if request.method == "POST":
            CantidadKm = request.POST.get('cantkm')
            tramosRectos = request.POST.get('kmTR')
            curvasSuaves = request.POST.get('kmCS')
            curvasPronunciadas = request.POST.get('kmCP')
            
            #x0 = Cantidad de km
            #x1 = Cantidad de km de curvas suaves
            #x2 = Cantidad de km de curvas pronunciadas
            #x3 = Cantidad de km de tramos rectos
            #Curva suaves = 0.5km, Curvas pronunciadas = 1.5km, Rectas = 1km

            curvasPronunciadas=float(curvasPronunciadas)
            curvasSuaves=float(curvasSuaves)
            tramosRectos=float(tramosRectos)
            CantidadKm=float(CantidadKm)

            # 1.5x1 + 0.5x2 + 1x3 = 50
            # x1 <= d1
            # x2 <= d2
            # x3 >= d3

            obj = [0.5,1.5,1]

            A = [[1,0,0],[0,1,0],[0,0,-1]]
            b = [curvasSuaves,curvasPronunciadas,-tramosRectos]
            x0_Bounds =(0, None)
            x1_Bounds =(0, None)

            lhs_eq = [[1.5,0.5,1]]
            rhs_eq = [CantidadKm] 

            opt = linprog(obj, A_ub=A, b_ub=b, A_eq=lhs_eq, b_eq=rhs_eq,method="revised simplex")
            r1=(opt.x[0])*1.5
            r2=(opt.x[1])*0.5
            r3=(opt.x[2])*1  

            distpiedra = request.POST.get('piedra')
            distarena = request.POST.get('arena')
            distcemento = request.POST.get('cememto')
            distconcreto = request.POST.get('concreto')
            distbitumen = request.POST.get('bituminoso')
            
            totalpiedra = request.POST.get('cantpiedra')
            totalarena = request.POST.get('cantarena')
            totalcemento = request.POST.get('cantcemento')
            totalconcreto = request.POST.get('cantconcreto')
            totalbitumen = request.POST.get('cantbitumen')
            
            if totalpiedra.isdigit():
                respuesta1=CostoA(distpiedra,int(totalpiedra))
                respuesta2=CostoB(distarena,int(totalarena))
                respuesta3=CostoC(distcemento,int(totalcemento))
                respuesta4=CostoD(distconcreto,int(totalconcreto))
                respuesta5=CostoE(distbitumen,int(totalbitumen))
            else:
                respuesta1=CostoA(distpiedra,0)
            
            tipo=respuesta1[0]
            preciotot=round(respuesta1[1],2)

    except:
        r1="Ha ocurrido un error..."
        r2="Ha ocurrido un error..."
        r3="Ha ocurrido un error..."
        tipo="Ha ocurrido un error..."
        preciotot="Ha ocurrido un error..."

    return render(request,'programacion_lineal/programacionlineal.html',{'r1':r1,'r2':r2,'r3':r3,'tipo':tipo,'preciotot':preciotot})

def CostoA(distpiedra,cantpiedra):
    respuesta1 =''
    respuesta2 =''
    try:
        if distpiedra=='a1':
            pass
        elif distpiedra=='a2':
            respuesta1='Piedrin 1/2 comercial Guadalupe (Antigua)'
            respuesta2=cantpiedra*160.75
        elif distpiedra=='a3':
            respuesta1='Piedrin 1/2 comercial Guadalupe (Chimaltenango)'
            respuesta2=cantpiedra*192.73
        elif distpiedra=='a4':
            respuesta1='Piedrin 1/2 comercial Guadalupe (Escuintla)'
            respuesta2=cantpiedra*133.80
        elif distpiedra=='a5':
            respuesta1='Piedrin negro'
            respuesta2=cantpiedra*173.00
        elif distpiedra=='a6':
            respuesta1='Piedrin negro (Huehetenango)'
            respuesta2=cantpiedra*230.00
        elif distpiedra=='a7':
            respuesta1='Piedrin negro 3/4 (Retalhuleu)'
            respuesta2=cantpiedra*178.00
        elif distpiedra=='a8':
            respuesta1='Piedrin 1/2 comercio Sol'
            respuesta2=cantpiedra*177.00
    
    except:
        respuesta1='no se ha ingresado ningun material'
        respuesta2='no se ha ingresado ningun material'

    return respuesta1,respuesta2

def CostoB(distarena):
    respuesta1=''
    try:
        if distarena=='b1':
            pass
        elif distarena=='b2':
            respuesta1='Arena Rio corriente'
        elif distarena=='b3':
            respuesta1='Arena Rio Guadalupe(Antigua)'
        elif distarena=='b4':
            respuesta1='Arena Rio Guadalupe(Chimaltenago)'
        elif distarena=='b5':
            respuesta1='Arena Rio Guadalupe(Santa Lucia)'
        elif distarena=='b6':
            respuesta1='Arena Rio Guadalupe(San Lucas)'
        elif distarena=='b7':
            respuesta1='Arena Rio triturada'
    
    except:
        respuesta1='no se ha ingresado ningun material'

    return respuesta1

def CostoC(distcemento):
    respuesta1=''
    try:
        if distcemento=='c1':
            pass
        elif distcemento=='c2':
            respuesta1='Cemento Cantera progreso 42.5KG'
        elif distcemento=='c3':
            respuesta1='Cemento UGC 42.5KG'
        elif distcemento=='c4':
            respuesta1='Cemento Monocapa Blanco 40KG'
        elif distcemento=='c5':
            respuesta1='Cemento Monocapa Gris 40KG'
        elif distcemento=='c6':
            respuesta1='Cemento asfaltico chova'
        elif distcemento=='c7':
            respuesta1='Cemento asfáltico Black Jack'
    
    except:
        respuesta1='no se ha ingresado ningun material'

    return respuesta1

def CostoD(distconcreto):
    respuesta1=''
    try:
        if distconcreto=='d1':
            pass
        elif distconcreto=='d2':
            respuesta1='Concreto 3001 PSI 3/8 50KG'
        elif distconcreto=='d3':
            respuesta1='Cemento UGC 42.5KG'
    
    except:
        respuesta1='no se ha ingresado ningun material'

    return respuesta1

def CostoE(distbitumen):
    respuesta1=''
    try:
        if distbitumen=='e1':
            pass
        elif distbitumen=='e2':
            respuesta1='AC-2.5'
        elif distbitumen=='e3':
            respuesta1='AC-5'
    
    except:
        respuesta1='no se ha ingresado ningun material'

    return respuesta1