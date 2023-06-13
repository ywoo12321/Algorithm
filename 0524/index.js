let fs = require("fs");
let [nowTime, needTime] = fs.readFileSync("index.txt").toString().split(" ");
let [inputHour, inputMinute] = nowTime.split(" ");

let nowHour = Number(inputHour);
let nowMinute = Number(inputMinute);
let cookingTime = Number(needTime);

function WhenFinish(nowHour, nowMinute, cookingTime) {
  let cookingMinute, cookingHour;
  cookingHour = 0;
  cookingMinute = cookingTime;
  if (cookingTime >= 60) {
    cookingHour = parseInt(cookingTime / 60);
    cookingMinute = cookingTime % 60;
  }
  let finishMinute = nowMinute + cookingMinute;
  let finishHour = nowHour + cookingHour;

  if (finishMinute > 59) {
    finishHour += 1;
    finishMinute = finishMinute - 60;
  }
  if (finishHour >= 24) {
    finishHour = finishHour - 24;
  }
  console.log(finishHour, finishMinute);
}

WhenFinish(nowHour, nowMinute, cookingTime);
