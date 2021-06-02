var socket;
var group;
var order;

$(document).ready(function() {
  namespace = '/test';
    socket = io(namespace);
    socket.on('connect', function() {
        socket.emit('my_event', {data: 'I\'m connected!'});
    });
});

//randomized cards code
// var prototypecard = $(".prototypecard");
// var feedbackcard = $(".feedbackcard");

// function* shuffle(array) {

//   var i = array.length;

//   while (i--) {
//     yield array.splice(Math.floor(Math.random() * (i+1)), 1)[0];
//   }

// }
// var ranNums = shuffle([0,1,2,3]);
// target = ranNums.next().value;
// target2 = ranNums.next().value;
// prototypecard.eq(target).after(feedbackcard.eq(target));
// feedbackcard.eq(target).after(prototypecard.eq(target2));

// target3 = ranNums.next().value;
// prototypecard.eq(target2).after(feedbackcard.eq(target2));
// feedbackcard.eq(target2).after(prototypecard.eq(target3));

// target4 = ranNums.next().value;
// prototypecard.eq(target3).after(feedbackcard.eq(target3));
// feedbackcard.eq(target3).after(prototypecard.eq(target4));
// prototypecard.eq(target4).after(feedbackcard.eq(target4));


//focus textbox on play code
function focustext(text) {
  document.getElementById(text).focus();
}

//ctrl button to focus
var aud;
function playonCtrl(text, audioid){
  aud = audioid;
  document.addEventListener('keydown', function(e) {
    if (e.ctrlKey && document.activeElement == text) {
      document.getElementById(aud).play();
    }
  });
}

//calculation of time code
var count = 0;
var play_times={
"0":0,
"11":0,
"12":0,
"13":0,
"21":0,
"22":0,
"23":0,
"31":0,
"32":0,
"33":0,
"41":0,
"42":0,
"43":0
};

var end_times={
"0": "0",
"11":"0",
"12":"0",
"13":"0",
"21":"0",
"22":"0",
"23":"0",
"31":"0",
"32":"0",
"33":"0",
"41":"0",
"42":"0",
"43":"0"
};

var start_times={
"0":"0",
"11":"0",
"12":"0",
"13":"0",
"21":"0",
"22":"0",
"23":"0",
"31":"0",
"32":"0",
"33":"0",
"41":"0",
"42":"0",
"43":"0"
};
/*var audio=document.getElementsByTagName('audio�)[0];
alert(audio.id);
audio.addEventListener('play�, function () { 
alert("played");
}, false);
$("#audio").click(function() {

});*/

function checkfinalform(){
  console.log("reasontolove", $("#reasontolove").get(0).value);
  console.log("reasontohate", $("#reasontohate").get(0).value);
  console.log("name", $("#name").get(0).value);
  console.log("email", $("#email").get(0).value);

  if( $("#reasontolove").get(0).value == ""||
        $("#reasontohate").get(0).value == ""||
        $("#name").get(0).value == ""||
        $("#email").get(0).value == "") {
          alert(alert_msg);
          return false;
        }else return true;
}

function before_submit(){
  if(!checkfinalform()) {
    return;
  }

  var answer1 = document.getElementsByClassName("ui-state")[0].lastChild.id;
  var answer2 = document.getElementsByClassName("ui-state")[1].lastChild.id;
  var answer3 = document.getElementsByClassName("ui-state")[2].lastChild.id;
  var answer4 = document.getElementsByClassName("ui-state")[3].lastChild.id;

  document.getElementById('answer1').value = answer1;
  document.getElementById('answer2').value = answer2;
  document.getElementById('answer3').value = answer3;
  document.getElementById('answer4').value = answer4;

  console.log(answer1);
  console.log(answer2);
  console.log(answer3);
  console.log(answer4);
  
  var i=0;
  var j=0;
  document.getElementById("0").value = end_times["0"]-start_times["0"];
  document.getElementById("c0").value = play_times["0"];
  for(i=10;i<=40;i=i+10){
    for(j=1;j<=3;j=j+1){
      var k=(i+j).toString();
      var time_interval = end_times[k]-start_times[k];
      var play_time = play_times[k]
      document.getElementById(k).value = time_interval;
      document.getElementById("c"+k).value = play_time;
      console.log(k, time_interval, play_time);
    }
  }
  document.getElementById("myform").submit();
  return true;
}


function record_end(key){
  end_times[key]=Date.now();
  console.log("end_times", key, end_times[key]);
}
function audio_play(key){
  if(start_times[key]==="0")
  start_times[key]=Date.now();
  console.log("start_times", key, start_times[key]);
  play_times[key]=play_times[key]+1;
}


function hideCaptcha1(){
  if(count == 0 && checkPro1_1()){
    document.getElementById("instance1_1").style.display = "none";
    document.getElementById("instance1_2").style.display = "block";
    document.getElementById("instance1_3").style.display = "none";
    document.getElementById("sub1").innerHTML="第二題";
    count += 1;
  }
  else if(count == 1 && checkPro1_2()){
    document.getElementById("instance1_1").style.display = "none";
    document.getElementById("instance1_2").style.display = "none";
    document.getElementById("instance1_3").style.display = "block";
    document.getElementById("instance1").style.display = "none";
    document.getElementById("pronext1").style.display = "inline";
    count = -1;
    document.getElementById("sub1").innerHTML="第三題";
    count += 1;
  }
  else return false;
}

function hideCaptcha2(){
  if(count == 0 && checkPro2_1()){
    document.getElementById("instance2_1").style.display = "none";
    document.getElementById("instance2_2").style.display = "block";
    document.getElementById("instance2_3").style.display = "none";
    document.getElementById("sub2").innerHTML="第二題";
    count += 1;
  }
  else if(count == 1 && checkPro2_2()){
    document.getElementById("instance2_1").style.display = "none";
    document.getElementById("instance2_2").style.display = "none";
    document.getElementById("instance2_3").style.display = "block";
    document.getElementById("instance2").style.display = "none";
    document.getElementById("pronext2").style.display = "inline";
    count = -1;
    document.getElementById("sub2").innerHTML="第三題";
    count += 1;
  }
  else return false;
}

function hideCaptcha3(){
  if(count == 0 && checkPro3_1()){
    document.getElementById("instance3_1").style.display = "none";
    document.getElementById("instance3_2").style.display = "block";
    document.getElementById("instance3_3").style.display = "none";
    document.getElementById("sub3").innerHTML="第二題";
    count += 1;
  }
  else if(count == 1 && checkPro3_2()){
    document.getElementById("instance3_1").style.display = "none";
    document.getElementById("instance3_2").style.display = "none";
    document.getElementById("instance3_3").style.display = "block";
    document.getElementById("instance3").style.display = "none";
    document.getElementById("pronext3").style.display = "inline";
    count = -1;
    document.getElementById("sub3").innerHTML="第三題";
    count += 1;
  }
  else return false;
}

function hideCaptcha4(){
  if(count == 0 && checkPro4_1()){
    document.getElementById("instance4_1").style.display = "none";
    document.getElementById("instance4_2").style.display = "block";
    document.getElementById("instance4_3").style.display = "none";
    document.getElementById("sub4").innerHTML="第二題";
    count += 1;
  }
  else if(count == 1 && checkPro4_2()){
    document.getElementById("instance4_1").style.display = "none";
    document.getElementById("instance4_2").style.display = "none";
    document.getElementById("instance4_3").style.display = "block";
    document.getElementById("instance4").style.display = "none";
    document.getElementById("pronext4").style.display = "inline";
    count = -1;
    document.getElementById("sub4").innerHTML="第三題";
    count += 1;
  }
  else return false;
}


$(document).on("keypress", "input", function (e) {
  var code = e.keyCode || e.which;
  if (code == 13) {
    e.preventDefault();
    return false;
  }
});

var alert_msg = "請確認回答了所有問題！";
function checkPro0() {
  if(!$("#pro0").get(0).value) {
    alert(alert_msg);
    console.log($("#pro0").get(0).value);
    return false;
  }else return true;
}
function checkPro1_1() {
  if(!$("#pro1_1").get(0).value) {
    alert(alert_msg);
    console.log($("#pro1_1").get(0).value);
    return false;
  }else return true;
}
function checkPro1_2() {
  if(!$("#pro1_2").get(0).value) {
    alert(alert_msg);
    console.log($("#pro1_2").get(0).value);
    return false;
  }else return true;
}
function checkPro1_3(){
  if(!$("#pro1_3").get(0).value) {
    alert(alert_msg);
    console.log($("#pro1_3").get(0).value);
    return false;
  }else return true;
}
function checkfeedback1(){
  if(!($("#text_fb1_1").get(0).value && $("#text_fb1_2").get(0).value && $("#text_fb1_3").get(0).value)) {
    alert(alert_msg);
    return false;
  }else return true;
}
  

function checkPro2_1() {
  if(!$("#pro2_1").get(0).value) {
    alert(alert_msg);
    console.log($("#pro2_1").get(0).value);
    return false;
  }else return true;
}
function checkPro2_2() {
  if(!$("#pro2_2").get(0).value) {
    alert(alert_msg);
    console.log($("#pro2_2").get(0).value);
    return false;
  }else return true;
}
function checkPro2_3(){
  if(!$("#pro2_3").get(0).value) {
    alert(alert_msg);
    console.log($("#pro2_3").get(0).value);
    return false;
  }else return true;
}
function checkfeedback2(){
  if(!($("#text_fb2_1").get(0).value && $("#text_fb2_2").get(0).value && $("#text_fb2_3").get(0).value)) {
    alert(alert_msg);
    return false;
  }else return true;
}


function checkPro3_1() {
  if(!$("#pro3_1").get(0).value) {
    alert(alert_msg);
    console.log($("#pro3_1").get(0).value);
    return false;
  }else return true;
}
function checkPro3_2() {
  if(!$("#pro3_2").get(0).value) {
    alert(alert_msg);
    console.log($("#pro3_2").get(0).value);
    return false;
  }else return true;
}
function checkPro3_3(){
  if(!$("#pro3_3").get(0).value) {
    alert(alert_msg);
    console.log($("#pro3_3").get(0).value);
    return false;
  }else return true;
}
function checkfeedback3(){
  if(!($("#text_fb3_1").get(0).value && $("#text_fb3_2").get(0).value && $("#text_fb3_3").get(0).value)) {
    alert(alert_msg);
    return false;
  }else return true;
}

function checkPro4_1() {
  if(!$("#pro4_1").get(0).value) {
    alert(alert_msg);
    console.log($("#pro4_1").get(0).value);
    return false;
  }else return true;
}
function checkPro4_2() {
  if(!$("#pro4_2").get(0).value) {
    alert(alert_msg);
    console.log($("#pro4_2").get(0).value);
    return false;
  }else return true;
}
function checkPro4_3(){
  if(!$("#pro4_3").get(0).value) {
    alert(alert_msg);
    console.log($("#pro4_3").get(0).value);
    return false;
  }else return true;
}
function checkfeedback4(){
  if(!($("#text_fb4_1").get(0).value && $("#text_fb4_2").get(0).value && $("#text_fb4_3").get(0).value)) {
    alert(alert_msg);
    return false;
  }else return true;
}



//jQuery time
(function($) {
  var current_fs, next_fs, previous_fs; //fieldsets
  var left, opacity, scale; //fieldset properties which we will animate
  var animating; //flag to prevent quick multi-click glitches

  $(".next").click(function() {
    // console.log("get into next");
    // console.log(animating)
    if (animating) return false;
    animating = true;

    current_fs = $(this).parent();
    next_fs = $(this).parent().next();

    if(this.id === 'pronext0') {
      if(!checkPro0()) {
        animating = false;
        return;
      }
    }else if(this.id === 'pronext1') {
      if(!checkPro1_3()) {
        animating = false;
        return;
      }
    }else if(this.id === 'feedbacknext1') {
      if(!checkfeedback1()) {
        animating = false;
        return;
      }
    }else if(this.id === 'pronext2') {
      if(!checkPro2_3()) {
        animating = false;
        return;
      }
    }else if(this.id === 'feedbacknext2') {
      if(!checkfeedback2()) {
        animating = false;
        return;
      }
    }else if(this.id === 'pronext3') {
      if(!checkPro3_3()) {
        animating = false;
        return;
      }
    }else if(this.id === 'feedbacknext3') {
      if(!checkfeedback3()) {
        animating = false;
        return;
      }
    }else if(this.id === 'pronext4') {
      if(!checkPro4_3()) {
        animating = false;
        return;
      }
    }else if(this.id === 'feedbacknext4') {
      if(!checkfeedback4()) {
        animating = false;
        return;
      }
    }

    //activate next step on progressbar using the index of next_fs
    $("#progressbar li").eq($("fieldset").index(next_fs) + 1).addClass("active");

    //show the next fieldset
    next_fs.show();
    //hide the current fieldset with style
    current_fs.animate({
      opacity: 0
    }, {
      step: function(now, mx) {
        //as the opacity of current_fs reduces to 0 - stored in "now"
        //1. scale current_fs down to 80%
        scale = 1 - (1 - now) * 0.2;
        //2. bring next_fs from the right(50%)
        left = (now * 50) + "%";
        //3. increase opacity of next_fs to 1 as it moves in
        opacity = 1 - now;
        current_fs.css({
          'transform': 'scale(' + scale + ')'
        });
        next_fs.css({
          'left': left,
          'opacity': opacity
        });
      },
      duration: 800,
      complete: function() {
        current_fs.hide();
        animating = false;
      },
      //this comes from the custom easing plugin
      easing: 'easeInOutBack'
    });
  });

  $(".previous").click(function() {
    if (animating) return false;
    animating = true;

    current_fs = $(this).parent();
    previous_fs = $(this).parent().prev();

    //de-activate current step on progressbar
    $("#progressbar li").eq($("fieldset").index(current_fs)).removeClass("active");

    //show the previous fieldset
    previous_fs.show();
    //hide the current fieldset with style
    current_fs.animate({
      opacity: 0
    }, {
      step: function(now, mx) {
        //as the opacity of current_fs reduces to 0 - stored in "now"
        //1. scale previous_fs from 80% to 100%
        scale = 0.8 + (1 - now) * 0.2;
        //2. take current_fs to the right(50%) - from 0%
        left = ((1 - now) * 50) + "%";
        //3. increase opacity of previous_fs to 1 as it moves in
        opacity = 1 - now;
        current_fs.css({
          'left': left
        });
        previous_fs.css({
          'transform': 'scale(' + scale + ')',
          'opacity': opacity
        });
      },
      duration: 800,
      complete: function() {
        current_fs.hide();
        animating = false;
      },
      //this comes from the custom easing plugin
      easing: 'easeInOutBack'
    });
  });

})(jQuery);
