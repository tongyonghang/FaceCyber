
var serverhost = 'http://127.0.0.1:8000';

	chrome.runtime.onMessage.addListener(
		function(message, sender, sendResponse) {

			if ((message.hello === 'Received scraper command.')){
				var url = serverhost + '/accounts/get_scraper/?username='+ encodeURIComponent(message.ext_username);
				console.log(message.hello);
				console.log(url);

				fetch(url)
				.then(response => response.json())
				.then(response => sendResponse({farewell: response}))
				.catch(error => console.log(error))

				return true;
			}
			else{
				var url = serverhost + '/accounts/get_wiki_summary/?username='+ encodeURIComponent(message.Ext_username) +'&password=' + encodeURIComponent(message.Ext_password);
			
			console.log(url);

            fetch(url)
			.then(response => response.json())
			.then(response => sendResponse({farewell: response}))
			.catch(error => console.log(error))
            
			return true;  // Will respond asynchronously.
			}
	});


	