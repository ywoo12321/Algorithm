let fs = require("fs");
let [first, second, third] = fs.readFileSync("input.txt").toString().split(" ");

let price = 0;

let Numbers = new Set();
Numbers.add(first);
Numbers.add(second);
Numbers.add(third);

if (Numbers.size === 1) {
  price = 10000 + first * 1000;
  console.log(price);
} else if (Numbers.size === 2) {
  first === second
    ? (price = 1000 + first * 100)
    : (price = 1000 + third * 100);
  console.log(price);
} else if (Numbers.size === 3) {
  price = Math.max(first, second, third) * 100;
  console.log(price);
}
