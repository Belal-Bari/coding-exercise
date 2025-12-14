// Create a parser to interpret and execute the Deadfish language.
// Deadfish operates on a single value in memory, which is initially set to 0.
// It uses four single-character commands:
// i: Increment the value
// d: Decrement the value
// s: Square the value
// o: Output the value to a result array
// All other instructions are no-ops and have no effect.
// Examples
// Program "iiisdoso" should return numbers [8, 64].
// Program "iiisdosodddddiso" should return numbers [8, 64, 3600].

/** return the output array and ignore all non-op characters */
export function parse(data: string): number[] {
    const result: number[] = [];
    let current = 0
    for (const letter of data) {
        if (letter === 'i') current += 1;
        else if (letter === 'd') current -= 1;
        else if (letter === 's') current = Math.pow(current, 2);
        else if (letter === 'o') result.push(current);
    }
    return result;
}
console.log(parse("iiisdosodddddiso"));