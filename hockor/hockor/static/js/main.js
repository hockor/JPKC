/**
 * Created by Hockor on 15-3-23.
 */
$(function(){
    $(".tab_content").hide();
    $("ul.tabs li:first").addClass("active").show();
    $(".tab_content:first").show();

    $("ul.tabs li").click(function() {
        $("ul.tabs li").removeClass("active");
        $(this).addClass("active");
        $(".tab_content").hide();
        var activeTab = $(this).find("a").attr("href");
        $(activeTab).fadeIn();
        return false;
    });


    /*登录注册*/
    $(".login-it").click(function() {
        var username = $(".username").val(),
            userpass = $(".userpass").val();
        $.ajax({
            url:"",
            type: 'POST',
            contentType:"application/x-www-form-urlencoded;charset=UTF-8",
            data:{
                username : username,
                password : userpass
            },
            dataType: 'json',
            error: function(){
                alert('请重新登录！');
            },
            success:function(data){
                var message = data.message;
                if (message == "error"){
                    alert("用户名或密码错误!");
                }else if(message == 'ok'){

                }
            }
        });
    });

    $(".regester").click(function() {
        var reg_user = $(".reg-user").val(),
            reg_pass = $(".reg-pass").val(),
            reg_pass_agin = $(".reg-pass-agin").val(),
            reg_num = $(".reg-num").val(),
            reg_email = $(".reg-email").val();

        if(reg_pass === reg_pass_agin){
            $.ajax({
                url:"",
                type: 'POST',
                contentType:"application/x-www-form-urlencoded;charset=UTF-8",
                data:{

                    /*就上面那些数据*/
                    /*我日，为什么linux突然不能打拼音了*/
                },
                dataType: 'json',
                error: function(){
                    alert('注册失败！');
                },
                success:function(data){
                    var message = data.message;
                    if (message == "error"){
                        alert("注册失败!");
                    }else if(message == 'ok'){

                    }
                }
            });
        } else {
           alert("密码不一致！")
        }
    });

})
