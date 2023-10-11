from django.shortcuts import render
from scipy.optimize import linprog, milp, Bounds, LinearConstraint
import math
import datetime

def Programacion(request):
    r1=''
    r2=''
    r3=''

    tipopied=''
    punitpiedra=''
    cantipiedra=''
    totalprecpiedra=''

    tipoare=''
    punitare=''
    cantiare=''
    totalprecare=''

    tipoceme=''
    punitceme=''
    canticeme=''
    totalprecceme=''

    tipoconc=''
    punitconc=''
    canticonc=''
    totalprecconc=''

    tipobitu=''
    punitbitu=''
    cantibitu=''
    totalprecbitu=''

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
            distcemento = request.POST.get('cemento')
            distconcreto = request.POST.get('concreto')
            distbitumen = request.POST.get('bituminoso')
            
            totalpiedra = request.POST.get('cantpiedra')
            totalarena = request.POST.get('cantarena')
            totalcemento = request.POST.get('cantcemento')
            totalconcreto = request.POST.get('cantconcreto')
            totalbitumen = request.POST.get('cantbitumen')
            
            if totalpiedra.isdigit() and distpiedra!='a1':
                respuesta1=CostoA(distpiedra,int(totalpiedra))
            else:
                respuesta1=CostoA(distpiedra,0)

            if totalarena.isdigit() and distarena!='b1':
                respuesta2=CostoB(distarena,int(totalarena))
            else:
                respuesta2=CostoB(distarena,0)

            if totalcemento.isdigit() and distcemento!='c1':
                respuesta3=CostoC(distcemento,int(totalcemento))
            else:
                respuesta3=CostoC(distcemento,0)

            if totalconcreto.isdigit() and distconcreto!='d1':
                respuesta4=CostoD(distconcreto,int(totalconcreto))
            else:
                respuesta4=CostoD(distconcreto,0)

            if totalbitumen.isdigit() and distbitumen!='e1':
                respuesta5=CostoE(distbitumen,int(totalbitumen))
            else:
                respuesta5=CostoE(distbitumen,0)

            
            tipopied=respuesta1[0]
            punitpiedra=respuesta1[1]
            cantipiedra=respuesta1[2]
            totalprecpiedra=respuesta1[3]

            tipoare=respuesta2[0]
            punitare=respuesta2[1]
            cantiare=respuesta2[2]
            totalprecare=respuesta2[3]

            tipoceme=respuesta3[0]
            punitceme=respuesta3[1]
            canticeme=respuesta3[2]
            totalprecceme=respuesta3[3]

            tipoconc=respuesta4[0]
            punitconc=respuesta4[1]
            canticonc=respuesta4[2]
            totalprecconc=respuesta4[3]

            tipobitu=respuesta5[0]
            punitbitu=respuesta5[1]
            cantibitu=respuesta5[2]
            totalprecbitu=respuesta5[3]

    except:
        r1="Ha ocurrido un error..."
        r2="Ha ocurrido un error..."
        r3="Ha ocurrido un error..."

        tipopied=''
        punitpiedra='0'
        cantipiedra='0'
        totalprecpiedra='0'

        tipoare=''
        punitare='0'
        cantiare='0'
        totalprecare='0'

        tipoceme=''
        punitceme='0'
        canticeme='0'
        totalprecceme='0'

        tipoconc=''
        punitconc='0'
        canticonc='0'
        totalprecconc='0'

        tipobitu=''
        punitbitu='0'
        cantibitu='0'
        totalprecbitu='0'

    # imprimirReporte(tipopied,punitpiedra,cantipiedra,totalprecpiedra,tipoare,punitare,cantiare,totalprecare,tipoceme,punitceme,canticeme,totalprecceme,tipoconc,punitconc,canticonc,totalprecconc,tipobitu,punitbitu,cantibitu,totalprecbitu)

    return render(request,'programacion_lineal/programacionlineal.html',{'r1':r1,'r2':r2,'r3':r3})

def CostoA(distpiedra,cantpiedra):
    respuesta1=''
    respuesta2=''
    respuesta3=''
    respuesta4=''

    try:
        if distpiedra=='a1':
            respuesta1='piedra'
            respuesta2=0
            respuesta3=0
            respuesta4=0

        elif distpiedra=='a2':
            respuesta1='Piedrin 1/2 comercial Guadalupe (Antigua)'
            respuesta2='160.75'
            respuesta3=cantpiedra
            respuesta4=cantpiedra*160.75

        elif distpiedra=='a3':
            respuesta1='Piedrin 1/2 comercial Guadalupe (Chimaltenango)'
            respuesta2='192.73'
            respuesta3=cantpiedra
            respuesta4=cantpiedra*192.73

        elif distpiedra=='a4':
            respuesta1='Piedrin 1/2 comercial Guadalupe (Escuintla)'
            respuesta2='133.80'
            respuesta3=cantpiedra
            respuesta4=cantpiedra*133.80

        elif distpiedra=='a5':
            respuesta1='Piedrin negro'
            respuesta2='173.00'
            respuesta3=cantpiedra
            respuesta4=cantpiedra*173.00

        elif distpiedra=='a6':
            respuesta1='Piedrin negro (Huehetenango)'
            respuesta2='230.00'
            respuesta3=cantpiedra
            respuesta4=cantpiedra*230.00

        elif distpiedra=='a7':
            respuesta1='Piedrin negro 3/4 (Retalhuleu)'
            respuesta2='178.00'
            respuesta3=cantpiedra
            respuesta4=cantpiedra*178.00

        elif distpiedra=='a8':
            respuesta1='Piedrin 1/2 comercio Sol'
            respuesta2='177.00'
            respuesta3=cantpiedra
            respuesta4=cantpiedra*177.00
    
    except:
        respuesta1=''
        respuesta2=''
        respuesta3=''
        respuesta4=''

    return respuesta1,respuesta2,respuesta3,respuesta4

def CostoB(distarena,cantarena):
    respuesta1=''
    respuesta2=''
    respuesta3=''
    respuesta4=''

    try:
        if distarena=='b1':
            respuesta1='arena'
            respuesta2=0
            respuesta3=0
            respuesta4=0

        elif distarena=='b2':
            respuesta1='Arena Rio corriente'
            respuesta2='100.00'
            respuesta3=cantarena
            respuesta4=cantarena*100.00

        elif distarena=='b3':
            respuesta1='Arena Rio Guadalupe(Antigua)'
            respuesta2='127.54'
            respuesta3=cantarena
            respuesta4=cantarena*127.54

        elif distarena=='b4':
            respuesta1='Arena Rio Guadalupe(Chimaltenago)'
            respuesta2='159.82'
            respuesta3=cantarena
            respuesta4=cantarena*159.82

        elif distarena=='b5':
            respuesta1='Arena Rio Guadalupe(Santa Lucia)'
            respuesta2='147.39'
            respuesta3=cantarena
            respuesta4=cantarena*147.39

        elif distarena=='b6':
            respuesta1='Arena Rio Guadalupe(San Lucas)'
            respuesta2='168.49'
            respuesta3=cantarena
            respuesta4=cantarena*168.49

        elif distarena=='b7':
            respuesta1='Arena Rio triturada'
            respuesta2='176.75'
            respuesta3=cantarena
            respuesta4=cantarena*176.75
    
    except:
        respuesta1=''
        respuesta2=''
        respuesta3=''
        respuesta4=''

    return respuesta1,respuesta2,respuesta3,respuesta4

def CostoC(distcemento,cantcemento):
    respuesta1=''
    respuesta2=''
    respuesta3=''
    respuesta4=''

    try:
        if distcemento=='c1':
            respuesta1='cemento'
            respuesta2=0
            respuesta3=0
            respuesta4=0

        elif distcemento=='c2':
            respuesta1='Cemento Cantera progreso 42.5KG'
            respuesta2='72.00'
            respuesta3=cantcemento
            respuesta4=cantcemento*72.00

        elif distcemento=='c3':
            respuesta1='Cemento UGC 42.5KG'
            respuesta2='82.48'
            respuesta3=cantcemento
            respuesta4=cantcemento*82.48

        elif distcemento=='c4':
            respuesta1='Cemento Monocapa Blanco 40KG'
            respuesta2='63.13'
            respuesta3=cantcemento
            respuesta4=cantcemento*68.13

        elif distcemento=='c5':
            respuesta1='Cemento Monocapa Gris 40KG'
            respuesta2='43.24'
            respuesta3=cantcemento
            respuesta4=cantcemento*43.24

        elif distcemento=='c6':
            respuesta1='Cemento asfaltico chova'
            respuesta2='790.00'
            respuesta3=cantcemento
            respuesta4=cantcemento*790.00

        elif distcemento=='c7':
            respuesta1='Cemento asfáltico Black Jack'
            respuesta2='455.00'
            respuesta3=cantcemento
            respuesta4=cantcemento*445.00
    
    except:
        respuesta1=''
        respuesta2=''
        respuesta3=''
        respuesta4=''

    return respuesta1,respuesta2,respuesta3,respuesta4

def CostoD(distconcreto,cantconcreto):
    respuesta1=''
    respuesta2=''
    respuesta3=''
    respuesta4=''
    try:
        if distconcreto=='d1':
            respuesta1='conocreto'
            respuesta2=0
            respuesta3=0
            respuesta4=0

        elif distconcreto=='d2':
            respuesta1='Concreto 3001 PSI 3/8 50KG'
            respuesta2='35.68'
            respuesta3=cantconcreto
            respuesta4=cantconcreto*35.68
            
        elif distconcreto=='d3':
            respuesta1='Cemento UGC 42.5KG'
            respuesta2='35.64'
            respuesta3=cantconcreto
            respuesta4=cantconcreto*35.64
    
    except:
        respuesta1=''
        respuesta2=''
        respuesta3=''
        respuesta4=''

    return respuesta1,respuesta2,respuesta3,respuesta4

def CostoE(distbitumen,cantbitumen):
    respuesta1=''
    respuesta2=''
    respuesta3=''
    respuesta4=''
    try:
        if distbitumen=='e1':
            respuesta1='Material bituminoso'
            respuesta2=0
            respuesta3=0
            respuesta4=0

        elif distbitumen=='e2':
            respuesta1='AC-2.5'
            respuesta2='pendiente'
            respuesta3=cantbitumen
            respuesta4=cantbitumen*0

        elif distbitumen=='e3':
            respuesta1='AC-5'
            respuesta2='pendiente'
            respuesta3=cantbitumen
            respuesta4=cantbitumen*0
    
    except:
        respuesta1=''
        respuesta2=''
        respuesta3=''
        respuesta4=''

    return respuesta1,respuesta2,respuesta3,respuesta4

def imprimirReporte(mpiedra,pupiedra,cpiedra,ptotal,marena,puarena,carena,atotal,mcemento,pucemento,ccemento,cetotal,mconcreto,puconcreto,cconcreto,cototal,mbitumen,pubitumen,cbitumen,btotal):

    hora_actual = datetime.datetime.now()
    print("El archivo se genero el: "+str(hora_actual))
    dia=hora_actual.day
    mes=hora_actual.month
    year=hora_actual.year
    hora = hora_actual.hour
    segundo = hora_actual.second
    micro=hora_actual.microsecond

    ptotal=str(round(float(ptotal),2))
    atotal=str(round(float(atotal),2))
    cetotal=str(round(float(cetotal),2))
    cototal=str(round(float(cototal),2))
    btotal=str(round(float(btotal),2))

    file = open(f"infome_{str(dia)+'_'+str(mes)+'_'+str(year)+'_'+str(hora)+str(segundo)+str(micro)}.txt","x")
    file.write("\n")
    file.write("Informe del reporte: \n")
    file.write("\n")
    file.write("+---------------------------------------------+---------------+---------------+----------------+\n")
    file.write("|Material y Distruibidor                      |Precio c/u (Q) |Cantidad       |Precio total (Q)|\n")
    file.write("+---------------------------------------------+---------------+---------------+----------------+\n")
    cadena = "|{:<45}|{:<15}|{:<15}|{:<16}|".format(mpiedra,pupiedra,cpiedra,ptotal)
    file.write(f"{cadena}\n")
    file.write("+---------------------------------------------+---------------+---------------+----------------+\n")
    cadena = "|{:<45}|{:<15}|{:<15}|{:<16}|".format(marena,puarena,carena,atotal)
    file.write(f"{cadena}\n")
    file.write("+---------------------------------------------+---------------+---------------+----------------+\n")
    cadena = "|{:<45}|{:<15}|{:<15}|{:<16}|".format(mcemento,pucemento,ccemento,cetotal)
    file.write(f"{cadena}\n")
    file.write("+---------------------------------------------+---------------+---------------+----------------+\n")
    cadena = "|{:<45}|{:<15}|{:<15}|{:<16}|".format(mconcreto,puconcreto,cconcreto,cototal)
    file.write(f"{cadena}\n")
    file.write("+---------------------------------------------+---------------+---------------+----------------+\n")
    cadena = "|{:<45}|{:<15}|{:<15}|{:<16}|".format(mbitumen,pubitumen,cbitumen,btotal)
    file.write(f"{cadena}\n")
    file.write("+---------------------------------------------+---------------+---------------+----------------+\n")