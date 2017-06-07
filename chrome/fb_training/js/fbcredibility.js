function get_content_url(user_content, user_content_img){
	var url_list = $(user_content).find("a").not("[class='_58cn'],[class='see_more_link']");
	return url_list.length;
}

function get_content_vdo(user_content_img){
	var vdo_list = $(user_content_img).find("i[class='_1jto _bsl _3htz']");
	return vdo_list.length;	
}

function get_content_image(user_content_img){
	var img_num = $(user_content_img).find("img[class='scaledImageFitWidth img'],img[class='scaledImageFitHeight img'],img[class='_46-i img']");
	// var img_type2 = $(user_content_img).find("img[class='_46-i img']");
	var is_vdo = $(user_content_img).find("i[class='_6o1']");
	return img_num.length-is_vdo.length;
}

function get_comments_shares(user_content){
	var comment_share = $(user_content).find('div[class="_ipo"] > div');
	var comment = $(comment_share[0]).text().replace(" Comments","").replace(" Comment","");
	comment = comment.replace("ความคิดเห็น","").replace(" รายการ","");
	var share = $(comment_share[1]).text().replace(" Shares", "").replace(" Share","");
	share = share.replace("แชร์ ","").replace(" ครั้ง","");
	return [comment==""?0:comment, share==""?0:share];
}

function get_likes(user_content){
	//var child_content = user_content.children('div')[1]; _4arz
	var like_a_obj = $(user_content).find('span[class=_4arz] > span');
	var like_text = like_a_obj.text();
	if (like_text == ''){
		return 0;
	}
	
	if (isNumeric(like_text)){
		return like_text;
	}
	if ((like_text.indexOf('K') != -1) && isNumeric(like_text.replace('K',''))){
		return parseFloat(like_text.replace('K',''))*1000;
	}
	var like_arr = like_text.split(',');
	var tail_arr = like_arr[like_arr.length-1].split(' and ');
	//var other_like = tail_arr[1].replace("other","");
	var tail_str = new String(tail_arr[1])
	var tail_like = tail_str.replace(' others','');
	if ((tail_like.indexOf('K') != -1) && isNumeric(tail_like.replace('K',''))){
		var tail_like_number = parseFloat(tail_like.replace('K',''))*1000;
		return (tail_arr.length-1)+tail_like_number;
	} else if (isNumeric(tail_like)) {
		return like_arr.length+parseFloat(tail_like);
	}
}

function get_hash_tag(user_content){
	var url_list = $(user_content).find("span[class='_58cm']");
	return url_list.length;
}

https://www.facebook.com/ThairathFan/?hc_ref=NEWSFEED&fref=nf
function create_user_post(user_content){
	var user_obj = $(user_content).find('span[class="fwn fcg"] > span[class="fwb fcg"] > a');
	var href_text = user_obj.attr('href');
	if (href_text == undefined){
		var href_link = $(user_content).find('a[class="profileLink"]');
		if (href_link == undefined){
			return undefined;
		}
		href_text = href_link.attr('href');
		if(href_text.indexOf('profile.php?') != -1){
			var no_page_user = href_text.substring(0, href_text.indexOf('&hc_ref'));
			no_page_user = no_page_user.replace('https://www.facebook.com/profile.php?id=', '');
			return no_page_user;
		}	
	}
	try{
		var str_user_id = href_text.substring(0, href_text.indexOf('/?'));	
		str_user_id = str_user_id.replace('https://www.facebook.com/', '');	
		if (str_user_id == ''){
			href_link = $(user_content).find('a[class="profileLink"]');
			str_user_id = href_text.substring(0, href_text.indexOf('?'));
			str_user_id = str_user_id.replace('https://www.facebook.com/', '');	
			return str_user_id;
		} else {
			return str_user_id;
		}
		// return str_user_id;	
	} catch (err){
		return undefined;
	}
}

function createFeatureDiv(divId, feature){
	ret = '<div>';
	for(var key in feature){
		ret += templateFeatureDiv(key+'_'+divId, feature[key], 'hidden');
	}
	ret += '</div>';
	return ret;
}

function templateFeatureDiv(dataId, data, type){
	if (typeof(data) == 'string'){
		data = data.replace(/[&'"]/g, '');
	}
	return '<input type="'+type+'" id="'+dataId+'"value="'+data+'"/>';
}

function isNumeric(n) {
  return !isNaN(parseFloat(n)) && isFinite(n);
}

function createButton(divId){
	ret = ' <div class="right_div" id=rating_container_'+divId+'>';
	ret += ' <button id=b_yes_'+divId+' value="Yes">Yes</button>';
	ret += ' <button id=b_no_'+divId+' value="No">No</button>';
	ret += ' </div>';
	return ret;
}

function insertKKUDiv(divId, features){
	var str = '<div id=kku_'+divId+' style="position: relative; margin-top: 10px; margin-bottom: 10px;">';
	str += '<span style="color:orange">FB credibility : </span>';
	str += 'ข้อมูลนี้น่าเชื่อถือหรือไม่';
	str += createButton(divId);
	str += createFeatureDiv(divId, features);
	str += '</div>';
	return str;
}

function template_sender(index, value){
	var likes = $("#likes_"+index).val();
	var shares = $("#shares_"+index).val();
	var comments = $("#comments_"+index).val();
	var hashtag = $("#hash_tag_"+index).val();
	var images = $("#images_"+index).val();
	var vdo = $("#vdo_"+index).val();
	var poster_id = $("#poster_id_"+index).val();
	var message = $("#message_"+index).val();

	FBPostObj = {return_id:index, likes: likes, shares: shares, 
				comments: comments, hashtag: hashtag, images: images, poster_id:poster_id,
				vdo: vdo, message: message, cred_value: value};

	var request = {action: 'fetch_credibility', fbpost: FBPostObj};
	chrome.runtime.sendMessage(request, function(response) {
			var return_id = response.return_id;
			var description = response.text;
			var status = response.status;
			var kkuDiv = $('#rating_container_'+return_id);
			kkuDiv.append(description);

			$('#b_yes_'+return_id).attr('disabled','disabled');
			$('#b_no_'+return_id).attr('disabled','disabled');
	});

}

$(document).ready(function () {
	var panel = $('<div class="panel panel-default tweetcred-logo"></div>');
	var logo  = new Image();
	// panel.append("<span>FB credibility powered by</span><br/>");
	logo.src = chrome.extension.getURL("img/logo.png");

	$(logo).load(function() {
		panel.append(logo);

		$(document.body).append(panel);

		panel.fadeIn(600, function() {
				setTimeout(function() {
					panel.fadeOut(600, function() {
							panel.remove();

							panel = null;
							logo  = null;
					});
				}, 1800);
		});
	});	
	setInterval(function(){
		$("div[class*='fbUserContent']").each(function(i){
			// var main_content = $(this);				
			// var user_content = $(main_content).find("div[class*='fbUserContent']");
			var user_content = $(this);
			var fb_content = $(user_content).find("div[class='_5x46']");			
			var likes_comments = get_comments_shares($(user_content).find("div[class*='_ipn clearfix']"));
			if($(fb_content).find("[id^='kku_']").length == 0){					
				var likes_data = get_likes(user_content);
				var features = {};
				features['likes'] = likes_data;				
				features['comments'] = likes_comments[0]; //ok
				features['shares'] = likes_comments[1]; //ok
				features['hash_tag'] = get_hash_tag(user_content);
				features['images'] = get_content_image($(user_content).find("div[class='mtm']"));
				features['vdo'] = get_content_vdo($(user_content).find("div[class='mtm']")); //ok
				features['poster_id'] = create_user_post(user_content);
				features['message'] = $(this).find('div[class="_5pbx userContent"]').text(); //ok							
				$(fb_content).append(insertKKUDiv(i, features));

				$("#b_yes_"+i).click(function(){
					var value = $('#b_yes_'+i).val();
					template_sender(i, value);
				});
				$("#b_no_"+i).click(function(){
					var value = $('#b_no_'+i).val();
					template_sender(i, value);
				});					
			}


		});
	}, 3000);
 
});
