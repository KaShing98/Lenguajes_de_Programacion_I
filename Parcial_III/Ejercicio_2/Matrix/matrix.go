package main

import (
	"fmt"
	"sync"
)

type Matrix [][]int

func sumRow(rowA []int, rowB []int, rowC []int) {
	for i := 0; i < len(rowA); i++ {
		rowC[i] = rowA[i] + rowB[i]
	}
}

func sumMatrix(matrixA Matrix, matrixB Matrix) Matrix {
	var wg sync.WaitGroup

	n := len(matrixA)
	m := len(matrixA[0])

	matrixC := make([][]int, n)
	for i := 0; i < n; i++ {
		matrixC[i] = make([]int, m)
	}

	// Generar una co-rutina por cada fila
	for i := 0; i < n; i++ {
		wg.Add(1)
		go func(i int) {
			defer wg.Done()
			sumRow(matrixA[i], matrixB[i], matrixC[i])
		}(i)
	}
	// Esperar a que se sumen todas las filas
	wg.Wait()
	return matrixC
}

func main() {

	a := Matrix{{0, 1, 2, 3}, {4, 5, 6, 7}, {8, 9, 10, 11}}
	b := Matrix{{10, 4, 42, 7}, {6, 5, 32, 7}, {8, 55, 8, 11}}
	c := sumMatrix(a, b)

	fmt.Println(c)
}
