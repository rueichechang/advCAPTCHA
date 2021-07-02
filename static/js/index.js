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

//focus textbox on play code
function focustext(pro_id) {
  document.getElementById(pro_id).focus();
  console.log(pro_id, "already focus");
}

//ctrl button to focus
var aud;
function playonCtrl(text, audioid){
  aud = audioid;
  document.addEventListener('keydown', function(e) {
    console.log("qwe", e.key);
    if (e.ctrlKey && e.shiftKey && e.key == 'z' && document.activeElement == text) {
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
  if( $("#reasontolove").get(0).value == ""||
        $("#reasontohate").get(0).value == ""||
        $("#name").get(0).value == ""||
        $("#email").get(0).value == "" ||
        $("#technical_report").get(0).value == "") {
          alert(alert_msg);
          return false;
        }else return true;
}

function before_submit(){
  // if(!checkfinalform()) {
  //   return;
  // }
  document.getElementById('end_time').value = Date.now();
  // var answer1 = document.getElementsByClassName("ui-state")[0].lastChild.id;
  // var answer2 = document.getElementsByClassName("ui-state")[1].lastChild.id;
  // var answer3 = document.getElementsByClassName("ui-state")[2].lastChild.id;
  // var answer4 = document.getElementsByClassName("ui-state")[3].lastChild.id;

  // document.getElementById('answer1').value = answer1;
  // document.getElementById('answer2').value = answer2;
  // document.getElementById('answer3').value = answer3;
  // document.getElementById('answer4').value = answer4;

  // console.log(answer1);
  // console.log(answer2);
  // console.log(answer3);
  // console.log(answer4);
  
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
}
function audio_play(key){
  if(start_times[key]==="0")start_times[key]=Date.now();
  play_times[key]=play_times[key]+1;
}


function hideCaptcha1(){
  if(count == 0 && checkPro1_1()){
    document.getElementById("instance1_1").style.display = "none";
    document.getElementById("instance1_2").style.display = "block";
    document.getElementById("instance1_3").style.display = "none";
    document.getElementById("sub1").innerHTML="第二題";
    count += 1;
    focustext("pro1_2");
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
    focustext("pro1_3");
  }
  else return;
}

function hideCaptcha2(){
  if(count == 0 && checkPro2_1()){
    document.getElementById("instance2_1").style.display = "none";
    document.getElementById("instance2_2").style.display = "block";
    document.getElementById("instance2_3").style.display = "none";
    document.getElementById("sub2").innerHTML="第二題";
    count += 1;
    focustext("pro2_2");
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
    focustext("pro2_3");
  }
  else return;
}

function hideCaptcha3(){
  if(count == 0 && checkPro3_1()){
    document.getElementById("instance3_1").style.display = "none";
    document.getElementById("instance3_2").style.display = "block";
    document.getElementById("instance3_3").style.display = "none";
    document.getElementById("sub3").innerHTML="第二題";
    count += 1;
    focustext("pro3_2");
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
    focustext("pro3_3");
  }
  else return;
}

function hideCaptcha4(){
  if(count == 0 && checkPro4_1()){
    document.getElementById("instance4_1").style.display = "none";
    document.getElementById("instance4_2").style.display = "block";
    document.getElementById("instance4_3").style.display = "none";
    document.getElementById("sub4").innerHTML="第二題";
    count += 1;
    focustext("pro4_2");
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
    focustext("pro4_3");
  }
  else return;
}


$(document).on("keypress", "input", function (e) {
  var code = e.keyCode || e.which;
  if (code == 13) {
    e.preventDefault();
    return false;
  }
});

var alert_msg = "請確認回答了所有（*必填）問題！";
var alert_digit = "請確認輸入答案為六位數字";
var alert_play_time = "請確實作答完畢再送出答案";

function checkPro0() {
  var audio = document.getElementById('0_1');
  audioStop(audio);
  var input = $("#pro0").get(0).value;
  if(!input) {
    alert(alert_msg);
    console.log($("#pro0").get(0).value);
    return false;
  }else if (!checkDigit(input)){
    alert(alert_digit);
    return false;
  }else return true;
}
function checkPro1_1() {
  var audio = document.getElementById('1_1');
  audioStop(audio);
  var input = $("#pro1_1").get(0).value;
  if(!input) {
    alert(alert_msg);
    console.log($("#pro1_1").get(0).value);
    return false;
  }else if (!checkDigit(input)){
    alert(alert_digit);
    return false;
  }else if (play_times['11']==0){
    alert(alert_play_time);
    return false;
  }else return true;
}
function checkPro1_2() {
  var audio = document.getElementById('1_2');
  audioStop(audio);
  var input = $("#pro1_2").get(0).value;
  if(!input) {
    alert(alert_msg);
    console.log($("#pro1_2").get(0).value);
    return false;
  }else if (!checkDigit(input)){
    alert(alert_digit);
    return false;
  }else if (play_times['12']==0){
    alert(alert_play_time);
    return false;
  }else return true;
}
function checkPro1_3(){
  var audio = document.getElementById('1_3');
  audioStop(audio);
  var input = $("#pro1_3").get(0).value;
  if(!input) {
    alert(alert_msg);
    console.log($("#pro1_3").get(0).value);
    return false;
  }else if (!checkDigit(input)){
    alert(alert_digit);
    return false;
  }else if (play_times['13']==0){
    alert(alert_play_time);
    return false;
  }else return true;
}
  

function checkPro2_1() {
  var audio = document.getElementById('2_1');
  audioStop(audio);
  var input = $("#pro2_1").get(0).value;
  if(!input) {
    alert(alert_msg);
    console.log($("#pro2_1").get(0).value);
    return false;
  }else if (!checkDigit(input)){
    alert(alert_digit);
    return false;
  }else if (play_times['21']==0){
    alert(alert_play_time);
    return false;
  }else return true;
}
function checkPro2_2() {
  var audio = document.getElementById('2_2');
  audioStop(audio);
  var input = $("#pro2_2").get(0).value;
  if(!input) {
    alert(alert_msg);
    console.log($("#pro2_2").get(0).value);
    return false;
  }else if (!checkDigit(input)){
    alert(alert_digit);
    return false;
  }else if (play_times['22']==0){
    alert(alert_play_time);
    return false;
  }else return true;
}
function checkPro2_3(){
  var audio = document.getElementById('2_3');
  audioStop(audio);
  var input = $("#pro2_3").get(0).value;
  if(!input) {
    alert(alert_msg);
    console.log($("#pro2_3").get(0).value);
    return false;
  }else if (!checkDigit(input)){
    alert(alert_digit);
    return false;
  }else if (play_times['23']==0){
    alert(alert_play_time);
    return false;
  }else return true;
}


function checkPro3_1() {
  var audio = document.getElementById('3_1');
  audioStop(audio);
  var input = $("#pro3_1").get(0).value;
  if(!input) {
    alert(alert_msg);
    console.log($("#pro3_1").get(0).value);
    return false;
  }else if (!checkDigit(input)){
    alert(alert_digit);
    return false;
  }else if (play_times['31']==0){
    alert(alert_play_time);
    return false;
  }else return true;
}
function checkPro3_2() {
  var audio = document.getElementById('3_2');
  audioStop(audio);
  var input = $("#pro3_2").get(0).value;
  if(!input) {
    alert(alert_msg);
    console.log($("#pro3_2").get(0).value);
    return false;
  }else if (!checkDigit(input)){
    alert(alert_digit);
    return false;
  }else if (play_times['32']==0){
    alert(alert_play_time);
    return false;
  }else return true;
}
function checkPro3_3(){
  var audio = document.getElementById('3_3');
  audioStop(audio);
  var input = $("#pro3_3").get(0).value;
  if(!input) {
    alert(alert_msg);
    console.log($("#pro3_3").get(0).value);
    return false;
  }else if (!checkDigit(input)){
    alert(alert_digit);
    return false;
  }else if (play_times['33']==0){
    alert(alert_play_time);
    return false;
  }else return true;
}

function checkPro4_1() {
  var audio = document.getElementById('4_1');
  audioStop(audio);
  var input = $("#pro4_1").get(0).value;
  if(!input) {
    alert(alert_msg);
    console.log($("#pro4_1").get(0).value);
    return false;
  }else if (!checkDigit(input)){
    alert(alert_digit);
    return false;
  }else if (play_times['41']==0){
    alert(alert_play_time);
    return false;
  }else return true;
}
function checkPro4_2() {
  var audio = document.getElementById('4_2');
  audioStop(audio);
  var input = $("#pro4_2").get(0).value;
  if(!input) {
    alert(alert_msg);
    console.log($("#pro4_2").get(0).value);
    return false;
  }else if (!checkDigit(input)){
    alert(alert_digit);
    return false;
  }else if (play_times['42']==0){
    alert(alert_play_time);
    return false;
  }else return true;
}
function checkPro4_3(){
  var audio = document.getElementById('4_3');
  audioStop(audio);
  var input = $("#pro4_3").get(0).value;
  if(!input) {
    alert(alert_msg);
    console.log($("#pro4_3").get(0).value);
    return false;
  }else if (!checkDigit(input)){
    alert(alert_digit);
    return false;
  }else if (play_times['43']==0){
    alert(alert_play_time);
    return false;
  }else return true;
}

function checkfeedback1(){
  var likert_fb1_1 = $("input[name=likert_fb1_1]:checked").length;
  var likert_fb1_2 = $("input[name=likert_fb1_2]:checked").length;

  if(!($("#text_fb1_1").get(0).value && $("#text_fb1_2").get(0).value && likert_fb1_1 && likert_fb1_2)) {
    alert(alert_msg);
    return false;
  }else return true;
}

function checkfeedback2(){
  var likert_fb2_1 = $("input[name=likert_fb1_1]:checked").length;
  var likert_fb2_2 = $("input[name=likert_fb1_2]:checked").length;
  if(!($("#text_fb2_1").get(0).value && $("#text_fb2_2").get(0).value && likert_fb2_1 && likert_fb2_2)) {
    alert(alert_msg);
    return false;
  }else return true;
}

function checkfeedback3(){
  var likert_fb3_1 = $("input[name=likert_fb1_1]:checked").length;
  var likert_fb3_2 = $("input[name=likert_fb1_2]:checked").length;
  if(!($("#text_fb3_1").get(0).value && $("#text_fb3_2").get(0).value && likert_fb3_1 && likert_fb3_2)) {
    alert(alert_msg);
    return false;
  }else return true;
}

function checkfeedback4(){
  var likert_fb4_1 = $("input[name=likert_fb1_1]:checked").length;
  var likert_fb4_2 = $("input[name=likert_fb1_2]:checked").length;
  if(!($("#text_fb4_1").get(0).value && $("#text_fb4_2").get(0).value && likert_fb4_1 && likert_fb4_2)) {
    alert(alert_msg);
    return false;
  }else return true;
}
function audioStop(input_audio){
  input_audio.pause();
  input_audio.currentTime = 0;
}
function checkDigit(input_answer){
  if (input_answer.length != 6 || !/^\d+$/.test(input_answer)){
    return false;
  }else return true;
}

//jQuery time
(function($) {
  var current_fs, next_fs, previous_fs; //fieldsets
  var left, opacity, scale; //fieldset properties which we will animate
  var animating; //flag to prevent quick multi-click glitches
  $(".next").click(function() {
    if (animating) return false;
    animating = true;

    current_fs = $(this).parent();
    next_fs = $(this).parent().next();
    console.log(this.id);

    if(this.id === 'pronext0') {
      var practice = $("#pro0").get(0).value;
      if(!(checkPro0() && checkDigit(practice) && play_times['0'] != 0)) {
        animating = false;
        return;
      }
    }else if(this.id === 'pronext1') {
      if(!checkPro1_3()) {
        animating = false;
        return;
      }
    }else if(this.id === 'pronext2') {
      if(!checkPro2_3()) {
        animating = false;
        return;
      }
    }else if(this.id === 'pronext3') {
      if(!checkPro3_3()) {
        animating = false;
        return;
      }
    }else if(this.id === 'pronext4') {
      if(!checkPro4_3()) {
        animating = false;
        return;
      }
    } 

    //activate next step on progressbar using the index of next_fs
    $("#progressbar li").eq($("fieldset").index(next_fs) + 1).addClass("active");

    //show the next fieldset
    next_fs.show();
    if(this.id === 'pronext0') focustext("pro1_1");
    else if (this.id === "feedbacknext1")focustext("pro2_1");
    else if (this.id === "feedbacknext2")focustext("pro3_1");
    else if (this.id === "feedbacknext3")focustext("pro4_1");
    
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
