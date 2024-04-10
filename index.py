"""Desafio 
problema: Dados s valores de horários abaixo, decifre a lógica e faça um codigo para executar
entrada01 3:45
entrada02 14:20
saida 06:05"""

hour1 = 3
minute1 = 45
hour2 = 14
minute2 = 20

finalMinute = minute1 + minute2
finalHour = hour1 + hour2

if(finalMinute >= 60):
    finalMinute = finalMinute - 60
    finalHour = finalHour + 1
    
if(finalHour >= 12):
    finalHour = finalHour - 12

print(f"{finalHour}:{finalMinute}")