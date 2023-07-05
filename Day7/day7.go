package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

const inputFilename string = "input.txt"

// CheckError is a helper function to CheckError for errors more conveniently. From https://gobyexample.com/reading-files
func CheckError(e error) {
	if e != nil {
		panic(e)
	}
}

type wire struct {
	precalculated bool
	value         uint16
	operation     string
	input1        string
	input2        string
}

func calculateWireValue(wires map[string]wire, target string) uint16 {
	currentWire := wires[target]
	fmt.Println("Calculating wire " + target)
	if !currentWire.precalculated {
		switch currentWire.operation {
		case "AND":
			input1, err := strconv.Atoi(currentWire.input1)
			if err != nil {
				// input1 is another wire, use input
				input1 = int(calculateWireValue(wires, currentWire.input1))
			}
			currentWire.value = uint16(input1) & calculateWireValue(wires, currentWire.input2)

		case "OR":
			currentWire.value = calculateWireValue(wires, currentWire.input1) | calculateWireValue(wires, currentWire.input2)

		case "NOT":
			currentWire.value = ^calculateWireValue(wires, currentWire.input1)

		case "LSHIFT":
			currentWire.value = calculateWireValue(wires, currentWire.input1) << currentWire.value

		case "RSHIFT":
			currentWire.value = calculateWireValue(wires, currentWire.input1) >> currentWire.value

		default:
			// A value is from another wire, use that wire
			currentWire.value = calculateWireValue(wires, currentWire.input1)
		}
	}
	currentWire.precalculated = true
	wires[target] = currentWire
	return currentWire.value
}

func processInput(inputFile *os.File) map[string]wire {
	// Create a hashmap to store wire information
	wires := make(map[string]wire)

	// Loop over each line in input file and process by adding data to hashmap
	scanner := bufio.NewScanner(inputFile)
	for scanner.Scan() {
		// Grab the line
		line := scanner.Text()

		// Split string into necessary parts
		parts := strings.Split(line, " ")
		fmt.Println(parts)
		currentWire := wire{}

		switch {
		case strings.Contains(line, "AND"):
			currentWire.operation = "AND"
			currentWire.input1 = parts[0]
			currentWire.input2 = parts[2]
			wires[parts[4]] = currentWire

		case strings.Contains(line, "OR"):
			currentWire.operation = "OR"
			currentWire.input1 = parts[0]
			currentWire.input2 = parts[2]
			wires[parts[4]] = currentWire

		case strings.Contains(line, "NOT"):
			currentWire.operation = "NOT"
			currentWire.input1 = parts[1]
			wires[parts[3]] = currentWire

		case strings.Contains(line, "LSHIFT"):
			currentWire.operation = "LSHIFT"
			currentWire.input1 = parts[0]
			val, err := strconv.Atoi(parts[2])
			CheckError(err)
			currentWire.value = uint16(val)
			wires[parts[4]] = currentWire

		case strings.Contains(line, "RSHIFT"):
			currentWire.operation = "RSHIFT"
			currentWire.input1 = parts[0]
			val, err := strconv.Atoi(parts[2])
			CheckError(err)
			currentWire.value = uint16(val)
			wires[parts[4]] = currentWire

		default:
			currentWire.operation = ""
			val, err := strconv.Atoi(parts[0])
			if err != nil {
				// Value is another wire, use input
				currentWire.input1 = parts[0]
			} else {
				// Value is direct, use value
				currentWire.precalculated = true
				currentWire.value = uint16(val)
			}
			wires[parts[2]] = currentWire
		}

	}
	CheckError(scanner.Err())
	return wires
}

func main() {
	// Read in input file
	inputFile, err := os.Open(inputFilename)
	CheckError(err)
	defer func(inputFile *os.File) {
		CheckError(inputFile.Close())
	}(inputFile)

	// Create a hashmap to store wire information
	wires := processInput(inputFile)

	// Run part 1 calculation
	fmt.Printf("Part 2 wire signal for wire a: %d\n", calculateWireValue(wires, "a"))

	// Override wire b's value to wire a's value for part 2, and reset the rest
	part1a := wires["a"].value

	_, err = inputFile.Seek(0, 0)
	CheckError(err)
	wires = processInput(inputFile)

	b := wires["b"]
	b.value = part1a
	wires["b"] = b

	// Run part 2 calculation
	fmt.Printf("Part 2 wire signal for wire a: %d\n", calculateWireValue(wires, "a"))

}
