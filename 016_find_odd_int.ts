// Given an array of integers, find the one that appears an 
// odd number of times.
// There will always be only one integer that appears an odd 
// number of times.

// Examples
// [7] should return 7, because it occurs 1 time (which is odd).
// [0] should return 0, because it occurs 1 time (which is odd).
// [1,1,2] should return 2, because it occurs 1 time (which is odd).
// [0,1,0,1,0] should return 0, because it occurs 3 times 
// (which is odd).
// [1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it 
// appears 1 time
// let a = Math.floor(5/2);
// console.log(a);
export const findOdd = (xs: number[]): number => {
  const unique: number[] = [];
  for(let i=0; i<xs.length; i = i + 1) {
    if(!unique.includes(xs[i])) unique.push(xs[i]);
  }
  for (let i=0; i < unique.length; i += 1) {
    let tmp = 0;
    for (let j=0; j < xs.length; j += 1) {
        if (unique[i] === xs[j]) tmp += 1;
    }
    if (tmp % 2 !== 0) return unique[i];
  }
  return 0;
};

console.log(findOdd([1,2,2,3,3,3,4,3,3,3,2,2,1]));