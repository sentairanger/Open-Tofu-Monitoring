$('#forward').on('mousedown', function(){
	$.get('/forward');
	});
$('#forward').on('mouseup', function(){
	$.get('/stop');
	});
$('#backward').on('mousedown', function(){
	$.get('/backward');
	});
$('#backward').on('mouseup', function(){
	$.get('/stop');
	});

$('#left').on('mousedown', function(){
	$.get('/left');
	});
$('#left').on('mouseup', function(){
	$.get('/stop');
	});

$('#right').on('mousedown', function(){
	$.get('/right');
	});
$('#right').on('mouseup', function(){
	$.get('/stop');
	});

$('#on').on('mousedown', function(){
	$.get('/on');
	});
$('#on').on('mouseup', function(){
	$.get('/off');
	});
$('#north').on('mousedown', function(){
	$.get('/north');
	});
$('#north').on('mouseup', function(){
	$.get('/stop2');
	});
$('#south').on('mousedown', function(){
	$.get('/south');
	});
$('#south').on('mouseup', function(){
	$.get('/stop2');
	});
$('#west').on('mousedown', function(){
	$.get('/west');
	});
$('#west').on('mouseup', function(){
	$.get('/stop2');
	});
$('#east').on('mousedown', function(){
	$.get('/east');
	});
$('#east').on('mouseup', function(){
	$.get('/stop2');
	});
$('#eye').on('mousedown', function(){
	$.get('/torvaldson');
	});
$('#eye').on('mouseup', function(){
	$.get('/torvaldsoff');
	});

var slider = document.getElementById("pwmrange");
var output = document.getElementById("pwm");
output.innerHTML = slider.value;

slider.oninput = function() {
  output.innerHTML = this.value;
};


var slider2 = document.getElementById("servo");
var output2 = document.getElementById("servo1");
output2.innerHTML = slider2.value;

slider2.oninput = function() {
  output2.innerHTML = this.value;
};

var slider3 = document.getElementById("servotwo");
var output3 = document.getElementById("servo2");
output3.innerHTML = slider3.value;

slider3.oninput = function() {
  output3.innerHTML = this.value;
};
