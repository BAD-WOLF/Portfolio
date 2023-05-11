$('#btn-lang').on('click', function() {
    $('#list-lang').toggle('slow');
});

$("#btn-pttn-me").on("click", function(){
    $("#list-me").toggle("slow");
});

$("#btn-pttn-look").on("click", function(){
    $("#list-look").toggle("slow");
});

$("#img-me").on("click", function(){
    $(location).attr("href", "https://www.instagram.com/_theusnx_");
})

$("#img-me").attr("src", "https://mir-s3-cdn-cf.behance.net/project_modules/disp/bc54b7109204737.5fceb98ae45dc.jpg");
