package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

// Helper function to check for errors more conveniently. From https://gobyexample.com/reading-files
func check(e error) {
	if e != nil {
		panic(e)
	}
}

func toggleLights(lights map[int]map[int]bool, startX int, startY int, endX int, endY int, action string) {
	for x := startX; x <= endX; x++ {
		if lights[x] == nil {
			lights[x] = make(map[int]bool)
		}
		for y := startY; y <= endY; y++ {
			switch action {
			case "on":
				lights[x][y] = true
			case "off":
				lights[x][y] = false
			case "toggle":
				lights[x][y] = !lights[x][y]
			}
		}
	}
}

func main() {
	// Create 2D hashmap to store light state values
	lights := make(map[int]map[int]bool)

	// Read in input file
	const inputFilename string = "input.txt"
	inputFile, err := os.Open(inputFilename)
	check(err)
	defer func(inputFile *os.File) {
		check(inputFile.Close())
	}(inputFile)

	// Loop over each line in input file and process by adding data to hashmap
	scanner := bufio.NewScanner(inputFile)
	for scanner.Scan() {
		// Grab the line
		line := scanner.Text()

		// Split string into necessary parts
		parts := strings.Split(line, " ")

		// Set up indexes to locate parts of the line based on the command's action
		var startIndex int
		switch parts[0] {
		case "turn":
			startIndex = 2
		case "toggle":
			startIndex = 1
		}

		// Locate coordinates in the line
		x1, err1 := strconv.Atoi(strings.Split(parts[startIndex], ",")[0])
		check(err1)
		y1, err2 := strconv.Atoi(strings.Split(parts[startIndex], ",")[1])
		check(err2)
		x2, err3 := strconv.Atoi(strings.Split(parts[startIndex+2], ",")[0])
		check(err3)
		y2, err4 := strconv.Atoi(strings.Split(parts[startIndex+2], ",")[1])
		check(err4)

		// Make sure the coordinates are in the right order
		if x2 < x1 {
			x1, x2 = x2, x1
		}
		if y2 < y1 {
			y1, y2 = y2, y1
		}

		// Toggle the lights in the map
		toggleLights(lights, x1, y1, x2, y2, parts[startIndex-1])
	}
	check(scanner.Err())

	// Calculate answer by looping through keys and tallying lights
	lightsOn := 0
	for _, yMap := range lights {
		for _, lightState := range yMap {
			if lightState {
				lightsOn++
			}
		}
	}

	// Output the answer
	fmt.Printf("Number of lights on: %d\n", lightsOn)
}
