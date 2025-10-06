class Pila:

    def __init__(self):
        self.contenido = []

    def insertar(self, elemento):
        self.contenido.append(elemento)
    
    def size(self):
        return len(self.contenido)
    
    def esta_vacia(self):
        return self.size() == 0
    
    def quitar(self):
        if not (self.esta_vacia()):
            return self.contenido.pop()
        raise IndexError("La pila está vacía")
    
    def inspeccionar(self):
        if self.esta_vacia():
            raise IndexError("La pila está vacía")
        return self.contenido[-1]
    
    def __str__(self):
        return f"Pila con {self.size()} elementos.\
              Contenido: {self.contenido}"
    
pila = Pila()
pila.insertar(3)
pila.insertar(90)

print(pila)

pila.quitar()
print(pila)

pila.insertar("Hola mundo")
print(pila)
print(f"¿Está vacía? {pila.esta_vacia()}")
print(f"Elemento tope {pila.inspeccionar()}")
print(f"Tamaño pila: {pila.size()}")

pila.quitar()
pila.quitar()
print(f"Tamaño pila: {pila.size()}")
print(f"¿Está vacía? {pila.esta_vacia()}")

def invertir_lista(lista:list):
    pila = Pila()
    lista_invertida = []

    for e in lista:
        pila.insertar(e)

    for i in range(pila.size()):
        lista_invertida.append(pila.quitar())

    return lista_invertida

print(invertir_lista([1, 2, 3]))
print(invertir_lista(["Primero", 18, 52, 453, "Chau"]))



def expresion_balanceda_dif_llaves(expresion: str) -> bool:
    parejas = {")": "(", "]": "[", "}": "{"}

    pila = Pila()

    for c in expresion:
        if c in parejas.values():
            pila.insertar(c)
        else:
            if pila.esta_vacia():
                print("No balanceada")
                return False
            if parejas[c] == pila.inspeccionar():
                pila.quitar()
            else:
                print("No balanceada")
                return False

    if pila.esta_vacia():
        print("Balanceada")
        return True
    else:
        print("No balanceada")
        return False


#parejas["]"] = "["
#parejas[c] → devuele el valor de esa clave que se pasa por parámetro

expresion_balanceda_dif_llaves("{[()]}")
expresion_balanceda_dif_llaves("{[()])}")
expresion_balanceda_dif_llaves("{[((()])}")