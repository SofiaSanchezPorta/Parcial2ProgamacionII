class Cola:

    def __init__(self):
        self.contenido = []

    def encolar(self, elemento):
        self.contenido.append(elemento)

    def size(self):
        return len(self.contenido)

    def esta_vacia(self):
        return self.size() == 0
    
    def primero(self):
        if not self.esta_vacia():
            return self.contenido[0]
        return None
    
    def desencolar(self):
        if self.esta_vacia():
            raise IndexError("La cola está vacía")
        return self.contenido.pop(0)
    
    def __str__(self):
        return f"Cola con {self.size()} elementos.\
            Contenido: {self.contenido}"
    
cola = Cola()
cola.encolar(32)
cola.encolar("Soy el último de la fila")

print(cola)

cola.desencolar()
print(cola)

cola.encolar(38)
print(cola)
print(f"¿Está vacía? {cola.esta_vacia()}")
print(f"Primer elemento {cola.primero()}")
print(f"Tamaño cola: {cola.size()}")

cola.desencolar()
cola.desencolar()
print(f"Tamaño cola: {cola.size()}")
print(f"¿Está vacía? {cola.esta_vacia()}")
