const STATE_IDLE = 0;
const STATE_PROCESSING = 1;
const STATE_DETECTING_FACE = 3
const STATE_DETECT_SUCCESSFUL = 4;

const SERVER_SUCCESS = 0
const SERVER_FAKE_IMAGE = 1
const SERVER_USER_NOT_EXIST = 2
const SERVER_INVALID_FACE = 3
const SERVER_NO_QR_CODE = 4

var streaming = false;
var video = null;
var canvas = null;
var faceCanvas = null
var photo = null;
var state = STATE_IDLE;

var faceTop, faceLeft, faceSize;

$(window).ready(function () {
	startup();
});

async function startup() {
	video = document.getElementById('video');
	canvas = document.getElementById('canvas');
	faceCanvas = document.getElementById('face_track');
	photo = document.getElementById('photo');

	navigator.mediaDevices.getUserMedia({ video: true, audio: false })
		.then(function (stream) {
			video.srcObject = stream;
			video.play();
			setTimeout(() => {
				recognize();
			}, 2000);
		})
		.catch(function (err) {
			console.log("An error occurred! " + err);
		});
}

function captureImage() {
	var context = canvas.getContext('2d');
	var width = video.videoWidth;
	var height = video.videoHeight;
	
	canvas.width = faceCanvas.width = width;
	canvas.height = faceCanvas.height = height;
	// context.translate(width, 0);
	// context.scale(-1, 1);
	context.drawImage(video, 0, 0, width, height);
	return canvas.toDataURL('image/jpeg');
}

function post(data, action, callback) {
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
function trackFace() {
	var ctx = faceCanvas.getContext("2d");
	ctx.scale(-1, 1);
	ctx.beginPath()
	ctx.strokeStyle = "red";
	ctx.lineWidth = "3px";
	ctx.strokeRect(faceLeft, faceTop, faceSize, faceSize);
}

function updateFaceLocation(top, left, size){
	faceTop = top;
	faceLeft = left;
	faceSize = size;
}

function showCheckInSuccess(text){
	document.getElementById("text").style.backgroundColor = "white";
	document.getElementById("text").innerText = text;
}

function recognize() {
	var imageData = captureImage();
	if (imageData.length <= 23) return;

	post({ image_data: imageData }, '/recognize',
		function (result) {
			console.log(result)
			var text = "";
			switch (result.code) {
				case SERVER_INVALID_FACE:
					state = STATE_IDLE;
					setTimeout(() => {
						recognize();
					}, 500);
					break;
				case SERVER_FAKE_IMAGE:
					state = STATE_PROCESSING
					updateFaceLocation(result.face_top, result.face_left, result.face_size)
					setTimeout(() => {
						recognize();
					}, 100);
					break;
				
				case SERVER_USER_NOT_EXIST:
					state = STATE_PROCESSING;
					updateFaceLocation(result.face_top, result.face_left, result.face_size)
					setTimeout(() => {
						recognize();
					}, 100);
					break;
				case SERVER_NO_QR_CODE:
					state = STATE_DETECT_SUCCESSFUL
					text= "Face Checkin\nTên: " + result.fullname + "\nMã nhân viên: " + result.staff_code + "\nThời gian: "+ result.checkin_time;
					showCheckInSuccess(text)
					setTimeout(() => {
						state = STATE_PROCESSING
						recognize();	
					}, 4000);
					break
				case SERVER_SUCCESS:
					state = STATE_DETECT_SUCCESSFUL
					document.getElementById("text").innerText = result.staff_code + "- " + result.fullname;
					if(result.is_checkin)
						text = "Mượn sách\n";
					else 
						text = "Trả sách\n";
					text += "Người mượn: " + result.fullname + "\nMã nhân viên: " + result.staff_code +"\n\nTên sách: "+ result.book_name +"\nTác giả: "+result.book_author+ "\nThời gian: "+ result.checkin_time;
					showCheckInSuccess(text)
					updateFaceLocation(result.face_top, result.face_left, result.face_size)
					setTimeout(() => {
						state = STATE_PROCESSING
						recognize();	
					}, 4000);
					break;
				default:
					break;
			}
		}
	);
}

setInterval(function () {
	//draw border
	switch (state) {
		case STATE_IDLE:
			document.getElementById("state").innerText = "STATE_IDLE";
			document.getElementById("overlay").style.visibility = "hidden";
			document.getElementById("face_track").style.visibility = "hidden";
			document.getElementById("text").style.backgroundColor = "transparent"
			document.getElementById("text").innerText= ""
			break;
		case STATE_PROCESSING:
			document.getElementById("state").innerText = "STATE_PROCESSING";
			document.getElementById("overlay").style.visibility = "visible";
			document.getElementById("face_track").style.visibility = "visible";
			document.getElementById("text").style.backgroundColor = "transparent"
			document.getElementById("text").innerText= ""
			break;
		case STATE_DETECT_SUCCESSFUL:
			document.getElementById("state").innerText = "STATE_DETECT_SUCCESSFUL";
			document.getElementById("overlay").style.visibility = "hidden";
			document.getElementById("face_track").style.visibility = "visible";
			break;
	}
}, 50);


setInterval(() => {
	switch (state) {
		case STATE_IDLE:
			faceCanvas.style.visibility = "hidden"
			break;
		case STATE_PROCESSING:
		case STATE_DETECT_SUCCESSFUL:
			faceCanvas.style.visibility = "visible"
			trackFace();
			break;
	}
}, 30);
