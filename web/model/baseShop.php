<?php
/**
 * Created by PhpStorm.
 * User: Administrator
 * Date: 2018/7/20 0020
 * Time: 1:33
 */

require_once(dirname(dirname(__FILE__)) . "/util/db.php");

//商城数据接口基类
class BaseShop
{
    public function __construct($db_config)
    {
        $this->db_param = $db_config;
    }

    //查询接口
    public function query($sql)
    {
        return db::query($sql, $this->db_param);
    }
}