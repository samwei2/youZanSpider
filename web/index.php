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
                var startYear = Number(startTime.substring(0, 4));
                var startMonth = Number(startTime.substring(5, 7));
                var startDay = Number(startTime.substring(8, 10));
                var startHours = Number(startTime.substring(11, 13));
                var startMinutes = Number(endTime.substring(14, 16));
                var endYear = Number(endTime.substring(0, 4));
                var endMonth = Number(endTime.substring(5, 7));
                var endDay = Number(endTime.substring(8, 10));
                var endHours = Number(endTime.substring(11, 13));
                var endMinutes = Number(endTime.substring(14, 16));
                
                if(Number(startYear+""+startMonth+""+startDay+""+startHours+""+startMinutes) > Number(endYear+""+endMonth+""+endDay+""+endHours+""+endMinutes))
                {
                    alert("开始时间不能晚于结束时间");
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
                    <input id="startTime" name="startTime" class="flatpickr" data-utc="true" data-enable-time="true" data-allow-input="true" />
                    <!--data-default-date="2016-03-01 03:30:00 -0300"-->
                    至
                    <input id="endTime" name="endTime" class="flatpickr" data-utc="true" data-enable-time="true" data-allow-input="true" />
                </div>
                <br>
                <div>
                    <label>【搜索关键词】</label>
                    <input id="searchStr" name="searchStr" value="春儿"/>
                </div>
                <br>
                <div>
                    <input type="submit" value="提交查询" onclick="return check(this.form)" />
                </div>
            </div>
        </form> 
        <script>
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