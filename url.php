<?php
    // создание нового ресурса cURL
    // 9479926142 , 10702006028 , 
    $x = 0;
        do {


        $i = 0;
        do {
            echo "Out:  ";
            $curl = curl_init();
                    $id = (string)11308009154;
                    $url = "https://followmania.vip/Send?postTag=c2VsYW1rYW5rYWJ1YmlyYmFzZTY0&device_id=$id";
                    curl_setopt($curl, CURLOPT_URL, $url);
                    curl_setopt($curl, CURLOPT_FOLLOWLOCATION, 1);
                    curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);
                    curl_setopt($curl, CURLOPT_ENCODING, "gzip");
                    curl_setopt($curl, CURLOPT_POST, 1);
                    curl_setopt($curl, CURLOPT_POSTFIELDS, '{"device_id": 11308009154, "username":"uraestheticgirls", "type":"followers","followers_count":"20","credi_count":"2"}');
            $curl2 = curl_init();
                    curl_setopt($curl2, CURLOPT_URL,"https://followmania.vip/GetUserInfo?postTag=c2VsYW1rYW5rYWJ1YmlyYmFzZTY0&device_id=$id");
                    $ef = curl_exec($curl2);
                    $ex = curl_exec($curl); 
                    curl_close($curl);
                    curl_close($curl2);
                    echo $ex;
                    echo $ef;
                    echo "\n";
                    sleep(10); 
                    $i = $i + 1;    
        } while ($i <= 25);
        
        echo "sleep \n";
        sleep(1800);
        $i = 0;  
        $x = $x + 1;
    } while ($x <= 50);
?>
