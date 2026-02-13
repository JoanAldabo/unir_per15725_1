class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.validar_nombre(nombre)
        self.validar_precio(precio)
        self.validar_cantidad(cantidad)

        self.nombre = nombre.strip()
        self.precio = float(precio)
        self.cantidad = int(cantidad)

    @staticmethod
    def validar_nombre(nombre):
        if not isinstance(nombre, str) or len(nombre.strip()) == 0:
            raise ValueError("Nombre no válido")

    @staticmethod
    def validar_precio(precio):
        if not isinstance(precio, (int, float)) or precio < 0:
            raise ValueError("Precio no válido")

    @staticmethod
    def validar_cantidad(cantidad):
        if not isinstance(cantidad, int) or cantidad < 0:
            raise ValueError("Cantidad no válida")

    def actualizar_precio(self, nuevo_precio):
        self.validar_precio(nuevo_precio)
        self.precio = float(nuevo_precio)

    def actualizar_cantidad(self, nueva_cantidad):
        self.validar_cantidad(nueva_cantidad)
        self.cantidad = int(nueva_cantidad)

    def calcular_valor_total(self):
        return self.precio * self.cantidad

    def __str__(self):
        return "Producto: {} | Precio: {:.2f} | Cantidad: {} | Total: {:.2f}".format(
            self.nombre,
            self.precio,
            self.cantidad,
            self.calcular_valor_total()
        )


class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        if not isinstance(producto, Producto):
            raise TypeError("Producto no válido")
        self.productos.append(producto)

    def buscar_producto(self, nombre):
        if not isinstance(nombre, str) or len(nombre.strip()) == 0:
            raise ValueError("Nombre no válido")

        nombre = nombre.strip().lower()
        for producto in self.productos:
            if producto.nombre.lower() == nombre:
                return producto
        return None

    def calcular_valor_inventario(self):
        return sum(p.calcular_valor_total() for p in self.productos)

    def listar_productos(self):
        if not self.productos:
            print("Inventario vacío")
            return

        for producto in self.productos:
            print(producto)


def leer_float(mensaje):
    try:
        return float(input(mensaje))
    except ValueError:
        raise ValueError("Entrada no válida")

def leer_int(mensaje):
    try:
        return int(input(mensaje))
    except ValueError:
        raise ValueError("Entrada no válida")


def menu_principal():
    inventario = Inventario()

    while True:
        print("\n1. Agregar producto")
        print("2. Buscar producto")
        print("3. Listar productos")
        print("4. Valor total del inventario")
        print("5. Salir")

        opcion = input("Opción: ").strip()

        try:
            if opcion == "1":
                nombre = input("Nombre: ")
                precio = leer_float("Precio: ")
                cantidad = leer_int("Cantidad: ")

                producto = Producto(nombre, precio, cantidad)
                inventario.agregar_producto(producto)
                print("Producto agregado")

            elif opcion == "2":
                nombre = input("Nombre: ")
                producto = inventario.buscar_producto(nombre)

                if producto is None:
                    print("Producto no encontrado")
                else:
                    print(producto)

            elif opcion == "3":
                inventario.listar_productos()

            elif opcion == "4":
                total = inventario.calcular_valor_inventario()
                print("Total inventario: {:.2f}".format(total))

            elif opcion == "5":
                break

            else:
                print("Opción no válida")

        except (ValueError, TypeError) as e:
            print("Error:", e)


if __name__ == "__main__":
    menu_principal()
