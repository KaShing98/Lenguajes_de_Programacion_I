import kotlin.math.*

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
