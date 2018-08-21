$(function() {
	setInterval(function() {

		var currentTime = new Date();
		var hours = currentTime.getHours();
		var minutes = currentTime.getMinutes();
		var seconds = currentTime.getSeconds();
		var month = currentTime.getMonth()+1;
		var day = currentTime.getDate();

		var output = ((''+day).length<2 ? '0' : '') + day + '/' +
		    ((''+month).length<2 ? '0' : '') + month + '/' + currentTime.getFullYear();

		    $('.date').html(output);
	  // Add leading zeros
		hours = (hours < 10 ? "0" : "") + hours;
		minutes = (minutes < 10 ? "0" : "") + minutes;
		seconds = (seconds < 10 ? "0" : "") + seconds;

		// Compose the string for display
		var currentTimeString = hours + ":" + minutes + ":" + seconds;
		$(".time").html(currentTimeString);

	}, 1000);
});