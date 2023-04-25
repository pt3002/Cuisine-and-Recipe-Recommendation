$(function() {
    console.log('HI')
    const source = document.getElementById('autoComplete');
    console.log(source);
    const inputHandler = function(e) {
        if(e.target.value==""){
          $('.search-button').attr('disabled', true);
        }
        else{
          $('.search-button').attr('disabled', false);
        }
      }
      source.addEventListener('input', inputHandler);
      $('.search-button').on('click', function(){
        var dish_name = document.getElementById('autoComplete').value;
        console.log(dish_name)
        similar_recipe(dish_name);
      });
});

function similar_recipe(dish_name){
    console.log('entered function')
    $.ajax({
        type: 'POST',
        url: "/similar_recipe",
        data:{'name':dish_name},
        success: function(recs){
            console.log(recs)
        }
    })
}