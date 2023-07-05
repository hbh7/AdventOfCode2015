package main

import (
	"bufio"
	"fmt"
	"os"
)

const inputFilename string = "input.txt"

// CheckError is a helper function to CheckError for errors more conveniently. From https://gobyexample.com/reading-files
func CheckError(e error) {
	if e != nil {
		panic(e)
	}
}

func processInput(inputFile *os.File) {
	part1count := 0
	part2count := 0
	// Loop over each line in input file and process by adding data to hashmap
	scanner := bufio.NewScanner(inputFile)
	for scanner.Scan() {
		// Grab the line
		line := scanner.Text()

		lineCount := 0
		for i := 0; i < len(line); i++ {
			lineCount++
			if string(line[i]) == "\\" && string(line[i+1]) == "\\" {
				i++
			} else if string(line[i]) == "\\" && string(line[i+1]) == "\"" {
				i++
			} else if string(line[i]) == "\\" && string(line[i+1]) == "x" {
				i += 3
			}
		}
		// Subtract 2 for the start and end quotes for part 1
		lineCount -= 2

		// Tally part 1
		part1count += len(line) - lineCount

		// Counting for part 2
		lineCount = 2
		for i := 0; i < len(line); i++ {
			lineCount++
			if string(line[i]) == "\"" || string(line[i]) == "\\" {
				lineCount++
			}
		}
		part2count += lineCount - len(line)
	}
	CheckError(scanner.Err())
	fmt.Printf("Part 1 Count: %d\n", part1count)
	fmt.Printf("Part 2 Count: %d\n", part2count)
}

func main() {
	// Read in input file
	inputFile, err := os.Open(inputFilename)
	CheckError(err)
	defer func(inputFile *os.File) {
		CheckError(inputFile.Close())
	}(inputFile)

	// Run calculations
	processInput(inputFile)
}
