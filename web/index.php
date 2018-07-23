<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <link rel="stylesheet" type="text/css" href="./css/flatpickr.min.css"/>
        <script src="./js/flatpickr.min.js"></script>        
        <title></title>
        <script type="text/javascript">
            function check(form)
            {
                var startTime = form.startTime.value;
                var endTime = form.endTime.value;
                startTime = startTime.replace(/\s+|\-|\:/g, "");
                endTime = endTime.replace(/\s+|\-|\:/g, "");

                if(Number(startTime) > Number(endTime))
                {
                    alert("开始时间不能晚于结束时间");
                    return false;
                }

                var lowPrice = parseFloat(form.lowPrice.value);
                var highPrice = parseFloat(form.highPrice.value);
                if((lowPrice >= 0 && highPrice >= lowPrice) == false)
                {
                    alert("输入的价格不正确");
                    return false;
                }
                var lowNum = parseFloat(form.lowNum.value);
                var highNum = parseFloat(form.highNum.value);
                if((lowNum >= 0 && highNum >= lowNum) == false)
                {
                    alert("输入的销量不正确");
                    return false;
                }

                return true;
            }
        </script>
    </head>
    <body>
        <form id="searchForm" action="query.php" method="post" >
            <div>
                <div>
                    <label>【选择商城】</label>
                    <select id="shopName" name="shopName">
                        <option value="youzan">有赞</option>
                        <option value="chaping">差评</option>
                    </select>
                </div>
                <br>
                <div>
                    <label>【选择时间段】</label>
                    <br>
                    从
                    <input id="startTime" name="startTime" class="flatpickr" data-utc="true" data-enable-time="true" data-allow-input="true" data-default-date="2018-01-01 01:30" />
                    <!--data-default-date="2016-03-01 03:30:00 -0300"-->
                    至
                    <input id="endTime" name="endTime" class="flatpickr" data-utc="true" data-enable-time="true" data-allow-input="true" data-default-date="2018-12-01 01:30" />
                </div>
                <br>
                <div>
                    <label>【售价区间】</label>
                    <input id="lowPrice" name="lowPrice" value="0" />
                    -
                    <input id="highPrice" name="highPrice" value="1000" />
                </div>
                <br>
                <div>
                    <label>【销量】</label>
                    <input id="lowNum" name="lowNum" value="0" />
                    -
                    <input id="highNum" name="highNum" value="1000" />
                </div>
                <br>
                <div>
                    <label>【搜索关键词】</label>
                    <input id="searchStr" name="searchStr" value="测试"/>
                </div>
                <br>
                <div>
                    <label>【排序】</label>
                    <input type="radio" name="order" value="asc" checked="true">正序</input>
                    <input type="radio" name="order" value="desc">倒序</input>
                </div>
                <br>
                <div>
                    <input type="submit" value="提交查询" onclick="return check(this.form)" />
                </div>
            </div>
        </form> 
        <script type="text/javascript">
            document.getElementById("startTime").flatpickr();
            document.getElementById("endTime").flatpickr();

            var nowTime = new Date();
            var day = ("0" + nowTime.getDate()).slice(-2);
            var month = ("0" + (nowTime.getMonth() + 1)).slice(-2);
            
            var hours = ("0" + nowTime.getHours()).slice(-2);
            var minutes = ("0" + nowTime.getMinutes()).slice(-2);
            
            var today = nowTime.getFullYear() + "-" + (month) + "-" + (day) + " " + hours+":"+minutes;
            
            var startTxt = document.getElementById("startTime")
            var endTxt = document.getElementById("endTime")
            startTxt.value = today;
            endTxt.value = today;
        </script>
    </body>
</html>