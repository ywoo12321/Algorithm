let fs = require("fs");
let input = fs.readFileSync("input.txt").toString().split("\n").map(Number);

const numberTime = input.shift();
const numberArray = new Array();

for (let i = 0; i < numberTime; i++) {
  numberArray.push(input[i]);
}
const compareNumber = (a, b) => {
  return a - b;
};

const sortedInput = numberArray.sort(compareNumber);

let answer = "";
for (let i = 0; i < sortedInput.length; i++) {
  answer += sortedInput[i] + "\n";
}
console.log(answer);
