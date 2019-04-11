qcigarro =  int ( input ())
anosFumando =  int ( input ())

c1 = qcigarro * 10  # 100 cigarros diarios = 1000 minutos perdidos
c2 = anosFumando * 12  # 5 anos fumando = 60 meses = 21900 dias fumando = 525600 horas = 31536000 minutos

anosPerdidos = (((c1 / 60 ) / 24 ) / 365 )

cFinal = ((((c1 * 365 ) * calc2) / 12 ) / 1000 ) / 60

print ( " Você perdeu % d anos " % (cFinal))
