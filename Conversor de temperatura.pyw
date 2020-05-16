# Conversor de temperatura
# Celsius - Kelvin - Farenheit

from tkinter import *
from tkinter import messagebox

ventPrincipal = Tk()
ventPrincipal.title("Conversor de temperatura")
#ventPrincipal.iconbitmap("src/logo.ico")
ventPrincipal.geometry("300x130")
ventPrincipal.resizable(0, 0)

celsiusS = StringVar()
kelvinS = StringVar()
farenheitS = StringVar()

# Funciones


def convertirGrados():
    try:
        if celsiusEntry.get() != "" and str(celsiusEntry.focus_displayof()) == ".!entry":
            kelvinS.set(float(celsiusEntry.get()) + 273.15)
            farenheitS.set(((float(celsiusEntry.get()) * 9) / 5) + 32)
            celsiusEntry.focus_set()
        elif kelvinEntry.get() != "" and str(celsiusEntry.focus_displayof()) == ".!entry2":
            celsiusS.set(float(kelvinEntry.get()) - 273.15)
            farenheitS.set(
                (((float(kelvinEntry.get()) - 273.15) * 9) / 5) + 32)
            kelvinEntry.focus_set()
        elif farenheitEntry.get() != "" and str(celsiusEntry.focus_displayof()) == ".!entry3":
            celsiusS.set((5 * (float(farenheitEntry.get()) - 32)) / 9)
            kelvinS.set(
                ((5 * (float(farenheitEntry.get()) - 32)) / 9) + 273.15)
            farenheitEntry.focus_set()
    except ValueError:
        messagebox.showerror(
            "Error", "Error en la conversion de unidades " + str(ValueError))

def limpiarCampos():
    celsiusS.set("")
    kelvinS.set("")
    farenheitS.set("")

def salida():
    valor = messagebox.askyesno("Salida","Desea salir?")
    if valor == 1:
        sys.exit(0)

def ayuda():
    messagebox.showinfo("Informacion","Ingresa un valor de temperatura en uno de los cuadros y pulsa Convertir")

tempLabel = Label(ventPrincipal, text="Temperaturas:", font="ArialBlack")
tempLabel.grid(row=0, column=0)
celsiusLabel = Label(ventPrincipal, text="Celsius", font="Arial")
celsiusLabel.grid(row=1, column=0, sticky=W)
kelvinLabel = Label(ventPrincipal, text="Kelvin", font="Arial")
kelvinLabel.grid(row=2, column=0, sticky=W)
farenheitLabel = Label(ventPrincipal, text="Farenheit", font="Arial")
farenheitLabel.grid(row=3, column=0, sticky=W)

celsiusEntry = Entry(ventPrincipal, textvariable=celsiusS)
celsiusEntry.grid(row=1, column=1)
kelvinEntry = Entry(ventPrincipal, textvariable=kelvinS)
kelvinEntry.grid(row=2, column=1)
farenheitEntry = Entry(ventPrincipal, textvariable=farenheitS)
farenheitEntry.grid(row=3, column=1)

convertirBoton = Button(ventPrincipal, text="Convertir",
                        font="ArialBlack", command=convertirGrados)
convertirBoton.grid(row=4, column=1, sticky=W)
limpiarBoton = Button(ventPrincipal, text="Limpiar",
                      font="ArialBlack", command=limpiarCampos)
limpiarBoton.grid(row=4, column=0)

barraMenu = Menu(ventPrincipal)
ventPrincipal.config(menu=barraMenu)
fuentesMenu = Menu(barraMenu, tearoff=0)
fuentesMenu.add_command(label="Informacion", command=ayuda)
fuentesMenu.add_command(label="Salir", command=salida)

barraMenu.add_cascade(label="Ayuda", menu=fuentesMenu)

ventPrincipal.mainloop()
