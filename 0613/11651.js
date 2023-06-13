let fs = require("fs");
let input = fs.readFileSync("input.txt").toString().split("\n");

const time = Number(input.shift());
const numberArray = new Array();

for (let i = 0; i < time; i++) {
  let [x, y] = input[i].split(" ");
  numberArray.push([x, y]);
}

numberArray.map((numbers) => {
  numbers[0] = Number(numbers[0]);
  numbers[1] = Number(numbers[1].split("\r")[0]);
});

const compareCoordinate = (a, b) => {
  if (a[1] === b[1]) {
    return a[0] - b[0];
  } else if (a[1] !== b[1]) {
    return a[1] - b[1];
  }
};

numberArray.sort(compareCoordinate);

let answer = "";
for (let i = 0; i < numberArray.length; i++) {
  answer += numberArray[i][0] + " " + numberArray[i][1] + "\n";
}
console.log(answer);
