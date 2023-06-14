let fs = require("fs");
let input = fs.readFileSync("input.txt").toString().split("\n");

const numberTime = Number(input.shift());
const numberArray = input[0].split(" ").map(Number);

const coordinateDictionary = {};

const NoDuplicationArray = [...new Set(numberArray)];

NoDuplicationArray.sort((a, b) => {
  return a - b;
});

NoDuplicationArray.map((number, index) => {
  coordinateDictionary[number] = index;
});

let answer = "";
numberArray.map((number) => {
  number = coordinateDictionary[number];
  answer += number + " ";
});

console.log(answer);
//사전형을 쓰면 될거 같다
/*
    정렬 시키고 set 으로 넣어놓는다 

   -10 -9 2 4

   자기 인덱스 위치를 찾고 총 크기에서 인덱스 위치를 뺀다.
   그값을 value에 저장하고 키를 넣어 answer에 value를 출력한다.


*/
