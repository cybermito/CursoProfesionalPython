#Hacer un closure que cuando indiquemos una palabra seguida
#de un número, esta palabra impresa en pantalla repetida el número
#de veces dados. 

#Hola 3 -> HolaHolaHola
#Antonio 2 -> AntonioAntonio
#Atigra 4 -> AtigraAtigraAtigraAtigra

#Este es el closure que cumple las tres reglas
#Tiene una nested function que referencia un valor del scope superior
#
def make_repeater_of(n): # Este es el closure, el valor de n será recordado en cada llamada a la función.
    def repeater(string): #Nested Function 
        assert type(string) == str, "Solo puedes utilizas cadenas"
        return string * n
    return repeater

def run():
    repeat_5 = make_repeater_of(5) #se crea una función que es la nested, la cuál recuerda el valor de n, en este caso el 5.
    print(repeat_5("Hola "))
    repeat_10 = make_repeater_of(10)
    print(repeat_10("Atigra "))

if __name__ == '__main__':
    run()