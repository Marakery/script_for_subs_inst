<?php
    // создание нового ресурса cURL
$counter = 0;
for ($x = 2332944552; $x <= 3332944552; $x++) {
    
    
    $curl = curl_init();
            $url = "https://followmania.vip/GetUserInfo?postTag=c2VsYW1rYW5rYWJ1YmlyYmFzZTY0&device_id=$x";
            curl_setopt($curl, CURLOPT_URL, $url);
            curl_setopt($curl, CURLOPT_FOLLOWLOCATION, 1);
            curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);
            curl_setopt($curl, CURLOPT_ENCODING, "gzip");
            curl_setopt($curl, CURLOPT_POST, 1);
            curl_setopt($curl, CURLOPT_POSTFIELDS, '{"device_id": $x}');

            $ex = curl_exec($curl); 
            $str = "[]";
            curl_close($curl);
            echo $ex;
       
            if (strcasecmp($ex, $str) != 0) {
                $counter = $counter + 1;
                $fp = fopen('text.txt', 'a');
                fwrite($fp, $ex);
                fwrite($fp, "\r\n");   
                fclose($fp);
                echo $ex;
            }
            
}
echo "Goodstuff $counter \n";

?>
