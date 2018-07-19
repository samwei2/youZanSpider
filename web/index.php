<?php
require_once("/model/youzan.php");


$youzanConfig = [];
$youzanConfig["host"] = "127.0.0.1";
$youzanConfig["port"] = 3306;
$youzanConfig["name"] = "alias";
$youzanConfig["user"] = "root";
$youzanConfig["pass"] = "root";
$youzanConfig["table_mall"] = "aliasinfo";
$youzanConfig["charset"] = "utf-8";

$shop = new Youzan($youzanConfig);
$queryResult = $shop->getAllMall();
//此处的数量不正确
$count = count($queryResult);
print(">>>>>>>>>>查询到的总数量为：".$count."\n");
var_dump($queryResult);
foreach ($queryResult as $item) {
    print("流水：".$item["id"]." 买家:".$item["buyer"]." 时间:".$item["time"]." \n");
}
?>