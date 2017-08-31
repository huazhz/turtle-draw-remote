<?php

// save_remote_py_turtle_cmd.php
// Ron Pulcer (c) 2016-2017

// Handles AJAX requests from Turtle Draw Remote Control web interface.
// Writes specified remote control command info to user's command text file
// (filename includes user first name and color).

// Originally developed for Rutland (VT) Mini Maker Faire (2016-07-30)
// 2016 June - July: Initial development of remote control interface.
// 2017-08-29: Added a verbose var to turn off detailed debug output, unless needed (default is false).


date_default_timezone_set("America/New_York");
$tmstamp = date_create();
$tmstamp_fmt = date_format($tmstamp, "Y-m-d H:i:s T");

// Set to true for more verbose debug output
$verbose = false;

$name  = $_GET["fn"];
$color = $_GET["clr"];
$cmd   = $_GET["cmd"];
$param = $_GET["prm"];
$speed = $_GET["spd"];
$step  = $_GET["stp"];
$pendown = $_GET["pen"];
$debug   = $_GET["dbg"];

// echo "Debug: $debug<br />";
if ($debug == "true" && $verbose) {
   echo "Echoing back your inputs:<br />";
   echo "Name: $name<br />";
   echo "Color: $color<br />";
   echo "Command: $cmd<br />";
   echo "Param: $param<br />";
   echo "Speed: $speed<br />";
   echo "Step: $step<br />";
   echo "Pen: $pendown<br />";
}

// In case the name is two words, remove embedded space for filename
$name4File = str_replace(" ", "", $name);
$colorHex = substr($color, 1);
$filename = "./data/" . $name4File . "_" . $colorHex . "_commands.txt";

if ($debug == "true" && $verbose) {
   if (file_exists($filename)) {
      echo "$filename exists<br />";
   }
   else {
      echo "$filename does NOT exist: Creating new file<br />";
   }
}

$dlm = "|";
$rec = $tmstamp_fmt . $dlm . $name . $dlm . $color . $dlm . $cmd . $dlm . $param . $dlm . $speed . $dlm . $step . $dlm . $pendown . "\n";

if ($debug == "true") {
   echo $rec;
}

$fileHandle = fopen($filename, "a");
fwrite($fileHandle, $rec);
fclose($fileHandle);

if ($debug == "true") {
   echo " - saved";
}

?>