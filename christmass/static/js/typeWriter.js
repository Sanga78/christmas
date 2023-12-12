let i = 0;
let text1 = "Hey friend ";
let text2 = `As the twinkling lights and festive spirit surround us,
may your Christmas be a symphony of laughter, love, and shared moments.
Wishing you joy that echoes through the holiday season and beyond. 
Merry Christmas to you and your cherished ones! 🌟🎁🎄`
let speed = 50;

function typeWriter(text, para){
	if(ok == 2){
		clearInterval(typeInterval);
	}
	if(i < text.length){
		document.getElementById(para).innerHTML += text.charAt(i);
		i++;
		speed = Math.random() * 50 + 100;
	}
	else{
		if(ok == 0){
			i = 0;
		}
		ok += 1;
	}
}

var typeInterval;

//window.onload = function() {
//	window.onload = function(){};
   	typeInterval = setInterval(function(){
		if(ok == 0){
			typeWriter(text1, "txt1");
		}
		else if(ok == 1){
			typeWriter(text2, "txt2");
		}
	}, 50);
//};
