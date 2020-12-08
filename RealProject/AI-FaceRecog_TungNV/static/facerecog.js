var streaming = false;
var video = null;
var canvas = null;
var photo = null;

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
    post({image_data : imageData}, '/recognize',
        function(result) {
            $("#text").css("fontSize", 18);
			$("#text").text(result.username);
			var context = canvas.getContext('2d');
			context.rect(20,20,150,150);
			context.strokeStyle="green";
			context.stroke();
        }
    );
}, 2000);
