function validateText() {
    var input = document.getElementById('txt').value;
    if (input == "") {
        console.log("event: " + event);
        event.preventDefault();
        alert("Must answer this question before moving on.");
        return false;
    }
    return true;
}

function validateFeedbackPro1() {
    var radiosQ1 = document.getElementsByName("likert_fb1_1");
    var radiosQ2 = document.getElementsByName("likert_fb1_2");
    var textQ3Q5 = document.getElementsByName("comment");
    var radiosQ4 = document.getElementsByName("likert_fb1_4");

    if (!checkRadios(radiosQ1) || !checkRadios(radiosQ2)
        || !checkRadios(radiosQ4) || !checkText(textQ3Q5)) {
        alert("Please complete all questions before continuing.");
        event.preventDefault();
        return false;
    }
    return true;
}

function checkRadios(arr) {
    console.log(arr);
    for (i = 0; i < 5; i++) {
        if (arr[i].checked) {
            return true;
        }
    }
    return false;
}

function checkText(arr) {
    for (i = 0; i < arr.length; i++) {
        if (arr[i].length < 1) {
            return false;
        }
    }
    return true;
}

function replaceForm() {
    var IDofForm = "text_submission";
    var IDofDivWithForm = "impression";
    var IDforReplacement = "for_replacement";

    if (validateText()) {
        //document.getElementById(IDofForm).submit();
        return true;
    } else {
        document.getElementById(IDofDivWithForm).innerHTML = document.getElementById(IDforReplacement).innerHTML;
    }
    return;
}

/*
function timeAudio() {
  var begin = new Date();
  var end;
  console.log("begin: " + begin)
  myAudio=document.getElementById('audio');
  //myAudio.addEventListener('onclick', function() {
  //  begin = new Date()
  //});
  myAudio.addEventListener('onended', function() {
    end = new Date();
  });
  totalTime = begin - end;
  alert(totalTime + "ms spent listening.");
}
*/

(function($) {
    var begin;
    var end;
    $(".audio").click('play', function(){
        // done playing
        begin = new Date();
        alert("began");
    });

    $(".audio").bind('ended', function(){
        // done playing
        end = new Date();
        alert("Player stopped");
        var total = end - begin;
        alert("time:" + total)
    });

})(jQuery);