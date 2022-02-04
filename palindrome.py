#Averiguar si una cadena de caracteres es un palindromo o no.
#Palindromo es una cadena que se lee del mismo modo en los dos sentidos. 
#Ejemplo ana, luz azul, ...

def is_palindrome(string: str) -> bool: #Creamos la función que nos devolverá si una palabra es palíndromo o no
    #Esta función se ha programado con tipado estatico, le decimos que solo aceptamos string y que nos devolverá bool

    string = string.replace(" ", "").lower() #Eliminamos los espacios en blanco y convertimos a minúsculas para poder
    #hacer la comparación, ya que python distingue entre mayúsculas y minúsculas, además de si ponemos una frase, los
    #espacios en blanco cuentan como carácteres. 
    return string == string[::-1] #Realiza la comparación y devuelve True o False.


def run():
    
    print(is_palindrome(1000)) #Si pasamos la palabra Ana, hola, etc en modo string funciona sin problema
    #Pero si le pasamos un entero saltará un error pero no bien explicado, con lo cuál vamos a utilizar el 
    #módulo mypy para resolverlo.
    #Este módulo se utiliza desde la terminal escribiendo el siguiente comando para que ejecute el programa.
    #mypy palindrome.py --check-untyped-defs


if __name__ == '__main__':
    run()



