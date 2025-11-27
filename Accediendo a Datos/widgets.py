# leer widgets log
with open("Archivos/widgets.txt", "r") as f_in: 
    lines = f_in.readlines()

contador = 0

# 2. Calcular pago (10% bonus por >50 widgets)
overtime_report = []
for line in lines:
    contador += 1
    produced = int(line.strip())
    if produced > 50:
        bonus = produced * 0.10
    else:
        bonus = 0
    overtime_report.append(f"Produced: {produced}, Bonus: {round(bonus, 2)}")  

#  Producir informe final
with open("Archivos/overtime_report.txt", "w") as f_out:
    for i in range(0, contador):
        f_out.write((overtime_report[i]) + "\n")

print(f"Overtime report generado con {contador} lineas.") 
