let fs = require("fs");
let input = fs.readFileSync("input.txt").toString().split(" ").map(Number);

const compareNumber = (a, b) => {
  return a - b;
};

const sortedInput = input.sort(compareNumber);

console.log(...sortedInput);
