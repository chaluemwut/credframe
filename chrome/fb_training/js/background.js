chrome.runtime.onStartup.addListener(initOnStartup);
chrome.runtime.onMessage.addListener(callAPI);

var apiRoot  = 'http://fbcredibility.com/fbcollect/process';
// var apiRoot  = 'http://localhost:5000/fbcollect/process';


var xhrF, xhrC = [];

function initOnStartup() {
	console.log('3');
	chrome.storage.local.clear();

	setInterval(function() { chrome.storage.local.clear(); }, (15*60*1000));
}

function callAPI(request, sender, sendResponse) {	
	if (request.action == 'fetch_credibility') {
		console.log('before');
		console.log(request.fbpost);
		var xhr = new XMLHttpRequest();
		var url = apiRoot+'?return_id='+request.fbpost.return_id
		+'&cred_value='+request.fbpost.cred_value
		+'&likes='+request.fbpost.likes
		+'&shares='+request.fbpost.shares
		+'&comments='+request.fbpost.comments
		+'&hash_tag='+request.fbpost.hashtag
		+'&images='+request.fbpost.images
		+'&vdo='+request.fbpost.vdo
		+'&poster_id='+request.fbpost.poster_id
		+'&message='+encodeURIComponent(request.fbpost.message);
		console.log('location : '+request.fbpost.location);
		xhr.open("get", url, false);
		xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
		xhr.onreadystatechange = function() {
			var response = {return_id:'', description:'', status:''};
			console.log(xhr.responseText);
			var fbres = JSON.parse(xhr.responseText);
			response.return_id = fbres.data.return_id;
			response.text = 'ขอบคุณครับ';
			response.status = 1;
			try {
				sendResponse(response);
			} catch(err) { 
				console.log("Couldn't send response: ", err); 
			}			
		}

		try { 
			xhr.send(null);
		} catch(err) { 
			console.log("Couldn't send XMLHttpRequest: ", err); 
		}
	}
}