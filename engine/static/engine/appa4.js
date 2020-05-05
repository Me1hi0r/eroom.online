function back_video(name, muted=false){
    var videobackground = new $.backgroundVideo($('.video_place'), {
      "align": "centerXY",
      "width": 1240,
      "height": 720,
      "path": "/static/engine/media/",
      "filename": name,
      "types": ["mov", "mp4"],
      "preload": true,
      "autoplay": false,
      "loop": true,
    });
    if (muted) $("#video_background").prop('muted', 'muted');
    var video = document.body.querySelector('#video_background')
//    video.style.height = '' + (parseInt(video.style.height) - 40) + 'px';
    return video
}

// "path": "/static/engine/media/",

function play_pause(){
    v = document.body.querySelector('#video_background');
    if (v.paused) v.play();
    else v.pause();
}

function start_timer(){
    var hour = new Date().getTime() + 3590000;
    $('#clock').countdown(hour)
    .on('update.countdown', function(event) {
      $(this).html(event.strftime('<span>%M:%S</span>'));
    }).on('finish.countdown', function(event) {
      $('#clock').html('Time out');
    });
}

$(document).ready(function () {
p = document.body.querySelector("#pict");
p.height = window.innerHeight;
p.width = window.innerWidth;
});

window.addEventListener('resize', function () {
  p = document.body.querySelector("#pict");
  p.height = window.innerHeight;
  p.width = window.innerWidth;
});