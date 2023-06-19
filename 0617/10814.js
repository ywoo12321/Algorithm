let fs = require("fs");
let input = fs.readFileSync("input.txt").toString().split("\r\n");

const peopleNumber = input.shift();
let personalInformation = [];
input.map((person) => {
  const [age, name] = person.split(" ");
  personalInformation.push({ name: name, age: Number(age) });
});

const comparePeople = (a, b) => {
  if (a.age !== b.age) {
    return a.age - b.age;
  } else {
    let x = a.name.toLowerCase();
    let y = b.name.toLowerCase();
    if (x < y) {
      return -1;
    }
    if (x > y) {
      return 1;
    }
  }
};

personalInformation.sort(comparePeople);

console.log(...personalInformation.name, ...personalInformation.age);
