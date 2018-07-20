<?php
/**
 * Created by PhpStorm.
 * User: AngryPotato
 * Date: 2018/7/20 0020
 * Time: 1:03
 */
require_once(dirname(dirname(__FILE__)) . "/util/db.php");
require_once(dirname(__FILE__) . "/baseShop.php");

class Youzan extends BaseShop
{
    public function __construct($db_config)
    {
        parent::__construct($db_config);
    }

    //所有的商品数据
    public function getAllMall()
    {
        return parent::query("SELECT * FROM `" . $this->db_param["table_mall"] . "`;");
    }
}

?>