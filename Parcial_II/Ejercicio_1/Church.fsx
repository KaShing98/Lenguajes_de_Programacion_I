type Church = 
    | Cero of Cero : int
    | Suc of Church : Church
    // Funcion suma
    static member (+) (x : Church, y : Church) : Church =
        match x with
        | Church.Cero(xx) -> y
        | Church.Suc(xx) -> xx + Suc(y)
    // Funcion multiplicacion
    static member (*) (x : Church, y : Church) : Church =
        match x with
        | Church.Cero(xx) -> Cero(xx)
        | Church.Suc(xx) -> y + (xx * y)

// Funcion para convertir un numeral Church en enteros
let rec toInt c = 
    match c with
    | Church.Cero(c) -> c
    | Church.Suc(cc) -> toInt(cc) + 1
    
[<EntryPoint>]
let main args =
    // a = 2
    let a = Suc(Suc(Cero(0)))
    printfn "%i" (toInt(a))

    // 0 + 4
    let c = Cero(0) + Suc(Suc(a))
    printfn "%i" (toInt(c))

    // 4 + 0
    let c = Suc(Suc(a)) + Cero(0) 
    printfn "%i" (toInt(c))

    // 4 + 2
    let c = Suc(Suc(a)) + a
    printfn "%i" (toInt(c))

    // 2 + 4
    let c = a + Suc(Suc(a))
    printfn "%i" (toInt(c))

    // 0 * 4
    let c = Cero(0) * Suc(Suc(a))
    printfn "%i" (toInt(c))

    // 4 * 0
    let c = Suc(Suc(a)) * Cero(0)
    printfn "%i" (toInt(c))

    // 4 * 2
    let c = Suc(Suc(a)) * a
    printfn "%i" (toInt(c))

    // 2 * 4
    let c = a * Suc(Suc(a))
    printfn "%i" (toInt(c))

    // Return 0. This indicates success.
    0

