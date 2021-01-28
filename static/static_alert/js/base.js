$( document ).ready(function() {
    let logo_click = 0
    $('.a4_burger').click(function(){
        $(".a4_menu_show").toggle();
        if ( logo_click === 0) {
            logo_click = 1;
            $(".a4_logo-nav img").css( "height", "8vh" );
        }
        else {
            logo_click = 0;
            $(".a4_logo-nav img").css( "height", "16vh" );
        }
    });
});


