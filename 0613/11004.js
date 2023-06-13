let fs = require("fs");
let input = fs.readFileSync("input.txt").toString().split("\n");

const [n, k] = input.shift().split(" ").map(Number);
const inputNumbers = input[0].split(" ").map(Number);
const numberArray = new Array();

for (let i = 0; i < inputNumbers.length; i++) {
  numberArray.push(inputNumbers[i]);
}

const sortedNumber = numberArray.sort((a, b) => {
  return a - b;
});

console.log(sortedNumber[k - 1]);
