$(function(){
$('#button_style').click(function(){
    var newURL = "http://127.0.0.1:8000/";
    chrome.tabs.create({ url: newURL });
});
});