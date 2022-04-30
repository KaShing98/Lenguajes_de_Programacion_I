package main

import (
	"fmt"
	"os"
	"sync"
)

var mutex = &sync.Mutex{}

func countDir(path string) int {
	var wg sync.WaitGroup

	count := 0
	// Abrir directorio
	if dir, err := os.ReadDir(path); err == nil {
		for _, subdir := range dir {
			// Si no es un directorio suma, sino iterar
			if !subdir.IsDir() {

				mutex.Lock()
				count += 1
				mutex.Unlock()

			} else {
				// Sumar por cada nuevo proceso
				wg.Add(1)
				// Nueva co-rutina
				go func(path string) {
					defer wg.Done()

					sum := countDir(path)

					mutex.Lock()
					count += sum
					mutex.Unlock()

				}(path + "/" + subdir.Name())

			}
		}
	}
	// Esperar que todos los del mismo nivel terminen
	wg.Wait()
	return count
}

func main() {
	path := "Parcial_II"
	count := countDir(path)

	fmt.Println("Total: ", count)
}
