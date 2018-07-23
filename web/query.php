<?php

/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

require_once(dirname(__FILE__) . "/util/db.php");

function createSql($startTime, $endTime, $lowPrice, $highPrice, $lowNum, $highNum, $searchStr, $order)
{
    $sql = "SELECT * FROM `" . DB_TABLE_MALL . "`";
    $sql .= " where (`title` like '%$searchStr%')";
    $sql .= " and (`price` > $lowPrice and `price` < $highPrice)";
    $sql .= " and (`buyCount` > $lowNum and `buyCount` < $highNum)";
    $sql .= " and (`time` between '$startTime' and '$endTime')";
    $sql .= " order by '$order';";
    return $sql;
}

function main()
{

    $shopName = $_REQUEST['shopName'];
    $startTime = $_REQUEST['startTime'];
    $endTime = $_REQUEST['endTime'];
    $lowPrice = $_REQUEST['lowPrice'];
    $highPrice = $_REQUEST['highPrice'];
    $lowNum = $_REQUEST['lowNum'];
    $highNum = $_REQUEST['highNum'];
    $searchStr = $_REQUEST['searchStr'];
    $order = $_REQUEST['order'];

    include(dirname(__FILE__) . "/config/$shopName.php");

    $sql = createSql($startTime, $endTime, $lowPrice, $highPrice, $lowNum, $highNum, $searchStr, $order);
    db::connect();
    $queryResult = db::query($sql);
    $dataList = db::fetch_all("id", true);
    if ($dataList != false) {
        $count = count($dataList);
        if ($count < 1) {
            echo "
                    <script type='text/javascript'>
                        alert('没有找到符合当前搜索条件的数据');
                        top.location='index.php';
                    </script>";
        }
        foreach ($dataList as $item) {
            print("流水：" . $item["id"] . "\t\t买家:" . $item["buyer"] . "\t\t时间:" . $item["time"] . "\t\t购买数量:" . $item["buyCount"] . "\t\t商品id:" . $item["aliasId"] . "\t\t售价:" . $item["price"] . "\t\t标题:" . $item["title"] . "</br>");
        }
    } else {
        echo "
              <script type='text/javascript'>
                alert('没有找到符合当前搜索条件的数据!!!');
                top.location='index.php';
              </script>";
    }
}

main();
