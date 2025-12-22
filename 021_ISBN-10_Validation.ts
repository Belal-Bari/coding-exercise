export function validISBN10(isbn: string): boolean {
    const ary = isbn.split('');
    let mod = 0;
    if (isbn.length !== 10) return false; 
    for (let n=0; n<ary.length; n += 1) {
        if (n === ary.length - 1 && /[0-9]/.test(ary[n]) || ary[n] === 'X') return true 
        //if (/[0-9]/.test(ary[n])) return false
        if (!"0123456789".includes(ary[n])) {
            console.log("ary", ary[n])
            return false
        }
    }
    return true
    //return isbn.length === 10 && isbn.split('').includes(/[0-9]/)
}

console.log(validISBN10("1234512345"));
