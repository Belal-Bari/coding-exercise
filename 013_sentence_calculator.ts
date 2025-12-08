// Calculate the total score (sum of the individual character scores) of a sentence given the following score rules for each allowed group of characters:

// Lower case [a-z]: 'a'=1, 'b'=2, 'c'=3, ..., 'z'=26
// Upper case [A-Z]: 'A'=2, 'B'=4, 'C'=6, ..., 'Z'=52
// Digits [0-9] their numeric value: '0'=0, '1'=1, '2'=2, ..., '9'=9
// Other characters: 0 value
// Note: input will always be a string
function lettersToNumbers(s: string): number {
  let num = 0
  for (const letter of s) {
    //console.log("Letter: ", letter.charCodeAt(0));
    if (letter.charCodeAt(0) >=65 && letter.charCodeAt(0) <= 90) {
        num = num + ((letter.charCodeAt(0) - 65 + 1) * 2);
        //console.log(num);
    } 
    else if (letter.charCodeAt(0) >=97 && letter.charCodeAt(0) <= 122) {
        num = num + (letter.charCodeAt(0) - 97 + 1);
    }
    else if (letter.charCodeAt(0) >=48 && letter.charCodeAt(0) <= 57) {
        num = num + (letter.charCodeAt(0) - 48);
    }
  }
  return num
}

console.log(lettersToNumbers('AC1 5'));