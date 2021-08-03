$(function() {

	chrome.storage.sync.get(['name','pass'], function(result) {
        if(typeof result.name === 'undefined') {
            console.log(result.name);
            console.log(result.pass);
            $('body').css('height','100px');
            $('.main_page').css('visibility','hidden');
            $('.form_group').css('visibility','visible');
        }
        else {
            chrome.runtime.sendMessage( 
                {Ext_username: result.name,
                Ext_password: result.pass},
                function(response) {
                    result = response.farewell;
                    if (result.raw == 'Successful'){
                        $('body').css('height','300px');
                        $('.main_page').css('visibility','visible');
                        $('.form_group').css('visibility','hidden');
                        $('h4.ext_username').html(result.Username);
                        console.log(result.Fb_name);
                        if (result.Fb_name === '' ){
                            $('p.ext_fb_name').html("[Empty]");
                        }
                        else{
                            $('p.ext_fb_name').html(result.Fb_name);
                        }
                        //$('p.ext_fb_name').html(result.Fb_name);
                        $('p.ext_score').html(result.bully_score+"%");
                        var rank = result.friend_rank;
                        if (rank.length == 0){
                            var x="",i;
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
                    }
                });
      }
      });
        

});

