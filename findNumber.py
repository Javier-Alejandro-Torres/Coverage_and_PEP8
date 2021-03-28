import random
import os

file = open("GuessingSteps.txt", "w")
Numero_Random = random.randint(0, 30)

file.write('Se asigno el número= %s' % Numero_Random + os.linesep + os.linesep)

i = 0
a = True

while a:

        Numero_magico = input("\nDame un Número: \n")
        if (Numero_magico == "exit"):
            file.write("exit" + os.linesep + os.linesep)
            break
        Numero_Usuario = int(Numero_magico)
        file.write('Numero_Usuario=%s' % Numero_Usuario + os.linesep)
        i = i+1

        if (Numero_Usuario > Numero_Random):
            print("Tu numero es muy grande, ingresa uno menor")
            file.write("Numero grande" + os.linesep + os.linesep)

        elif (Numero_Usuario < Numero_Random):
            print("Numero pequeño, porfavor ingresa uno mayor")
            file.write("Numero pequeño " + os.linesep + os.linesep)

        elif (Numero_Usuario == Numero_Random):
            print("Excelente, has acertado!!!!")
            print("Te ha tomado", i, "intentos")
            file.write("Excelente, acertaste!!" + os.linesep + os.linesep)
            file.close()
            break
