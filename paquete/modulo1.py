class Cliente:
    # Constructor de la clase
    def __init__(self, nombre, apellido, edad, mail, domicilio) -> None:
        self._nombre = nombre,
        self._apellido = apellido,
        self._edad = edad,
        self._mail = mail,
        self._domicilio = domicilio,
        self.carrito = []

    # getter and Setter de los atributos
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    
    @property
    def apellido(self):
        return self._apellido
    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad
    @edad.setter
    def edad(self, edad):
        self._edad = edad
    
    @property
    def mail(self):
        return self._mail
    @mail.setter
    def mail(self, mail):
        self._mail = mail

    @property
    def domicilio(self):
        return self._domicilio
    @domicilio.setter
    def domicilio(self, domicilio):
        self._domicilio = domicilio

    # Metodos de la clase Cliente
    def agregar_carrito(self, producto, tienda):
        self.carrito.append(producto)
        print(f"Se agrego al carrito el producto {producto} de la tienda {tienda}")
    def ver_carrito(self):
        print(f"\nProductos del carrito: ")
        for prod in self.carrito:
            print(f"\t-{prod}")
    def comprar(self):
        print("\nCompra realizada con exito: ")
        for prod in self.carrito:
            print(f"\t-{prod}")
    def exit(self):
        print("\nGracias por comprar, vuelva prontos!")
    def __str__(self):
        return f"Se ha creado al cliente {self._nombre[0]}\n"
