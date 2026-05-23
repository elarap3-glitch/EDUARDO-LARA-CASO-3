class Producto:
    def __init__(self, codigo: str, nombre: str, precio: float, stock: int):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    @property
    def codigo(self) -> str:
        return self.__codigo

    @codigo.setter
    def codigo(self, valor: str) -> None:
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El código debe ser una cadena no vacía.")
        self.__codigo = valor.strip()

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El nombre debe ser una cadena no vacía.")
        self.__nombre = valor.strip()

    @property
    def precio(self) -> float:
        return self.__precio

    @precio.setter
    def precio(self, valor: float) -> None:
        if valor < 0:
            raise ValueError("El precio no puede ser negativo.")
        self.__precio = float(valor)

    @property
    def stock(self) -> int:
        return self.__stock

    @stock.setter
    def stock(self, valor: int) -> None:
        if not isinstance(valor, int):
            raise TypeError("El stock debe ser un número entero.")
        if valor < 0:
            raise ValueError("El stock no puede ser negativo.")
        self.__stock = valor

    def hay_stock(self, cantidad: int) -> bool:
        if cantidad < 0:
            raise ValueError("La cantidad a verificar no puede ser negativa.")
        return self.__stock >= cantidad

    def modificar_stock(self, cantidad: int) -> bool:
        nuevo_stock = self.__stock + cantidad
        if nuevo_stock < 0:
            return False
        self.__stock = nuevo_stock
        return True

    def __str__(self) -> str:
        return (
            f"Producto(codigo='{self.codigo}', nombre='{self.nombre}', "
            f"precio={self.precio:.2f}, stock={self.stock})"
        )
