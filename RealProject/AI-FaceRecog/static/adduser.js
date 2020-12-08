const MAX_COUNT = 5;
var streaming = false;
var video = null;
var canvas = null;
var photo = null;
var recording = false;
var countDown = 0;
var username = "";

$(window).ready(function() {
    startup();
});

function startup() {
    video = document.getElementById('video');
    canvas = document.getElementById('canvas');
    photo = document.getElementById('photo');

	navigator.mediaDevices.getUserMedia({ video: true, audio: false })
    .then(function(stream) {
        video.srcObject = stream;
        video.play();
    })
    .catch(function(err) {
        console.log("An error occurred! " + err);
    });
}

function addUser() {
	username = $("#username").val().trim();

	if(username == '') {
		alert('Please enter user name');
		return;
	}

	recording = true;
	countDown = MAX_COUNT + 1;

	$("#text").show();
	$("#text").css("fontSize", 36);
	$("#text").text("Recording new user ...");
}

function captureImage() {
	var context = canvas.getContext('2d');
	var width = video.videoWidth;
	var height = video.videoHeight;
	canvas.width = width;
	canvas.height = height;
	context.drawImage(video, 0, 0, width, height);
	return canvas.toDataURL('image/jpeg');
}

function post(data, action, callback){
	$.ajax({
		url: action,
		contentType: "application/json",
		data : JSON.stringify(data),
		method: "POST",
		success: function(result){
			if(callback) callback(result);
		}
	});
}

setInterval(function(){
	var imageData = captureImage();
	if(imageData.length <= 23) return;

	if(recording) {
		if(countDown > 0 && countDown <= MAX_COUNT){
			post({
					image_data : imageData,
					username : username
				},
				'/add_user_image'
			);
			$("#text").css("fontSize", 72);
			$("#text").text(countDown);
		}else if(countDown == 0){
			$("#text").css("fontSize", 36);
			$("#text").text("Done");
		}else if(countDown < 0){
			$("#text").text("");
			recording = false;
		}
		countDown--;
	}
}, 2000);
