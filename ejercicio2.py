# Escribe un programa que dada una hora
# (expresada en hora, minutos y segundos ) 
# mustre por pantalla el total de segundos transcurridos  desde la ultima 
# medianoche y los que quedan para la siguiente medianoche 

hora=int(input(" hora "));
minuto=int(input(" minuto"));
segundo=int(input(" segundo"));
segundosDIA = 86400

totalsegundos= hora*3600 + minuto*60 + segundo

cUANTOSfaltan = segundosDIA - totalsegundos

print( totalsegundos)
print( cUANTOSfaltan)