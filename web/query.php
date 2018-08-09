<?php

/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

function createSql($startTime, $endTime, $lowPrice, $highPrice, $lowNum, $highNum, $searchStr, $order)
{
    $a = getCutYearTime($startTime);
    $b = getCutYearTime($endTime);
    $sql = "SELECT * FROM `" . DB_TABLE_MALL . "`";
    $sql = $sql . " where";
    $sql = $sql . " (`title` like \"%$searchStr%\")";
    $sql = $sql . " and";
    $sql = $sql . " (`price` > $lowPrice and `price` < $highPrice)";
    $sql = $sql . " and";
    $sql = $sql . " (`buyCount` > $lowNum and `buyCount` < $highNum)";
    $sql = $sql . " and";
    $sql = $sql . " ((`time` between '".$a."' and '".$b."')"." or "."(`time` between '".$startTime."' and '".$endTime."'))";
    $sql .= " order by '$order';";
    return $sql;
}

function printResult($queryResult, $hasData)
{
    echo("<table border='true'>");
    echo("<tr>");
    echo("<td>自增流水id</td>");
    echo("<td>买家</td>");
    echo("<td>购买时间</td>");
    echo("<td>购买数量</td>");
    echo("<td>商品id</td>");
    echo("<td>价格</td>");
    echo("<td>商品名</td>");
    echo("</tr>");
    while ($row = mysqli_fetch_assoc($queryResult)) {
        echo("<tr>");
        echo("<td>".$row["id"]."</td>");
        echo("<td>".$row["buyer"]."</td>");
        echo("<td>".$row["time"]."</td>");
        echo("<td>".$row["buyCount"]."</td>");
        echo("<td>".$row["aliasId"]."</td>");
        echo("<td>".$row["price"]."</td>");
        echo("<td>".$row["title"]."</td>");
        echo("</tr>");
        $hasData = true;
    }
    echo("</table>");
    return $hasData;
}
function getCutYearTime($inputTime)
{
    return substr($inputTime,5);
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

    $con = mysqli_connect(DB_HOST, DB_USER, DB_PASS, DB_NAME, DB_PORT);
    if (mysqli_error($con)) {
        $message = sprintf("Database Connect failed:%s\r\n", mysqli_connect_error());
        echo($message."<br>");
        exit();
    }else
    {
        printf('sql connect.........,%s,%s,%s,%s,%s,%s,%s,%s',$startTime, $endTime, $lowPrice, $highPrice, $lowNum, $highNum, $searchStr, $order);
    }
    mysqli_set_charset($con,DB_CHARSET);

    $sql = createSql($startTime, $endTime, $lowPrice, $highPrice, $lowNum, $highNum, $searchStr, $order);
    $queryResult = mysqli_query($con, $sql);
    if (mysqli_error($con)) {
        $message = sprintf("SQL Query Error:%s\r\n", $con->error);
        echo($message . "<br>");
        exit();
    }
    $hasData = false;
    $hasData = printResult($queryResult, $hasData);
    // 释放结果集
    mysqli_free_result($queryResult);
    mysqli_close($con);
    if ($hasData == false) {
        echo "
              <script type='text/javascript'>
                alert('没有找到符合当前搜索条件的数据!!!');
//                top.location='index.php';
              </script>";
    }
}

main();
