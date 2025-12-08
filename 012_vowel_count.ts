// Return the number (count) of vowels in the given string.
// We will consider a, e, i, o, u as vowels for this Kata (but not y).
// The input string will only consist of lower case letters and/or spaces.
// Running the code: npx ts-node .\
export class Kata {
  static getCount(str: string): number {
    let num = 0;
    for(const letter of str) {  
        if (['a','e','i','o','u'].includes(letter)) num += 1;
    }
    return num
  }
}

console.log(Kata.getCount('whats up'))