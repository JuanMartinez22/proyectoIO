from django.shortcuts import render
import plotly.express as px
import pandas as pd
import datetime

def proceRedes(request):

    # fechaActual=''
    # fechaFinal=''
    # try:
        # if request.method == "POST":
    #         hora_actual = datetime.datetime.now()
    #         dia=hora_actual.day
    #         mes=hora_actual.month
    #         year=hora_actual.year
    #         fechaActual=(str(year)+'-'+str(mes)+'-'+str(dia))
    #         fechaFinal=(str(year+5)+'-'+str(mes)+'-'+str(dia))
    #         Start='2009-01-01'
    #         Finish='2009-02-28'

    # except:
    #     fechaActual='2009-01-01'
    #     fechaFinal='2009-02-28'
    if request.method == "POST":
        file = open("infome_23.txt","x")
        file.write("\n")
        file.write("Informe del reporte: \n")
        file.write("\n")

    return render(request, 'programacion_lineal/redes.html')

def impriRep():
    # df = pd.DataFrame([
    # dict(Task="Construccion de sub-base", Start='2009-02-20', Finish='2009-05-30', Resource="Ken"),
    # dict(Task="Construccion de base", Start='2009-02-20', Finish='2009-05-30', Resource="August"),
    # dict(Task="Construccion de la superficie de pavimento o rodadura", Start='2009-02-20', Finish='20022-05-30', Resource="oha"),
    # dict(Task="Construccion de estructuras de puentes", Start='2009-02-20', Finish='2009-05-30', Resource="aah"),
    # dict(Task="Construccion de las se;ales y marcas de trafico", Start='2009-02-20', Finish='2009-05-30', Resource="membre")
    # ])
    # fig = px.timeline(df, x_start="Start", x_end="Finish", y="Resource", color="Resource")
    # fig.write_image("figu1.pdf")
    pass

def Redes(request):
    return render(request, "redes/redes.html")