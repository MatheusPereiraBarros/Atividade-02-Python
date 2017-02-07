def convMPS(valor):
    valorKMH = valor/3.6
    return valorKMH

def main():
    valorKMH = (int(input("Insira o valor: ")))
    print(convMPS(valorKMH))

main()
