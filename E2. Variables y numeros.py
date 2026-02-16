#1 crear variable "numero1" con el valor 5
#2 crear variable "numero2" con el valor 3
#3 crear variable "suma" con las suma de las ddos variables anteriores
#4 convertir la variable "suma" en una cadena de caracteres y llamarla "strsuma"
#5 crear una variable resultado que concatene el texto "el resultado es" y la variable "strsuma"


numero1=5
numero2=3
suma=numero1+numero2
print(suma)
strsuma=str(suma)
type(strsuma)
print((type(strsuma)))

resultado="el resultado es"
print(resultado +" "+ strsuma)


#Convertir a str sirve cuando necesitas:
#Mostrar información
#Guardar datos
#Enviar información
#Manipular el número como texto