<?php

/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

require_once(dirname(__FILE__)."/util/db.php");

$shopName = "youzan";
$startTime = "2018-07-17 03:20";
$endTime = "2018-07-17 03:20";
$searchStr = "test";


//构造查询条件
function createQueryParam()
{    
    $queryCon = array(
        0=>array(
            "key"=>"startTime", 
            "value"=>$startTime
        ),
        1=>array(
            "key"=>"endTime", 
            "value"=>$endTime
        ),
        2=>array(
            "key"=>"title", 
            "value"=>$searchStr
        ),
        3=>array(
            "key"=>"buyCount",
            "value"=>$buyCount
        ),
        4=>array(
            "key"=>"price",
            "value"=>$price
        ),
        5=>array(
            "key"=>"order",
            "value"=>$order
        )
    );
    return $queryCon;
}

function main()
{
    
    $shopName = $_REQUEST['shopName'];
    $startTime = $_REQUEST['startTime'];
    $endTime = $_REQUEST['endTime'];
    $searchStr = $_REQUEST['searchStr'];
    $buyCount = null;
    $price = null;
    $order = "asc";
    
    include(dirname(__FILE__)."/config/$shopName.php");
    
    $queryCon = createQueryParam();
    
    //////////////////////////////
    //数据库时间改字段类型
    db::connect();
    $dataList = db::querySaleList($queryCon);
    $count = count($dataList);
    foreach ($dataList as $item) {
        print("流水：".$item["id"]."\t\t买家:".$item["buyer"]."\t\t时间:".$item["time"]."\t\t购买数量:".$item["buyCount"]."\t\t商品id:".$item["aliasId"]."\t\t售价:".$item["price"]."\t\t标题:".$item["title"]."</br>");
    }
}

main();
