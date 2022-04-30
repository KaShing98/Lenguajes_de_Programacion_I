public class Grafo<T: Any>() {
    var lados: MutableList<MutableList<T>> = mutableListOf()
    var vertices: MutableList<T> = mutableListOf()

    public fun agregarLado (i: T, f: T) {
        if (vertices.contains(i)) {
            val index = vertices.indexOf(i)
            lados[index].add(f)
        } else {
            vertices.add(i)
            lados.add(mutableListOf())
            lados[lados.size - 1].add(f)
        }

        if (vertices.contains(f)) {
            val index = vertices.indexOf(f)
            lados[index].add(i)
        } else {
            vertices.add(f)
            lados.add(mutableListOf())
            lados[lados.size - 1].add(i)
        }
    }
}

abstract class Busqueda {   
    abstract fun buscar(D: Int, H: Int) : Int
}

public class DFS(var grafo: Grafo<Int>): Busqueda() {

    override fun buscar(D: Int, H: Int) : Int {
        var stack: ArrayDeque<Int> = ArrayDeque()
        var discovered_index: ArrayDeque<Int?> = ArrayDeque()
        var nodes: Int = 0

        print("======= Path =======\n")
        stack.addLast(D)
        while (!stack.isEmpty()) {
            val actual = stack.removeLastOrNull()
            print("Vertice actual: ${actual}\n")

            if (actual == H) {
                print("=====  Success =====\n")
                return nodes
            }

            val index = grafo.vertices.indexOf(actual)
            if (discovered_index.contains(actual)) {
                continue
            }
            discovered_index.addLast(actual)

            for (i in grafo.lados[index]) {
                if (!discovered_index.contains(i)) {
                    stack.addLast(i)
                }
            }
            nodes += 1
        }
        print("======= Fail =======\n")
        return -1;
    }
}

public class BFS(var grafo: Grafo<Int>): Busqueda() {

    override fun buscar(D: Int, H: Int) : Int {
        var queue: ArrayDeque<Int> = ArrayDeque()
        var discovered_index: ArrayDeque<Int?> = ArrayDeque()
        var nodes: Int = 0

        print("======= Path =======\n")
        queue.addFirst(D)
        while (!queue.isEmpty()) {
            val actual = queue.removeFirstOrNull()
            print("Vertice actual: ${actual}\n")

            if (actual == H) {
                print("=====  Success =====\n")
                return nodes
            }

            val index = grafo.vertices.indexOf(actual)
            if (discovered_index.contains(actual)) {
                continue
            }
            discovered_index.addLast(actual)

            for (i in grafo.lados[index]) {
                if (!discovered_index.contains(i)) {
                    queue.addLast(i)
                }
            }
            nodes += 1
        }
        print("======= Fail =======\n")
        return -1;
    }
}

fun main() {
	val g = Grafo<Int>()

    g.agregarLado(1, 2)
    g.agregarLado(1, 7)
    g.agregarLado(1, 8)
    g.agregarLado(2, 3)
    g.agregarLado(2, 6)
    g.agregarLado(3, 4)
    g.agregarLado(3, 5)
    g.agregarLado(8, 9)
    g.agregarLado(12, 8)
    g.agregarLado(9, 10)
    g.agregarLado(11, 9)

    var dfs = DFS(g)
    print("======== DFS ========\n\n")
    println("Total nodos: ${dfs.buscar(1, 10)}\n\n")
    println("Total nodos: ${dfs.buscar(1, 14)}\n\n")

    var bfs = BFS(g)
    print("\n\n======== BFS ========\n\n")
    println("Total nodos: ${bfs.buscar(1, 10)}\n\n")
    println("Total nodos: ${bfs.buscar(1, 14)}\n\n")

    val with_cycle = Grafo<Int>()

    with_cycle.agregarLado(1, 2)
    with_cycle.agregarLado(1, 7)
    with_cycle.agregarLado(1, 8)
    with_cycle.agregarLado(2, 3)
    with_cycle.agregarLado(2, 6)
    with_cycle.agregarLado(3, 4)
    with_cycle.agregarLado(3, 5)
    with_cycle.agregarLado(8, 9)
    with_cycle.agregarLado(12, 8)
    with_cycle.agregarLado(9, 10)
    with_cycle.agregarLado(9, 12)
    with_cycle.agregarLado(11, 9)

    var dfs_c = DFS(with_cycle)
    print("\n\n======== DFS ========\n\n")
    println("Total nodos: ${dfs_c.buscar(1, 10)}\n\n")

    var bfs_c = BFS(with_cycle)
    print("\n\n======== BFS ========\n\n")
    println("Total nodos: ${bfs_c.buscar(1, 10)}\n\n")

    // Grafo g
    //        1
    //      / | \
    //     2  7  8
    //    / \    | \
    //   3   6   9  12
    //  / \      |\
    // 4   5    10 11
    
    // Grafo with_cycle
    //        1
    //      / | \
    //     2  7  8
    //    / \    | \
    //   3   6   9-12
    //  / \      |\
    // 4   5    10 11

}