// Write a function that takes a string of braces, and determines if the order of the braces is valid. It should 
// return true if the string is valid, and false if it's invalid.
// This Kata is similar to the Valid Parentheses Kata, but introduces new characters: brackets [], and curly 
// braces {}. Thanks to @arnedag for the idea!
// All input strings will be nonempty, and will only consist of parentheses, brackets and curly braces: ()[]{}.
// What is considered Valid?
// A string of braces is considered valid if all braces are matched with the correct brace.
// Examples
// "(){}[]"   =>  True
// "([{}])"   =>  True
// "(}"       =>  False
// "[(])"     =>  False
// "[({})](]" =>  False     (40)41, {123}125, [91]93
// const br = ')'
// console.log(br.charCodeAt(0))
export function validBraces(braces: string): boolean {
    const left = [];
    for(const brace of braces) {
        if (braces.indexOf(brace) === 0) left.push(brace.charCodeAt(0) + 2);
        else if (['[','{','('].includes(brace)) left.push(brace.charCodeAt(0) + 2);
        else if ([']','}'].includes(brace)) {
            if (left[left.length - 1] === brace.charCodeAt(0)) left.pop();
            else return false;
        }
        else if ([')'].includes(brace)) {
            if (left[left.length - 1] === brace.charCodeAt(0) + 1) left.pop();
            else return false;
        }
        else return false
    }
    return left.length === 0;
}

console.log(validBraces('[('));