//######################################################################
//######################################################################
//##    /$$$$$$$  /$$ /$$$$$$$$                              /$$      ##
//##   | $$__  $$|__/| $$_____/                             | $$      ##
//##   | $$  \ $$ /$$| $$     /$$$$$$   /$$$$$$   /$$$$$$$ /$$$$$$    ##
//##   | $$$$$$$ | $$| $$$$$ /$$__  $$ /$$__  $$ /$$_____/|_  $$_/    ##
//##   | $$__  $$| $$| $$__/| $$  \__/| $$  \ $$|  $$$$$$   | $$      ##
//##   | $$  \ $$| $$| $$   | $$      | $$  | $$ \____  $$  | $$ /$$  ##
//##   | $$$$$$$/| $$| $$   | $$      |  $$$$$$/ /$$$$$$$/  |  $$$$/  ##
//##   |_______/ |__/|__/   |__/       \______/ |_______/    \___/    ##
//######################################################################
//##########From JS: https://codepen.io/sumpiii8/pen/bGKwwGY############
//########################By: Varga Zsombor#############################
//######################################################################

let h;
let m;
let s;
let difference;
let startDifference;
let on = 0;
let startdifference;

function mp10() {
  startDifference = 10;
  on = 1;
}
function mp30() {
  startDifference = 30;
  on = 1;
}
function mp60() {
  startDifference = 60;
  on = 1;
}

function onoff() {
  startDifference = 0;
  on = 0;
}

function startTime() {
  const today = new Date();
  h = today.getHours();
  m = today.getMinutes();
  s = today.getSeconds();
  m = checkTime(m);
  s = checkTime(s);
  document.getElementById("current").innerHTML = h + ":" + m + ":" + s;

  if (on === 0) {
    document.getElementById("next").innerHTML = "OFF";
  } else {
    document.getElementById("next").innerHTML =
      Math.abs((s % startDifference) - startDifference) + "s";
  }

  setTimeout(startTime, 1000);
}

function checkTime(i) {
  if (i < 10)i = "0" + i;
  return i;
}