// Swiper
var swiper = new Swiper(".popular-content", {
  slidesPerView: 1,
  spaceBetween: 10,
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
  autoplay: {
    delay: 5000,
    disableOnInteraction: false,
  },
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
  breakpoints: {
    280: {
      slidesPerView: 1,
      spaceBetween: 10,
    },
    320: {
      slidesPerView: 2,
      spaceBetween: 10,
    },
    510: {
      slidesPerView: 2,
      spaceBetween: 10,
    },
    758: {
      slidesPerView: 3,
      spaceBetween: 15,
    },
    900: {
      slidesPerView: 4,
      spaceBetween: 20,
    },
  },
});
// Show Video
let playButton = document.querySelector(".play-movie");
let video = document.querySelector(".video-container");
let myvideo = document.querySelector("#myvideo");
let closebtn = document.querySelector(".close-video");

playButton.onclick = () => {
  video.classList.add("show-video");
  // Auto Play When Click On Button
  myvideo.play();
};
closebtn.onclick = () => {
  video.classList.remove("show-video");
  // Pause On Close Video
  myvideo.pause();
  myvideo.pauseAllVideos() ;
};


var playlist = new Array("https://www.jolie-bobine.fr/wp-content/uploads/2022/08/RHN9q9J4pEHgJzCli2qZu88X3i708m.jpg","https://dondon.media/wp-content/uploads/2022/08/chronologie-one-piece-red.jpg","https://sm.ign.com/t/ign_fr/news/j/james-came/james-cameron-is-gonna-have-to-do-avatar-4-and-5-as-way-of-w_tt4q.1200.jpg","https://img.phonandroid.com/2021/07/loki-saison-deux.jpg","https://i.insider.com/61168ccb3dd01000199d9272?width=1136&format=jpeg","https://sumo.cdn.tv2.no/imageapi/v3/img/61e12cd3498e7819ca3ade40-1642147029103?location=identity16x9&quality=50&width=1280&height=720")
var videos = new Array("https://www.youtube.com/embed/mkomfZHG5q4","play-page/ONE PIECE FILM RED _ OFFICIAL TRAILER.mp4","https://www.youtube.com/embed/o5F8MOz_IDw","play-page/Marvel Studios' LOKI Season 2 - TEASER TRAILER _ Disney .mp4","play-page/Disney's Jungle Cruise _ Official Trailer.mp4","play-page/13 HOURS - Bande-annonce officielle (VF) [au cinéma le 30 mars 2016].mp4")
var names = new Array("BLACK ADAM","RED","AVATAR","LOKI",">Jungle Cruise","13H")
var acters= new Array("play-page/cast1.jpg","https://images.mubicdn.net/images/cast_member/338108/cache-353994-1531355853/image-w856.jpg?size=800x","https://fr.web.img5.acsta.net/c_310_420/pictures/20/01/03/09/47/3048844.jpg")
var actn=new Array("Dwayne Johnson","oda")
//represent changeContent
function F1(n) {
  localStorage.setItem('optionChosen', n);
  console.log(n);
}


function F2(){
  var opt = localStorage.getItem('optionChosen');

console.log(opt)
 document.getElementById('imo').src=playlist[opt];
 document.getElementById('myvideo').src=videos[opt];
 document.getElementById('oom').textContent=names[opt];
 document.getElementById('ACT1').src=acters[opt];
 document.getElementById('ACTN').textContent=actn[opt];

};
var vid = document.getElementById("myVideo");

function pauseVid() {
  vid.pause();
}