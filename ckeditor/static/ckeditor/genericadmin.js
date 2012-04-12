activate_content_type_select = function(){
    $ = django.jQuery;  
    $("select.content_type").change(function (){  
        console.log($(".lookup_button")); 
        $(".lookup_button").attr("href",CKEDITOR.config.content_embed_urls[$(this).val()]);    
    });
}