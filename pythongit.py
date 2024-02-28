testo = input("Ingrese el tecto que desea ingresar: ")


def detecte_pinga_de_mono(texto):
    msj = True
    if texto != "pinga de mono":
        msj = False
    return msj


def main():
    msj = detecte_pinga_de_mono(testo)
    if msj:
        print("efectivamente pinga de mono")
    else:
        print("Isn´t pinga de mono")


if __name__ == '__main__':
    main()
