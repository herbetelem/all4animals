$( document ).ready(function() {
    $("td").click(function() {
        let days = $(this).attr('id');
        $('.a4_info_days p').html('La journée sélectioné est le ' + days + ' Janvier 2021');
    })
});