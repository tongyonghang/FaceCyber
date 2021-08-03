
function moveCursorToEnd(el) {
    if (typeof el.selectionStart == "number") {
        el.selectionStart = el.selectionEnd = el.value.length;
    } else if (typeof el.createTextRange != "undefined") {
        el.focus();
        var range = el.createTextRange();
        range.collapse(false);
        range.select();
    }
}

function PosEnd(end) {
    console.log("RUN");
    var len = end.innerText.length;
      
    // Mostly for Web Browsers
    if (end.setSelectionRange) {
        end.focus();
        end.setSelectionRange(len, len);
    } else if (end.createTextRange) {
        var t = end.createTextRange();
        t.collapse(true);
        t.moveEnd('character', len);
        t.moveStart('character', len);
        t.select();
    }
}

async function CommentClick(){
    //document.querySelectorAll("form[role='presentation']").onclick = CommentScan;
    const url = chrome.runtime.getURL('en.txt');
    let response = await fetch(url);
    let data = await response.text();
    const rows = data.split('\n');
    var inputs = document.querySelectorAll("form[role='presentation'] > div > div > div._5rpb > div > div > div > div > span > span ");
    var marked_1 ="";
    var flag = 0;
    for (i = 0; i < inputs.length; i++) {
    //console.log("Comment->"+inputs[i].innerText);
    //console.log("Comment"+inputs[i].innerText.length);
    if (inputs[i].innerText.length > 1){
        marked_1 = inputs[i].innerText;
        console.log(inputs[i].innerHTML);
        comment_test = inputs[i].innerHTML;
        try {
            var lowerstr = marked_1.toLowerCase();
            for (row of rows) {
                if (lowerstr.includes(row)){
                    console.log("scan",lowerstr);
                    //console.log("input",inputs[i].innerHTML);
                    //marked_1 = comment_test.replaceAll(scan_1,"<div class='tooltip' name='check'><span class='tooltiptext'>Bad Word !</span>"+scan_1+"</div>");
                    //marked_1 = marked_1.replaceAll(scan_1,"<div class='tooltip'>"+scan_1+"</div>");
                    marked_1 = marked_1.replaceAll(row,"<div class='tooltip' readonly><span class='tooltiptext'></span>"+row+"</div>");
                    flag = 1;
                }
            }
            if (flag == 1){
            console.log("scan_1",marked_1);
            if( marked_1.length > 1 ){
                inputs[i].innerHTML = marked_1;
                //inputs[i].innerHTML = "";
            }
            //var inputs_2 = document.querySelectorAll("form[role='presentation'] > div > div > div._5rpb > div ");
            PosEnd(inputs[i]);
            }
            flag = 0;
        }
        catch(e){
            console.log("skip");
            var lowerstr = marked_1.toLowerCase();
            for (row of rows) {
                if (lowerstr.includes(row)){
                    console.log("scan",lowerstr);
                    //console.log("input",inputs[i].innerHTML);
                    //marked_1 = comment_test.replaceAll(scan_1,"<div class='tooltip' name='check'><span class='tooltiptext'>Bad Word !</span>"+scan_1+"</div>");
                    //marked_1 = marked_1.replaceAll(scan_1,"<div class='tooltip'>"+scan_1+"</div>");
                    marked_1 = marked_1.replaceAll(row,"<div class='tooltip' readonly><span class='tooltiptext'></span>"+row+"</div>");
                    flag = 1;
                }
            }
            if (flag == 1){
                console.log("scan_1",marked_1);
                if( marked_1.length > 1 ){
                    inputs[i].innerHTML = marked_1;
                    //inputs[i].innerHTML = "";
                }
                //var inputs_2 = document.querySelectorAll("form[role='presentation'] > div > div > div._5rpb > div ");
                PosEnd(inputs[i]);
                }
                flag = 0;
            
        }
    }
}
}


function PostScan() {
    var test = setTimeout(PostTimer, 5000);
    async function PostTimer(){
        const url = chrome.runtime.getURL('en.txt');
        let response = await fetch(url);
        let data = await response.text();
        const rows = data.split('\n');
        var marked_2 = "";
        var detected = 0;
        var test3 = document.querySelector("div.rq0escxv.buofh1pr.df2bnetk.hv4rvrfc.dati1w0a.l9j0dhe7.k4urcfbm.du4w35lb.gbhij3x4 > div > div > div > div > div > div > div > div > div > span > span");
        var test1 = document.querySelector("div.rq0escxv.buofh1pr.df2bnetk.hv4rvrfc.dati1w0a.l9j0dhe7.k4urcfbm.du4w35lb.gbhij3x4 > div > div > div > div > div > div > div > div > div");
        try {
            var test2 = test3.innerText;
            marked_2 = test2;
            console.log(">>>",test2);
            //var test2 = test1.innerText;
        }
        catch(e){
            console.log("skip")
        }
        //console.log("Post"+test2.length);
        //console.log("Post->"+test2);
        try {
            if (test2.length > 1) {
                    var lowerstr = test2.toLowerCase();
                    //var n = lowerstr.includes(row.split("\n"));
                    //console.log(lowerstr);
                    for (row of rows) {
                        if (lowerstr.includes(row)){
                            console.log("scan",lowerstr);
                            //console.log("input",inputs[i].innerHTML);
                            marked_2 = marked_2.replaceAll(row,"<div class='tooltip' readonly><span class='tooltiptext'></span>"+row+"</div>");
                            //marked_2 = marked_2.replaceAll(scan_1,"<mark>"+scan_1+"</mark>");
                            //marked_2 = test2.replaceAll(scan_1,"<div class='tooltip'>****</div>");
                            //marked_2 = marked_2.replaceAll(scan_1,"<div class='tooltip'>"+scan_1+"</div>");
                            detected = 1;
                        }   
                    }
                    if (detected == 1){
                        console.log("scan_1",marked_2);
                        if( marked_2.length > 1 ){
                            test3.innerHTML = marked_2;
                        }
                        moveCursorToEnd(test3);    
                        }
                    detected = 0;
                }
                
        }
        catch(e){
            console.log(e);
            console.log("length skip");
            if (test2.length > 1) {
                var lowerstr = test2.toLowerCase();
                    //var n = lowerstr.includes(row.split("\n"));
                    //console.log(lowerstr);
                    for (row of rows) {
                        if (lowerstr.includes(row)){
                            console.log("scan",lowerstr);
                            //console.log("input",inputs[i].innerHTML);
                            marked_2 = marked_2.replaceAll(row,"<div class='tooltip readonly'><span class='tooltiptext'></span>"+row+"</div>");
                            //marked_2 = marked_2.replaceAll(scan_1,"<mark>"+scan_1+"</mark>");
                            //marked_2 = test2.replaceAll(scan_1,"<div class='tooltip'>****</div>");
                            //marked_2 = marked_2.replaceAll(scan_1,"<div class='tooltip'>"+scan_1+"</div>");
                            detected = 1;
                        }   
                    }  
                    if (detected == 1){
                        console.log("scan_1",marked_2);
                        if( marked_2.length > 1 ){
                            test3.innerHTML = marked_2;
                        }
                        moveCursorToEnd(test3);    
                    }
                    detected = 0;
            }
        }
    } 
}


function CollectTimer(){
    chrome.storage.sync.get(['name','pass'], function(result) {
    console.log('Value currently is ' + result.name);
    if(typeof result.name === 'undefined') {
                console.log(result.name);
                console.log(result.pass);
        }
    else{
        //alert('FaceCyber is starting to collect your data. Please do not refresh this tab.');
        chrome.runtime.sendMessage(
            {ext_username:result.name,
            hello:'Received scraper command.'},
            function(response){
                result = response.farewell;
                if(result.scraped == 'success'){
                    alert('Data collection complete.');
                }
                else if(result.scraped == 'fail'){
                    alert('Something wrong with your facebook data. Please make sure you fill the correct information');
                }
            });
        }
    });
}

window.onload = setInterval(CommentClick, 5000);
window.onload = setInterval(PostScan,5000);
window.onload = setInterval(CollectTimer, 300000);

chrome.storage.sync.get(['name','pass'], function(result) {
    console.log('Value currently is ' + result.name);
    if(typeof result.name === 'undefined') {
        console.log(result.name);
        console.log(result.pass);
    }
    else{
        //alert('FaceCyber is starting to collect your data. Please do not refresh this tab.');
        chrome.runtime.sendMessage(
            {ext_username:result.name,
            hello:'Received scraper command.'},
            function(response){
                result = response.farewell;
                if(result.scraped == 'success'){
                    alert('Data collection complete.');
                }
                else if(result.scraped == 'fail'){
                    alert('Something wrong with your facebook data. Please make sure you fill the correct information');
                }
            });
        
    }
  });


