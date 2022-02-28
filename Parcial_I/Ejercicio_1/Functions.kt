import kotlin.math.*

/*
    Precondición: b > 0
    Postcondición: a^b

    El algoritmo empleado es el de binary power:
        a^n = 1                  if n == 0
        a^n = (a^(n/2))²         if n > 0, n es par
        a^n = (a^((n-1)/2))² * a if n > 0, n es impar
*/
fun Power(a: Int, b: Int): Long {
    var base = a.toLong()
    var exponent = b.toLong()
    var answer: Long = 1


    while (exponent > 0) {
        if ((exponent and 1) > 0) {
            answer = answer * base
        }
        base *= base
        exponent = exponent shr 1
    }
    return answer
}

/*
    Función que genera test random y los verifica contra la función de pow de kotlin
*/
fun RunPowerTests() {
    val powerTestRun = true
    val numberTestCases = 10

    if (powerTestRun) {
        var succesful = 0
        for (num in 1..numberTestCases) {
            var a = (0..15).random()
            var b = (0..15).random()
            if (Power(a, b) == a.toDouble().pow(b).toLong()) {
                succesful += 1
            }
        }
        println("La función Power completó $succesful tests exitosamente de $numberTestCases")
    }
}

/*
    Precondición: a y b son Array de IntArray
    Postcondición: Array de Intarray con el producto de a y b
*/
fun Multiplication(a: Array<IntArray>, b: Array<IntArray>): Array<IntArray>{
    val N = a.size
    val M = a[0].size
    val P = b[0].size

    val product = Array(N) { IntArray(P) }
    for (i in 0..N - 1) {
        for (j in 0..P - 1) {
            for (k in 0..M - 1) {
                product[i][j] += a[i][k] * b[k][j]
            }
        }
    }

    return product
}

/*
    Función que genera test random e imprime el resultado
*/
fun RunMatrixMultiplicationTests() {
    val N = (1..15).random()
    val M = (1..15).random()
    val P = (1..15).random()

    println("Primera matrix (NxM):")
    val a = Array(N) { IntArray(M) }
    for (i in 0..N-1) {
        a[i] = IntArray(M) { (0..15).random() }
        println(a[i].contentToString())
    }

    println("Segunda matrix (MxP):")
    val b = Array(M) { IntArray(P) }
    for (i in 0..M-1) {
        b[i] = IntArray(P) { (0..15).random() }
        println(b[i].contentToString())
    }

    println("Resultado de la multiplicación:")
    var answer = Multiplication(a, b)
    for (i in answer.indices) {
        println(answer[i].contentToString())
    }
}
