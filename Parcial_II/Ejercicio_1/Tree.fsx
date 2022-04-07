type Arbol<'a when 'a : comparison> = 
    | Hoja of 'a 
    | Rama of 'a * Arbol<'a> * Arbol<'a>
    // Funcion que retorna el valor de la raíz o rama
    member this.value (a : Arbol<'a>) : 'a =
        match a with
        | Hoja(x) -> x
        | Rama(x, y, z) -> x
    // Funcion que retorna si un arbol es un minHeap
    member this.isMinHeap (a : Arbol<'a>) : bool =
        match a with
        | Hoja(_) -> true
        | Rama(a, b, c) -> this.isMinHeap(b) && this.isMinHeap(c) && a <= this.value(b) && a <= this.value(c)
    // Funcion que retorna si un arbol esta balanceado
    member this.isBalanced (a : Arbol<'a>) : bool =
        match a with
        | Hoja(_) -> true
        | Rama(a, b, c) -> this.isBalanced(b) && this.isBalanced(c) && this.height(b) <= this.height(c) + 1 && this.height(c) <= this.height(b) + 1
    // Funcion que retorna la altura de un arbol
    member this.height (a : Arbol<'a>) : int = 
        match a with
        | Hoja(_) -> 0
        | Rama(a, b, c) -> 1 + max (this.height(b)) (this.height(c))
    // Funcion que retorna si un arbol es un min heap balanceado
    member this.esMinHeapBalanceado (a : Arbol<'a>) : bool =
        (this.isMinHeap(a)) && (this.isBalanced(a))

[<EntryPoint>]
let main args =
    //   d 
    // a   b
    let a = Hoja "a"
    let b = Hoja "b"
    let c = Rama("d", a, b)
    printfn "%b" (c.esMinHeapBalanceado(c))

    //      a
    //   c    b
    // d  e
    //   e  f
    let a = Rama("c", Hoja "d", Rama("e", Hoja "e", Hoja "f"))
    let b = Hoja "b"
    let c = Rama("a", a, b)
    printfn "%b" (c.esMinHeapBalanceado(c))

    // c
    let a = Hoja "c"
    printfn "%b" (c.esMinHeapBalanceado(a))

    //   0 
    // 1  12
    let a = Hoja 1
    let b = Hoja 12
    let c = Rama(0, a, b)
    printfn "%b" (c.esMinHeapBalanceado(c))

    // Return 0. This indicates success.
    0
