<?php

require_once(dirname(__FILE__)."/util/db.php");

$queryCon = array(
    0=>array(
        "key"=>"time", 
        "value"=>"07-"
    ),
    1=>array(
        "key"=>"buyCount", 
        "value"=>"2"
    ),
    2=>array(
        "key"=>"title", 
        "value"=>"MILENSEA"
    ),
);

include(dirname(__FILE__)."/config/youzan.php");
db::connect();
$dataList = db::querySaleList($queryCon);
$count = count($dataList);
foreach ($dataList as $item) {
    print("流水：".$item["id"]."\t\t买家:".$item["buyer"]."\t\t时间:".$item["time"]."\t\t购买数量:".$item["buyCount"]."\t\t商品id:".$item["aliasId"]."\t\t售价:".$item["price"]."\t\t标题:".$item["title"]."</br>");
}
?>