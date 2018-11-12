$(document).ready(function () {
    setTimeout(function () {
        swiper1();
        swiper2();
    }, 100)
})


// 轮播图
function swiper1() {
    var mySwiper1 = new Swiper('#topSwiper',{
        direction: 'horizontal',
        loop: true,
        speed: 500,
        autoplay: 500,
        pagination: '.swiper-pagination',
        control: true,
        }
    );
};


// 必买
function swiper2() {
    var mySwiper2 = new Swiper('#swiperMenu',{
        slidesPerView: 3,
        paginationClickable: true,
        spaceBetween: 2,
        loop: false,
        }
    );
};


