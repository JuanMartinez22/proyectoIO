from django.shortcuts import render
from scipy.optimize import linprog, milp, Bounds, LinearConstraint

def Programacion(request):
    r1=''
    r2=''
    r3=''
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

    except:
        r1="Ha ocurrido un error..."
        r2="Ha ocurrido un error..."
        r3="Ha ocurrido un error..."

    return render(request,'programacion_lineal/programacionlineal.html',{'r1':r1,'r2':r2,'r3':r3})

def Costo(request):
    print('hola')