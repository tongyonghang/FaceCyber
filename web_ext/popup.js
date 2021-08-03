/*"default_popup": "popup.html"*/
$(function(){

    $('#keywordsubmit').click(function(){
		var username = $('#username').val();
        var password = $('#password').val();
				
		if (username && password){
                chrome.runtime.sendMessage(
					{Ext_username: username,
                     Ext_password: password},
					function(response) {
						result = response.farewell;
                        if (result.raw == 'Invalid'){
                            alert('Invalid credientials');
                        }
                        else if (result.raw == 'Failed'){
                            alert('Password is not correct');
                        }
                        else if (result.raw == 'Successful'){
                            alert("login success");
                            $('body').css('height','300px');
                            $('.main_page').css('visibility','visible');
                            $('.form_group').css('visibility','hidden');
                            $('h4.ext_username').html(result.Username);
                            console.log("testing",result.Fb_name);
                            if (result.Fb_name === '' ){
                                $('p.ext_fb_name').html("[Empty]");
                            }
                            else{
                                $('p.ext_fb_name').html(result.Fb_name);
                            }
                            //$('p.ext_fb_name').html(result.Fb_name);
                            $('p.ext_score').html(result.bully_score+"%");
                            var rank = result.friend_rank;
                            //console.log(rank[0]['friend']);
                            if (rank.length == 0){
                                x = "<center><table style='text-align:center;'><tr><th>No.</th><th>Name</th><th>Bully Score</th></tr>";
                                x = x +"<tr><td>1</td></tr>"; 
                                x = x +"<tr><td>2</td></tr>"; 
                                x = x +"<tr><td>3</td></tr>"; 
                                x = x + "</table></center>";
                                $('p.ext_rank').html(x);
                            }
                            else{
                                var x="",i,rank_scale;
                                var j=1;
                                rank_scale = rank.length;
                                if (rank_scale > 3){
                                    rank_scale = 2;
                                }
                                x = "<center><table style='text-align:center;'><tr><th>No.</th><th>Name</th><th>Bully Score</th></tr>";
                                x = x +"<tr><td>1</td>" + "<td>"+ rank[0]['friend']+"</td>" +"<td>"+rank[0]['bully_score']+"%</td></tr>"; 
                                x = x +"<tr><td>2</td>" + "<td>"+ rank[1]['friend']+"</td>" +"<td>"+rank[1]['bully_score']+"%</td></tr>"; 
                                x = x +"<tr><td>3</td>" + "<td>"+ rank[2]['friend']+"</td>" +"<td>"+rank[2]['bully_score']+"%</td></tr>"; 
                                x = x + "</table></center>";
                                $('p.ext_rank').html(x);
                            }
                            chrome.storage.sync.set({name: username}, function() {
                                console.log('Value is set to ' + username);
                              });
                            chrome.storage.sync.set({pass: password}, function() {
                                console.log('Value is set to ' + password);
                              });
                              
                            /*localStorage.setItem("name", username);
                            localStorage.setItem("password", password);
                            console.log(localStorage.getItem("name"));
                            console.log(localStorage.getItem("password"));*/
                        }
					});
		}
        else{
            alert("Your Username or Password is empty");
        }
		$('#username').val('');
        $('#password').val('');
    });
    $('#keylogout').click(function(){
        alert("You are logged out");
        chrome.storage.sync.remove('name');
        chrome.storage.sync.remove('pass'); //remove cache
        $('body').css('height','100px');
        $('.main_page').css('visibility','hidden');
        $('.form_group').css('visibility','visible');
    });
});

