from django.shortcuts import render
from django.http import  HttpResponse
from scipy.optimize import linprog, milp, Bounds, LinearConstraint
import math
import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def Programacion(request):
    kmtotales=''
    r1=''
    r2=''
    r3=''

    tipopied=''
    punitpiedra=''
    cantipiedra=''
    totalprecpiedra='0'

    tipoare=''
    punitare=''
    cantiare=''
    totalprecare='0'

    tipoceme=''
    punitceme=''
    canticeme=''
    totalprecceme='0'

    tipoconc=''
    punitconc=''
    canticonc=''
    totalprecconc='0'

    tipobitu=''
    punitbitu=''
    cantibitu=''
    totalprecbitu='0'

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
            kmtotales=CantidadKm
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
        kmtotales="Ha ocurrido un error..."
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

    imprimirReporte(kmtotales,r1,r2,r3,tipopied,punitpiedra,cantipiedra,totalprecpiedra,tipoare,punitare,cantiare,totalprecare,tipoceme,punitceme,canticeme,totalprecceme,tipoconc,punitconc,canticonc,totalprecconc,tipobitu,punitbitu,cantibitu,totalprecbitu)
    # imprimirReporte(kmtotales,r1,r2,r3)

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

def imprimirReporte(km,r1,r2,r3,mpiedra,pupiedra,cpiedra,ptotal,marena,puarena,carena,atotal,mcemento,pucemento,ccemento,cetotal,mconcreto,puconcreto,cconcreto,cototal,mbitumen,pubitumen,cbitumen,btotal):
# def imprimirReporte(km,r1,r2,r3):
    km=str(km)
    r1=str(r1)
    r2=str(r2)
    r3=str(r3)
    ptotal=(round(float(ptotal),2))
    atotal=(round(float(atotal),2))
    cetotal=(round(float(cetotal),2))
    cototal=(round(float(cototal),2))
    btotal=(round(float(btotal),2))

    totaldetotales=ptotal+atotal+cetotal+cototal+btotal
    totaldetotales=round(totaldetotales,2)
    totaldetotales=str(totaldetotales)

    c = canvas.Canvas('Optimizacion.pdf', pagesize=letter)
    ruta='C:\\Users\\Pablo\\Desktop\\ose\\Logo1.jpeg'
    c.drawImage(ruta, -20, 650, 200, 200)
    c.setFont('Helvetica', 25)
    c.drawString(150,720,"Reporte de optimizacion Optitech")

    c.line(20, 650, 600, 650)

    c.setFont('Helvetica', 13)
    c.drawString(20,600,f"Cantidad de km a abarcar: {km}km")
    c.drawString(20,570,f"Cantidad de tramos rectos: {r3}km")
    c.drawString(20,555,f"Cantidad de curvas pronunciadas: {r2}km")
    c.drawString(20,540,f"Cantidad de curvas suaves: {r1}km")

    c.drawString(20,510,f"Materiales a usar")
    c.drawString(20,495,f"{mpiedra}")
    c.drawString(20,480,f"{marena}")
    c.drawString(20,465,f"{mcemento}")
    c.drawString(20,450,f"{mconcreto}")
    c.drawString(20,435,f"{mbitumen}")

    c.drawString(350,510,f"Precio Unitario")
    c.drawString(350,495,f"Q.{pupiedra}")
    c.drawString(350,480,f"Q.{puarena}")
    c.drawString(350,465,f"Q.{pucemento}")
    c.drawString(350,450,f"Q.{puconcreto}")
    c.drawString(350,435,f"Q.{pubitumen}")
    
    c.drawString(475,510,f"Cantidad")
    c.drawString(475,495,f"{cpiedra} mt3")
    c.drawString(475,480,f"{carena} mt3")
    c.drawString(475,465,f"{ccemento} saco")
    c.drawString(475,450,f"{cconcreto} saco")
    c.drawString(475,435,f"{cbitumen} mt3")

    c.setFont('Helvetica', 15)
    c.drawString(400,405,f"Total: ")
    c.drawString(475,405,f"Q.{totaldetotales}")


    c.setFont('Helvetica', 10)
    c.drawString(250,70,"Contacto:")
    c.drawString(200,60,"Correo: optitech@solutions.gt")
    c.drawString(205,50,"Telefono: (+502) 5621-8345")
    c.save()

def MyV(request):
    return render(request, "programacion_lineal/misionvision.html")

def SN(request):
    return render(request, "programacion_lineal/Sobrenosotros.html")

def IN(request):
    return render(request, "programacion_lineal/Inicio.html")

def pdf_view(request):
    with open('C:\\Users\\Pablo\\Desktop\\ose\\ManualUsuario.pdf', 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=mypdf.pdf'
        return response
