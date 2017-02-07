def convHoras(valor):
    valorHora = valor/60
    valorMinuto = valor%60
    print(int(valorHora))
    print(valorMinuto)

def main():
    valorMinutos = (int(input("Insira o valor: ")))
    convHoras(valorMinutos)

main()
