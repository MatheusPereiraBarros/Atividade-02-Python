def minutos(valor):
    return((valor/100)*60)+(valor%100)

def horas(valor):
    return valor/100

def segundos(valor):
    return (valor/100)*3600


valor = int(input("Digite no formato HHMM: "))

print("Passaram-se %d horas" % horas(valor))
print("Passaram-se %d minutos" % minutos(valor))
print("Passaram-se %d segundos" % segundos(valor))

