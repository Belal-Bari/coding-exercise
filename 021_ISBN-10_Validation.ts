// ISBN-10 identifiers are ten digits long. The first nine characters are digits 0-9. The last digit can be 0-9 or X, to indicate a value of 10.

// An ISBN-10 number is valid if the sum of the digits multiplied by their position modulo 11 equals zero.

// For example:

// ISBN     : 1 1 1 2 2 2 3 3 3  9
// position : 1 2 3 4 5 6 7 8 9 10
// This is a valid ISBN, because:

// (1*1 + 1*2 + 1*3 + 2*4 + 2*5 + 2*6 + 3*7 + 3*8 + 3*9 + 9*10) % 11 = 0
// Examples
// 1112223339   -->  true
// 111222333    -->  false
// 1112223339X  -->  false
// 1234554321   -->  true
// 1234512345   -->  false
// 048665088X   -->  true
// X123456788   -->  false

// export function validISBN10(isbn: string): boolean {
//     const ary = isbn.split('');
//     let mod = 0;
//     if (isbn.length !== 10) return false; 
//     for (let n=0; n<ary.length; n += 1) {
//         if (n === ary.length - 1 && !/[0-9]/.test(ary[n]) || ary[n] !== 'X') return false 
//         //if (/[0-9]/.test(ary[n])) return false
//         if (!"0123456789".includes(ary[n])) {
//             console.log("ary", ary[n])
//             return false
//         }
//         if (n !== ary.length - 1) mod += (n+1) * parseInt(ary[n])
//         console.log(mod)
//     }
//     if (ary[ary.length - 1] !== 'X') mod += 10 * parseInt(ary[ary.length - 1])
//     console.log(mod % 11);
//     return mod % 11 === 0 ? true : false
//     //return isbn.length === 10 && isbn.split('').includes(/[0-9]/)
// }

export function validISBN10(isbn: string): boolean {
    if (isbn.length !== 10) return false
    let test = isbn.split('')
                .map((n, ind, ar) => ar.length - 1 !== ind ? /[0-9]/.test(n) : null)
                .includes(false);
    if(test || isbn[isbn.length-1] !== 'X' && !/[0-9]/.test(isbn[isbn.length - 1])) return false;
    return isbn.split('')
            .map((n, ind, ar) => /[0-9]/.test(n) ? parseInt(n) : 10)
            .reduce((acc, n, ind, ar) => acc += (ind+1) * n, 0) % 11 === 0
}

console.log(validISBN10("048665088X"));
