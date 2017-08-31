
// JavaScript for Turtle Draw Remote Control web app
// Ron Pulcer (c) 2016
// Originally developed for Rutland (VT) Mini Maker Faire (2016-07-30)
// 2016 June - July: Initial development
// 2016-08-30: Added message function for use with CCV Website Development course

var fname = "";
var dir = "";
var prevDir = "";
var turn = true;
var ctrlList = "clear_display,speed,step,pen_down,dir_north,dir_south,dir_east,dir_west" + 
",dir_northwest,dir_northeast,dir_southwest,dir_southeast,dir_center" + 
",spin_left,spin_times,spin_right,hop_up,bounce_times,dip_down" + 
",shake_horiz,shake_both,shake_vert" + 
",circle,triangle,square,pentagon,fill_color,hexagon,septagon,octagon,nonagon";
var turtleColor = "";

function pageLoad() {
  document.getElementById("fname").value = "";
  stopRemote();
}

function startRemote() {
  fname = document.getElementById("fname").value;
  if (fname != null) {
    fname = fname.trim();
    if(fname == "") {
      alert("Please enter first name before starting Py Turtle Remote Control.");
      return;
    }
  }
  disableControls(false);
  document.getElementById("fname").disabled = true;
  document.getElementById("start_remote").disabled = true;
  document.getElementById("stop_remote").disabled = false;
  var cmdDiv = document.getElementById("commands");
  if(cmdDiv != null) {
    cmdDiv.innerHTML = "";
  }
  chooseColor();
}

function stopRemote() {
  document.getElementById("fname").disabled = false;
  document.getElementById("start_remote").disabled = false;
  document.getElementById("stop_remote").disabled = true;

  // When called from pageLoad(), the name is blank, so don't write out Stop command
  var fname = document.getElementById("fname").value;
  if(fname != "") {
    writeCommand("stop", "");
  }
  disableControls(true);
}

function disableControls(disBool) {
  var controls = ctrlList.split(",");
  for(var c = 0; c<controls.length; c++) {
    var ctrl = document.getElementById(controls[c]);
    if (ctrl != null) { ctrl.disabled = disBool; }
  }
}

function writeCommand(cmd, param) {
  var speed   = document.getElementById("speed").value;
  var step    = document.getElementById("step").value;
  var pendown = document.getElementById("pen_down").checked;
  var debug   = document.getElementById("debug_mode").checked;
  var cmdDiv  = document.getElementById("commands");

  var newCmd = fname + "," + turtleColor + "," + cmd + "," + param + "," + speed + "," + step + "," + pendown + "<br />";
  if(cmdDiv != null) {
    cmdDiv.innerHTML += "Send: " + newCmd;
  }
  var reqURL = "./save_remote_py_turtle_cmd.php?" +
    "fn="   + encodeURIComponent(fname) +
    "&clr=" + encodeURIComponent(turtleColor) +
    "&cmd=" + cmd +
    "&prm=" + encodeURIComponent(param) +
    "&spd=" + speed +
    "&stp=" + step +
    "&pen=" + pendown +
    "&dbg=" + debug;
  // alert(reqURL);
   saveCmd(reqURL);
}

function saveCmd(url) {
  var xmlhttp = getAJAXRequest();
  xmlhttp.onreadystatechange = function() {
    if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
      document.getElementById("commands").innerHTML += "Recv: " + xmlhttp.responseText + "<br />";
      // alert("enabling...");
      disableControls(false);
    }
  };
  // xmlhttp.open("GET", "./save_cmd_result.txt", true);
  xmlhttp.open("GET", url, true);
  disableControls(true);

  xmlhttp.send();
}

function getAJAXRequest() {
  if (window.XMLHttpRequest) {
    // alert("XMLHttpRequest");
    return new XMLHttpRequest();
  }
  else {
    // code for IE6, IE5
    // alert("ActiveXObject");
    return new ActiveXObject("Microsoft.XMLHTTP");
  }
}

function chooseColor() {
  var r = Math.floor(Math.random() * 256);
  var g = Math.floor(Math.random() * 256);
  var b = Math.floor(Math.random() * 256);
  // alert("r = " + r + "\ng = " + g + "\nb = " + b);
  var rgbColor = "rgb(" + r + "," + g + "," + b + ")";
  // alert(rgbColor);

  var rHex = dec2Hex(r);
  var gHex = dec2Hex(g);
  var bHex = dec2Hex(b);
  var rgbHex = "#" + rHex + gHex + bHex;
  // alert(rgbHex);

  var txtTSwatch = document.getElementById("turtle_swatch");

  if (txtTSwatch != null) {
    txtTSwatch.style.backgroundColor = rgbColor;
  }

  turtleColor = rgbHex;
}

function dec2Hex(decVal) {
  // Convert decimal value (0-255) into 2-digit Hex value
  var twosComp = decVal;

  // Note: Since numbers above 127 can be interpreted as negative (left-most bit is 1),
  // convert to Two's Complement if necessary (flip bits and add 1), before converting to Hex.
  if (decVal < 0) { twosComp = 0xFFFFFFFF + decVal + 1; }

  var hexVal = twosComp.toString(16).toUpperCase();

  if(hexVal.length == 1) { hexVal = "0" + hexVal; }

  return hexVal;
}

function clearDisplay() {
  writeCommand("clear", "");
}

function direction(dir) {
  turn = false;
  if(dir != prevDir) { turn = true; }
  // alert("Going " + dir + ", turn = " + turn);
  prevDir = dir;
  writeCommand(dir, turn);
}

function centerXY() {
  prevDir = "center";
  writeCommand("center", "");
}

function spinLeft() {
  var times = 0;
  var num = document.getElementById("spin_times");
  if (num != null) { times = num.value; }
  // alert("Spin Left: " + times + " times");
  writeCommand("spinleft", times);
}

function spinRight() {
  var times = 0;
  var num = document.getElementById("spin_times");
  if (num != null) { times = num.value; }
  // alert("Spin Right: " + times + " times");
  writeCommand("spinright", times);
}

function shakeHoriz() {
  writeCommand("shakehoriz", "");
}

function shakeVert() {
  writeCommand("shakevert", "");
}

function shakeBoth() {
  writeCommand("shakeboth", "");
}

function hop() {
  var times = 0;
  var bounce = document.getElementById("bounce_times");
  if (bounce != null) { times = bounce.value; }
  // alert("Hop: " + times + " times");
  writeCommand("hop", times);
}

function dip() {
  var times = 0;
  var bounce = document.getElementById("bounce_times");
  if (bounce != null) { times = bounce.value; }
  // alert("Dip: " + times + " times");
  writeCommand("dip", times);
}

function makeShape(shape) {
  var fill = false;
  var fillColor = document.getElementById("fill_color");
  if (fillColor != null) { fill = fillColor.checked; }
  writeCommand(shape, fill);
}

function sendMessage() {
  var msg = document.getElementById("message");
  if (msg != null) {
    writeCommand("message", msg.value);
  }
}

function display_instructions() {
    alert("Instructions for Remote Control Turtle Drawing and Animation\n\n" +
          "1. Enter your first name.\n" +
          "2. Press Start button.  A random color will be selected for your remote Turtle.\n" +
          "3. If you don't like your assigned color: Press Stop, then Start to get another Turtle color.\n" +
          "4. Enter 'remote control' buttons to animate or draw with your remote Turtle.\n" +
          "5. After pressing first command button, you should see your remote Turtle appear on remote screen, and write your first name.\n" +
          "6. Please press Stop button when you are finished to see Turtle message!\n\n");
}
