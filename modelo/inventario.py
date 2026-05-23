from modelo.producto import Producto


class Inventario:
    def __init__(self):
        self.__productos: list[Producto] = []

    @property
    def productos(self) -> list[Producto]:
        return self.__productos

    def buscar_producto(self, codigo: str) -> Producto | None:
        for producto in self.__productos:
            if producto.codigo == codigo:
                return producto
        return None

    def agregar_producto(self, producto: Producto) -> bool:
        if self.buscar_producto(producto.codigo) is not None:
            return False
        self.__productos.append(producto)
        return True

    def actualizar_stock(self, codigo: str, cantidad: int) -> bool:
        producto = self.buscar_producto(codigo)
        if producto is None:
            return False
        return producto.modificar_stock(cantidad)

    def consultar_stock(self, codigo: str) -> int | None:
        producto = self.buscar_producto(codigo)
        if producto is None:
            return None
        return producto.stock
