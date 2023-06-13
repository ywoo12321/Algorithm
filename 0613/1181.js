let fs = require("fs");
let input = fs.readFileSync("input.txt").toString().split("\n");

const time = Number(input.shift());
const letterSet = new Set();

for (let i = 0; i < time; i++) {
  let letter = input[i].split("\r");
  letterSet.add(letter[0]);
}
const letterArray = [...letterSet];

const compareLetter = (a, b) => {
  if (a.length !== b.length) {
    return a.length - b.length;
  } else return a > b ? 1 : -1;
};

letterArray.sort(compareLetter);

let answer = "";

for (let i = 0; i < letterArray.length; i++) {
  answer += letterArray[i] + "\n";
}
console.log(answer);
