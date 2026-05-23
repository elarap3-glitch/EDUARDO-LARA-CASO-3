from modelo.producto import Producto
from modelo.inventario import Inventario


def main():
    inventario = Inventario()

    # Agregar 3 productos
    p1 = Producto("P001", "Cuaderno", 2.50, 40)
    p2 = Producto("P002", "Lápiz", 0.50, 100)
    p3 = Producto("P003", "Borrador", 0.30, 25)

    inventario.agregar_producto(p1)
    inventario.agregar_producto(p2)
    inventario.agregar_producto(p3)

    # Aumentar el stock de uno
    inventario.actualizar_stock("P001", 15)  # +15 cuadernos

    # Reducir el stock de otro
    inventario.actualizar_stock("P002", -20)  # -20 lápices

    # Intento inválido (no debe permitir stock negativo)
    operacion_invalida = inventario.actualizar_stock("P003", -100)
    print("¿Se pudo descontar 100 borradores?:", operacion_invalida)

    # Mostrar stock final de un producto
    stock_final_lapiz = inventario.consultar_stock("P002")
    print("Stock final de Lápiz (P002):", stock_final_lapiz)

    # Mostrar resumen general
    print("\nInventario actual:")
    for producto in inventario.productos:
        print(producto)


if __name__ == "__main__":
    main()
