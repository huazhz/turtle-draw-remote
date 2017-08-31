<?php

// get_turtle_cmd_queue.php
// Ron Pulcer (c) 2016

// Take in a timestamp param (get only data past this point)
// Get a list of files from server data dir (*_commands.txt only)
// Also, only get files with modified time >= timestamp param
// Loop through each file and pick out only the most recent commands (as per timestamp)
// Accumlulate commands for multiple remote turtles
// Send back combined list in timestamp order
// Also include a header line (counts): Users: # and Commands: #

// Example request
// http://localhost/rmf/get_turtle_cmd_queue.php?cutoff_time=2016-07-15+17:30:15+EDT

// 2016 July: Initial development for use by Python drawing display app.


date_default_timezone_set("America/New_York");

$cutoff_time  = $_GET["cutoff_time"];
$cutoff_tmstamp = date_create($cutoff_time);
// echo "Query string param: $cutoff_time<br />";
// echo "Formatted date string of DateTime object: ".date_format($cutoff_tmstamp, "Y-m-d H:i:s T")."<br />";
// echo "<br /><br />";
// echo "Working directory: ".getcwd()."<br /><br />";

$dir = "./data";

$result_string = "";
$user_count = 0;
$cmd_count  = 0;

// Open a directory, and read its contents
if (is_dir($dir)){
  if ($dh = opendir($dir)){
    while (($file = readdir($dh)) !== false){

    	$filepath = $dir."/".$file;
      // echo "filename:" . $filepath . "<br>";

      $iscmdfile = strpos($filepath, "commands.txt");
      // echo "strpos() check for commands.txt: ";
      if ($iscmdfile == FALSE) {
      	// echo "Not a command file, so skipping ...<br /><br />";
      	continue;
      }

      $filemodtime_num = filemtime($filepath);
      // echo "filemtime(): $filemodtime_num<br />";
      $filemodtime_str = date("Y-m-d H:i:s T", $filemodtime_num);
      // echo "File time formatted: $filemodtime_str<br />";
      $file_tmstamp = date_create($filemodtime_str);
      // echo "Formatted date string of DateTime object: ".date_format($file_tmstamp, "Y-m-d H:i:s T")."<br />";

      if ($file_tmstamp > $cutoff_tmstamp) {

      	// echo "file timestamp GREATER THAN or EQUAL cutoff timestamp<br />";
      	// echo readfile($filepath);

        if ($fh = fopen($filepath, "r")) {
        	$user_count++;
        	// $line1 = TRUE;
 
      	  while(! feof($fh)) {
            $cmdline = utf8_decode(fgets($fh));
      	  	// if($line1) {
      	  		// // utf8_decode() still leaves behind an extra byte in front of command line, so just substring from 2nd char
      	  		// $cmdline = substr($cmdline, 1);
      	  		// $line1 = FALSE;
      	  	// }
            // 2016-MM-DD HH:MM:SS EDT: Date format 23 chars
            $cmdtime_str = substr($cmdline, 0, 23);
            // echo "cmdline time: $cmdtime_str<br />";
            if (strlen($cmdtime_str) > 0) {
              $cmd_tmstamp = date_create($cmdtime_str);
              if ($cmd_tmstamp > $cutoff_tmstamp) {
                // echo "$cmdline";
                $result_string .= $cmdline;
                $cmd_count++;
              }
            }
          }
          fclose($fh);
        }
      }

      // echo "<br /><br />";
    }
    closedir($dh);
  }
}

// Send results: Summary row + data
echo "Users: $user_count, Commands: $cmd_count\n";

if ($user_count == 1) {
  echo $result_string;
  // echo "No need to sort!";
}
elseif ($user_count > 1) {
  $cmd_array = explode("\n", $result_string);

  // Timestamp is first field, so this will sort commands by time (currently by user + time)
  sort($cmd_array, 2);

  $sz = sizeof($cmd_array);
  for($c=0; $c<$sz; $c++) {
  	if($cmd_array[$c] != "") {
      echo $cmd_array[$c]."\n";
    }
  }
}

?>