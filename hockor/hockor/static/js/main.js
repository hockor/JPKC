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
        var username = $.trim($(".username").val()),
            userpass = $(".userpass").val();

        if(username && userpass){
            $.ajax({
                type: 'POST',
                dataType: 'json',
                contentType:"application/x-www-form-urlencoded;charset=UTF-8",
                url:"../login/",
                data:{
                    username : username,
                    password : userpass
                },
                error: function(){
                    alert('请重新登录！');
                },
                success:function(data){
                    var message = data.message;
                    if (message == "error"){
                        alert("用户名或密码错误!");
                    }else if(message == 'ok'){
                        $(".for-login").remove();
                        window.location.href = "/"
                    }
                }
            });
        } else {
            $(".login .error-tip").css("display","block");
        }
        
    });

    $(".regester").click(function() {
        var reg_user = $(".reg-user").val(),
            reg_pass = $(".reg-pass").val(),
            reg_pass_agin = $(".reg-pass-agin").val(),
            reg_num = $(".reg-num").val(),
            reg_email = $(".reg-email").val();

        if(reg_pass === reg_pass_agin && reg_user && reg_num && reg_email){
            $.ajax({
                type: 'POST',
                dataType: 'json',
                contentType:"application/x-www-form-urlencoded;charset=UTF-8",
                url:"../register/",
                data:{
                    username:reg_user,
                    password:reg_pass_agin,
                    email:reg_email,
                    number:reg_num
                    /*就上面那些数据*/
                    /*我日，为什么linux突然不能打拼音了*/
                },
                
                error: function(){
                    alert('注册失败！');
                },
                success:function(data){
                    var message = data.message;
                    if (message == "error1"){
                        alert("该用户名已注册!");
                    }else if (message == "error2"){
                        alert("该邮箱已注册");
                    }else if (message == "error3"){
                        alert("注册失败");
                    }else if(message == 'ok'){
                        alert("注册成功");
                    }
                }
            });
        } else {
           $(".reg .error-tip").css("display","block");
        }
    });


    
    

})
