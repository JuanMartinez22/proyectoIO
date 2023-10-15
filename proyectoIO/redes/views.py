from django.shortcuts import render
import plotly.express as px
import pandas as pd
import datetime
from reportlab.pdfgen import canvas

def proceRedes(request):
    fi1=''
    fi2=''
    fi3=''
    fi4=''
    fi5=''
    fi6=''
    fi7=''

    ff1=''
    ff2=''
    ff3=''
    ff4=''
    ff5=''
    ff6=''
    ff7=''
    try:
        if request.method == "POST":
            fi1 = request.POST.get('fi1')
            fi1 = str(fi1)
            fi2 = request.POST.get('fi2')
            fi2 = str(fi2)
            fi3 = request.POST.get('fi3')
            fi3 = str(fi3)
            fi4 = request.POST.get('fi4')
            fi4 = str(fi4)
            fi5 = request.POST.get('fi5')
            fi5 = str(fi5)
            fi6 = request.POST.get('fi6')
            fi6 = str(fi6)
            fi7 = request.POST.get('fi7')
            fi7 = str(fi7)
            
            ff1 = request.POST.get('ff1')
            ff1 = str(ff1)
            ff2 = request.POST.get('ff2')
            ff2 = str(ff2)
            ff3 = request.POST.get('ff3')
            ff3 = str(ff3)
            ff4 = request.POST.get('ff4')
            ff4 = str(ff4)
            ff5 = request.POST.get('ff5')
            ff5 = str(ff5)
            ff6 = request.POST.get('ff6')
            ff6 = str(ff6)
            ff7 = request.POST.get('ff7')
            ff7 = str(ff7)
            print('holla'+fi7)
            print('holla'+ff7)
            
    except:
        fi1='2023-10-25'
        fi2='2023-10-25'
        fi3='2023-10-25'
        fi4='2023-10-25'
        fi5='2023-10-25'
        fi6='2023-10-25'
        fi7='2023-10-25'

        ff1='2023-10-26'
        ff2='2023-10-26'
        ff3='2023-10-26'
        ff4='2023-10-26'
        ff5='2023-10-26'
        ff6='2023-10-26'
        ff7='2023-10-26'
    impriRep(fi1,ff1,fi2,ff2,fi3,ff3,fi4,ff4,fi5,ff5,fi6,ff6,fi7,ff7)

    return render(request, 'redes/redes.html')

def impriRep(fi1,ff1,fi2,ff2,fi3,ff3,fi4,ff4,fi5,ff5,fi6,ff6,fi7,ff7):
    c = canvas.Canvas('FechasOptimas.pdf')
    df = pd.DataFrame([
        dict(Task="Construccion de drenaje menor", Start=str(fi1), Finish=str(ff1), Resource="Actividad1"),
        dict(Task="Construccion de drenaje mayor", Start=str(fi2), Finish=str(ff2), Resource="Actividad2"),
        dict(Task="Construccion de sub-base", Start=str(fi3), Finish=str(ff3), Resource="Actividad3"),
        dict(Task="Construccion de base", Start=str(fi4), Finish=str(ff4), Resource="Actividad4"),
        dict(Task="Construccion de la superficie de pavimento o rodadura", Start=str(fi5), Finish=str(ff5), Resource="Actividad5"),
        dict(Task="Construccion de estructuras de puentes", Start=str(fi6), Finish=str(ff6), Resource="Actividad6"),
        dict(Task="Construccion de las senales y marcas de trafico", Start=str(fi7), Finish=str(ff7), Resource="Actividad7")
    ])
    fig = px.timeline(df, x_start="Start", x_end="Finish", y="Resource", color="Resource")
    fig.write_image("FechasOptimas.pdf")
    c.setFont('Helvetica', 25)
    c.drawString(150,720,"Reporte de optimizacion Optitech")

def Redes(request):
    return render(request, "redes/redes.html")