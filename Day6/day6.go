package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

// CheckError is a helper function to CheckError for errors more conveniently. From https://gobyexample.com/reading-files
func CheckError(e error) {
	if e != nil {
		panic(e)
	}
}

func toggleLights(lights map[int]map[int]int, startX int, startY int, endX int, endY int, action string) {
	for x := startX; x <= endX; x++ {
		if lights[x] == nil {
			lights[x] = make(map[int]int)
		}
		for y := startY; y <= endY; y++ {
			switch action {
			case "on":
				lights[x][y] = 1
			case "off":
				lights[x][y] = 0
			case "toggle":
				switch lights[x][y] {
				case 0:
					lights[x][y] = 1
				case 1:
					lights[x][y] = 0
				}
			}
		}
	}
}

func adjustLights(lights map[int]map[int]int, startX int, startY int, endX int, endY int, action string) {
	for x := startX; x <= endX; x++ {
		if lights[x] == nil {
			lights[x] = make(map[int]int)
		}
		for y := startY; y <= endY; y++ {
			switch action {
			case "on":
				lights[x][y] += 1
			case "off":
				if lights[x][y] != 0 {
					lights[x][y] -= 1
				}
			case "toggle":
				lights[x][y] += 2
			}
		}
	}
}

func processInput(inputFile *os.File, mode string) int {
	// Create 2D hashmap to store light state values
	lights := make(map[int]map[int]int)

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
		CheckError(err1)
		y1, err2 := strconv.Atoi(strings.Split(parts[startIndex], ",")[1])
		CheckError(err2)
		x2, err3 := strconv.Atoi(strings.Split(parts[startIndex+2], ",")[0])
		CheckError(err3)
		y2, err4 := strconv.Atoi(strings.Split(parts[startIndex+2], ",")[1])
		CheckError(err4)

		// Make sure the coordinates are in the right order
		if x2 < x1 {
			x1, x2 = x2, x1
		}
		if y2 < y1 {
			y1, y2 = y2, y1
		}

		// Modify the lights in the map
		switch mode {
		case "part1":
			toggleLights(lights, x1, y1, x2, y2, parts[startIndex-1])
		case "part2":
			adjustLights(lights, x1, y1, x2, y2, parts[startIndex-1])
		}

	}
	CheckError(scanner.Err())

	// Calculate answer by looping through keys and tallying lights
	lightsOn := 0
	for _, yMap := range lights {
		for _, lightState := range yMap {
			lightsOn += lightState
		}
	}
	return lightsOn
}

func main() {
	// Read in input file
	const inputFilename string = "input.txt"
	inputFile, err := os.Open(inputFilename)
	CheckError(err)
	defer func(inputFile *os.File) {
		CheckError(inputFile.Close())
	}(inputFile)

	// Run calculations and output the answers
	fmt.Printf("Number of lights on for part 1: %d\n", processInput(inputFile, "part1"))
	_, err = inputFile.Seek(0, 0)
	CheckError(err)
	fmt.Printf("Total light brightness for part 2: %d\n", processInput(inputFile, "part2"))
}
