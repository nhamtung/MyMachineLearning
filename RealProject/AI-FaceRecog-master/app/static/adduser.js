const MAX_COUNT = 5;
var streaming = false;
var video = null;
var canvas = null;
var photo = null;
var recordedNumber = 0;
var fullname = "";
var staff_code = "";

const STATE_IDLE = 0;
const STATE_RECORDING = 1;
const STATE_FINISHED = 2;
var state = STATE_IDLE;

const SERVER_SUCCESS = 0;
const SERVER_USER_NOT_EXISTED = 2;
const SERVER_INVALID_FACE = 3;
const SERVER_USER_EXISTED = 5;

$(window).ready(function () {
	startup();
});

function startup() {
	video = document.getElementById('video');
	canvas = document.getElementById('canvas');
	photo = document.getElementById('photo');
	$("#text").show();
	$("#text").css("fontSize", 36);
	document.getElementById("overlay").style.visibility = "hidden";

	navigator.mediaDevices.getUserMedia({ video: true, audio: false })
		.then(function (stream) {
			video.srcObject = stream;
			video.play();
		})
		.catch(function (err) {
			console.log("An error occurred! " + err);
		});
}

function addUser() {
	fullname = $("#fullname").val().trim();
	staff_code = $("#staff_code").val().trim();

	if (staff_code == '') {
		alert('Please enter user id');
		return;
	}

	if (fullname == '') {
		alert('Please enter user name');
		return;
	}
	requestServer(
		{ staff_code: staff_code },
		'/user/check_user',
		function (result) {
			switch (result.code) {
				case SERVER_USER_NOT_EXISTED:
					startRecording();
					break;
				case SERVER_USER_EXISTED:
					var confirmDelete = confirm("User is exised.\nDo you want to remove?")
					if (confirmDelete) {
						requestServer({staff_code: staff_code},
							'/delete_user',
							function(){
								startRecording();
							}
						)
					}
					break;
			}
		});

}

function captureImage() {
	var context = canvas.getContext('2d');
	canvas.width = video.videoWidth;
	canvas.height = video.videoHeight;
	// context.translate(canvas.width, 0);
	// context.scale(-1, 1);
	context.drawImage(video, 0, 0, video.videoWidth, video.videoHeight);
	return canvas.toDataURL('image/jpeg');
}

function startRecording() {
	recordedNumber = 0;
	state = STATE_RECORDING;
}

function requestServer(data, action, callback) {
	$.ajax({
		url: action,
		contentType: "application/json",
		data: JSON.stringify(data),
		method: "POST",
		success: function (result) {
			if (callback) callback(result);
		}
	});
}


setInterval(() => {
	console.log("state=", state)
	if (state == STATE_RECORDING) {
		$("#text").text("Recording: " + recordedNumber);
		document.getElementById("overlay").style.visibility = "visible";
		var imageData = captureImage();
		if (imageData.length <= 23) return;

		requestServer({
			image_data: imageData,
			fullname: fullname,
			staff_code: staff_code
			},
			'/add_user_image',
			function(result){
				if(result.code == SERVER_INVALID_FACE){
					document.getElementById("overlay").style.borderColor = "orange";
				}else{
					document.getElementById("overlay").style.borderColor = "aqua";
					recordedNumber++;
					if(recordedNumber >= MAX_COUNT){
						state = STATE_FINISHED;
						document.getElementById("overlay").style.visibility = "hidden";
						$("#text").text("Done");
						video.pause();
						setTimeout(() => {
							state = STATE_IDLE;
							video.play();
							recordedNumber  = 0 
							$("#text").text("");
							document.getElementById('fullname').value='';  
							document.getElementById('staff_code').value='' ;
						}, 2000);
					}
				}
			});
	}
}, 800);

setInterval(() => {
	$("#overlay").fadeOut();
	$("#overlay").fadeIn();
}, 900);
