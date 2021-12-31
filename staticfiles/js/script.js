$(function(){

    $('.btn').hide().delay(2000).fadeIn(2000);
    $('.pop-div').hover( function(){
        $('.pop-up').html(
            "<span class='el-span'>"
             + "💡<i>Tip: \"click any title to navigate to the portfolio-project!\"" 
             + "</i></span>");
    },
    function(){
        $('.el-span').remove();
    })
    


});