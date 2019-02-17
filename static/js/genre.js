$(document).ready(function(){
    var selectedGenre = "None";
    $("select.genreselect").change(function(){
        $(".teaser").removeClass("hidden");
   
        
        selectedGenre = $(this).children("option:selected").val();
        
        
        if (selectedGenre =="All") {
            $(".teaser").removeClass("hidden");
        }
        else {
        
               $(".teaser").addClass("hidden");
               $("." + selectedGenre).removeClass("hidden");
          
         
         
     }
    });
  
   
 });