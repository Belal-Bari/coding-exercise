// A pangram is a sentence that contains every single letter of the alphabet at least once. For example, 
// the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z 
// at least once (case is irrelevant).

// Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers 
// and punctuation.
export const isPangram = (phrase: string): boolean => {
    const letters: string[] = [];
    const regex = /^[a-z]+$/i;
    for (const str of phrase) {
        if (!letters.includes(str.toLowerCase()) && regex.test(str)) letters.push(str.toLowerCase());
    }
    return letters.length === 26
}
console.log(isPangram("This is not a pangram."))