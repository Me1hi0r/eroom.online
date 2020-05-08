function back_video(name, muted=false){
    var videobackground = new $.backgroundVideo($('.video_place'), {
      "align": "centerY",
      "width": 1240,
      "height": 720,
      "path": "/static/engine/media/",
      "filename": name,
      "types": ["mov", "mp4"],
      "preload": true,
      "autoplay": false,
    });
  var v = $("#video_background")
  v.prop('loop', 'false');
  if (muted) v.prop('muted', 'muted');

  return document.body.querySelector('#video_background');
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


window.addEventListener('resize', function () {
  p = document.body.querySelector("#pict");
  p.height = window.innerHeight;
  p.width = window.innerWidth;
});

function video_ended(){
  video = document.body.querySelector('#video_background');
  video.onended = (event) => {
    play_pause();
    console.log('Video stopped either because 1) it was over, ' +
      'or 2) no further data is available.');
  }
}
