def main():
    sx = input()
    id = int(input())
    Tn = int(input())
    Trn = int(input())
    Tc = int(input())
    Trc = int(input())
    Tcor = int(input())
    tempatleta(Tn,Trn,Tc,Trc,Tcor,sx)
    analise(sx,id,Tn,Trn,Tc,Trc,Tcor)
    
    
def tempatleta(Tn,Trn,Tc,Trc,Tcor,sx):
    tempo = (Tn + Trn + Tc +Trc + Tcor)
    horas = tempo // 60
    minutos = tempo%60
    if (sx =="M" or sx =="m"):
        print(f"Tempo do atleta: {horas:02d}h {minutos:02d}min")
    else:
        print(f"Tempo da atleta: {horas:02d}h {minutos:02d}min")


def analise(sx,id,Tn,Trn,Tc,Trc,Tcor):
    temp = (Tn + Trn + Tc +Trc + Tcor)
    
    if id >= 18 and id <=29:
        if sx =="M" or sx =="m":
            maximo = 480
        else:
            maximo = 490
    elif id >=30 and id <=34:
        if sx =="M" or sx =="m":
            maximo = 490
        else:
            maximo = 500
    elif id >=35 and id <=39:
        if sx =="M" or sx =="m":
            maximo = 505
        else:
            maximo = 520
    elif id >=40 and id <=44:
        if sx =="M" or sx =="m":
            maximo = 515
        else:
            maximo = 540
    elif id >=45 and id <=49:
        if sx =="M" or sx =="m":
            maximo = 530
        else:
            maximo = 560
    elif id >=50 and id <=54:
        if sx =="M" or sx =="m":
            maximo = 540          
        else:
            maximo = 580
    elif id >= 55 and id <=59:
        if sx =="M" or sx =="m":
            maximo = 555
        else:
            maximo = 600
    elif id >=60 and id <=64:
        if sx =="M" or sx =="m":
            maximo = 570
        else:
            maximo = 630
    elif id >=64 and id <=69:
        if sx =="M" or sx =="m":
            maximo = 590
        else:
            maximo = 660
    elif id >=70 and id <=74:
        if sx =="M" and sx =="m":
            maximo = 620
        else:
            maximo = 705
    elif id >=75 and id <=79:
        if sx =="M" or sx =="m":
            maximo = 660
        else:
            maximo = 750
    elif id >=80:
        if sx =="M" or sx =="m":
            maximo = 720
        else:
            maximo = 810
    print(f"Tempo necessario: {maximo//60:02d}h {maximo%60:02d}min")
            
    
    if temp <= maximo:
        print("Conseguiu indice? SIM")
    else:
        print("Conseguiu indice? NAO")
    
    conta =(temp - maximo)
    if sx =="M" or sx =="m":
        if conta <=0:
            print(f"O atleta terminou a prova {(conta*(-1))//60:02d}h {conta*(-1)%60:02d}min abaixo do indice")
        else:
            print(f"O atleta terminou a prova {conta//60:02d}h {conta%60:02d}min acima do indice")
    else:
        if conta <=0:
            print(f"A atleta terminou a prova {(conta*(-1))//60:02d}h {conta*(-1)%60:02d}min abaixo do indice")
        else:
            print(f"A atleta terminou a prova {conta//60:02d}h {conta%60:02d}min acima do indice")
main()