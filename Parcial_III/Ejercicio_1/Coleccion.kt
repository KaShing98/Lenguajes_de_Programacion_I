
abstract class Coleccion<T: Any> {
    public var elementos: MutableList<T> = mutableListOf()
    
    abstract fun agregar(elemento: T)
    abstract fun eliminar(elemento: T)
    abstract fun vacio() : Boolean

    fun size() : Int {
        return elementos.size
    }
}

public class Conjunto<T: Any> : Coleccion<T>() {
    override fun agregar(elemento: T) {
        if (!elementos.contains(elemento)) {
            elementos.add(elemento)
        } else {
            println("ERROR: El elemento ya existe")
        }
    }

    override fun eliminar(elemento: T) {
        if (elementos.contains(elemento)) {
            elementos.remove(elemento)
        } else {
            println("ERROR: El elemento no existe")
        }
    }

    override fun vacio() : Boolean {
        return elementos.size == 0
    }
}

public class Bolsa<T: Any> : Coleccion<T>() {
    override fun agregar(elemento: T) {
        elementos.add(elemento)
    }

    override fun eliminar(elemento: T) {
        if (elementos.contains(elemento)) {
            while(elementos.contains(elemento)) {
                elementos.remove(elemento)
            }
        }else {
            println("ERROR: El elemento no existe")
        }
    }

    override fun vacio() : Boolean {
        return elementos.size == 0
    }
}

fun main() {
	val c = Conjunto<Int>()

    print("========= Conjunto =========\n")
    print("Vacio: ${c.vacio()}, Size: ${c.size()}\n")
    c.agregar(42)
    print("Vacio: ${c.vacio()}, Size: ${c.size()}\n")
    c.agregar(42)
    print("Vacio: ${c.vacio()}, Size: ${c.size()}\n")
    c.eliminar(42)
    print("Vacio: ${c.vacio()}, Size: ${c.size()}\n")
    c.agregar(13)
    c.agregar(14)
    print("Vacio: ${c.vacio()}, Size: ${c.size()}\n")
    c.eliminar(42)
    print("Vacio: ${c.vacio()}, Size: ${c.size()}\n")

    val b = Bolsa<String>()

    print("========= Bolsa =========\n")
    print("Vacio: ${b.vacio()}, Size: ${b.size()}\n")
    b.agregar("12")
    print("Vacio: ${b.vacio()}, Size: ${b.size()}\n")
    b.agregar("12")
    print("Vacio: ${b.vacio()}, Size: ${b.size()}\n")
    b.eliminar("12")
    print("Vacio: ${b.vacio()}, Size: ${b.size()}\n")
    b.agregar("42")
    b.agregar("56")
    print("Vacio: ${b.vacio()}, Size: ${b.size()}\n")
    b.eliminar("12")
    print("Vacio: ${b.vacio()}, Size: ${b.size()}\n")
    
}