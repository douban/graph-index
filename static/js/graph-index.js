function change_image(image) {
	var imgold = image;
	var src = imgold.attr('src');
	if (src.indexOf('&now=') > 0) {
		src = src.substring(0, src.indexOf('&now='));
	}
	if (src.indexOf('?') > 0) {
		src = src + "&now=" + (new Date()).getTime();
	} else {
		src = src + "?&now=" + (new Date()).getTime();
	}
	var imgnew = new Image();
	imgnew.src = src;
	$(imgnew).attr('class', imgold.attr('class'));
	$(imgnew).attr('alt', imgold.attr('alt'));
	$(imgnew).attr('style', imgold.attr('style'));
	$(imgnew).load(function(){
		var imgtd = imgold.parent();
		imgtd.html(imgnew);
	});
}

$(document).ready(function(){
	setInterval(function(){
		var day_graphs = $('.day');
		for (var i=0; i<day_graphs.length; i++) {
			var img = $(day_graphs[i]);
			change_image(img);
		}
	}, 10000);
});
