
//헤더 스크롤
function windowScroll() {
    //기본
    if ($( window ).scrollTop() > 10) {
        
        $( '.header' ).addClass('scroll');
        
    } else if ($( document ).scrollTop() <= 10) {
        
        $( '.header' ).removeClass('scroll');
    }
    //메인페이지
    if ($(window).find('.mainPage').length < 1 && $( window ).scrollTop() < 200) {
        
        $( '.mainPage .header' ).removeClass('scroll');
        
    } else if ($(window).find('.mainPage').length < 1 && $( window ).scrollTop() >= 200) {
        
        $( '.mainPage .header' ).addClass('scroll');
    }
}

//헤더 GNB 버튼
function headerGnb() {
    
    $('.gnbWp .gnb-menu .menuBtn').click( function() {

        $(this).closest('.gnb-menu').find('.menuBtn').removeClass('active');
        $(this).addClass('active');
        
    });
}

//사이드 메뉴
function sideMenuShow() {
            
    $('.header .side-menuBtn').click( function() {

        $('.gnbWpper').addClass('open');
        $('.side-menu.dim').fadeIn(300);
        
    });

    $('.gnbWpper .gnb-h .close').click( function() {

        $('.gnbWpper').removeClass('open');
        $('.side-menu.dim').fadeOut(300);
        
    });
    
    if ($( window ).width() <= 414) {

        if ($('.gnbWpper').hasClass('open')) {
            
            $('.side-menu.dim').fadeOut(10);
        }

    } else {
        $('.gnbWpper').removeClass('open');
    }
}

//탭버튼 내용
function tabBtnCon() {

    $('.tabCon').hide();

    $('.tabCon').eq(0).show();

    $('.tabWp .tabBtn').click( function(){

        $(this).closest('.tabWp').find('.tabBtn').removeClass('active');

        $(this).addClass('active');

        var hrefs=$(this).attr('data-tab');

        $('.tabCon').hide();

        $('#' + hrefs).show();
    });
}

//리스트 페이지네이션
function pagiNation() {
    
    $('.pagiNation-Wp .pageAr .pageNum').click( function(){

        $(this).closest('.pageAr').find('.pageNum').removeClass('active');
        $(this).addClass('active');
        
    });
}

$(function(){
    //헤더 스크롤
    windowScroll();

    //헤더 GNB 버튼
    headerGnb();

    //사이드 메뉴
    sideMenuShow();
    
    //탭버튼 내용
    tabBtnCon();

    //리스트 페이지네이션
    pagiNation();
});

$(window).scroll(function (){
    
    //헤더 스크롤
    windowScroll();
});

$(window).resize(function (){
    
    //사이드 메뉴
    sideMenuShow();
});