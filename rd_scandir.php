<?php
//$dir = "C:/wamp/www/rmf";
$dir = "C:/wamp/www/rmf/data";

// Sort in ascending order - this is default
$a = scandir($dir);

// Sort in descending order
$b = scandir($dir,1);

print_r($a);
echo "<br /><br />";

print_r($b);
echo "<br /><br />";


// Open a directory, and read its contents
if (is_dir($dir)){
  if ($dh = opendir($dir)){
    while (($file = readdir($dh)) !== false){
      echo "filename:" . $file . "<br>";
    }
    closedir($dh);
  }
}

?>