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


function nutri(){
  var input = document.getElementById("autoComplete").value;
  console.log("searchInfo")
  $.ajax({
    type: "POST",
    url: "/nutri",
    data: { name: input },
    success: function (recs) {
      let recipe = [
        {
        Cuisine: recs[0][0],
        Recipe: recs[0][1],
        Ingredients: recs[0][2],
        Calories: recs[0][3],
        recipe_url: recs[0][4],
        },
        {
          Cuisine: recs[1][0],
          Recipe: recs[1][1],
          Ingredients: recs[1][2],
          Calories: recs[1][3],
          recipe_url: recs[1][4],
          },
          {
            Cuisine: recs[2][0],
            Recipe: recs[2][1],
            Ingredients: recs[2][2],
            Calories: recs[2][3],
            recipe_url: recs[2][4],
            },
            {
              Cuisine: recs[3][0],
              Recipe: recs[3][1],
              Ingredients: recs[3][2],
              Calories: recs[3][3],
              recipe_url: recs[3][4],
              },
              {
                Cuisine: recs[4][0],
                Recipe: recs[4][1],
                Ingredients: recs[4][2],
                Calories: recs[4][3],
                recipe_url: recs[4][4],
                },
                {
                  Cuisine: recs[5][0],
                  Recipe: recs[5][1],
                  Ingredients: recs[5][2],
                  Calories: recs[5][3],
                  recipe_url: recs[5][4],
                  },
      ]
      for(let element of recipe){
        const row = document.getElementById("recipe_data");
        const outer = document.createElement("div");
        outer.classList.add('column');
        const para = document.createElement("div");
        para.classList.add('card');
        const node1 = document.createTextNode("Cuisine: " + element.Cuisine + "\n");
        const node2 = document.createTextNode("Recipe: " + element.Recipe+ "\n");
        const node3 = document.createTextNode("Ingredients: " + element.Ingredients + "\n");
        const node4 = document.createTextNode("Calories: " + element.Calories);
        const node5 = document.createTextNode("Recipe URL: " + element.recipe_url);
        para.appendChild(node1);
        para.appendChild(document.createElement("br"));
        para.appendChild(node2);
        para.appendChild(document.createElement("br"));
        para.appendChild(node3);
        para.appendChild(document.createElement("br"));
        para.appendChild(node4);
        para.appendChild(document.createElement("br"));
        para.appendChild(node5);
        para.appendChild(document.createElement("br"));
        outer.appendChild(para)
        row.appendChild(outer);
      }

    }

  })
}
function searchInfo(){
  var input = document.getElementById("autoComplete").value;
  console.log("searchInfo")
  $.ajax({
    type: "POST",
    url: "/search_info",
    data: { recipe: input },
    success: function (recs) {
      let recipe = [
        {
        Cuisine: recs[0][0],
        Recipe: recs[0][1],
        Ingredients: recs[0][2],
        Calories: recs[0][3],
        recipe_url: recs[0][4]
        },
      ]
      console.log(recipe)
      for(let element of recipe){
        const row = document.getElementById("recipe_data");
        const outer = document.createElement("div");
        outer.classList.add('column');
        const para = document.createElement("div");
        para.classList.add('card');
        const node1 = document.createTextNode("Cuisine: " + element.Cuisine + "\n");
        const node2 = document.createTextNode("Recipe: " + element.Recipe+ "\n");
        const node3 = document.createTextNode("Ingredients: " + element.Ingredients + "\n");
        const node4 = document.createTextNode("Calories: " + element.Calories);
        const node5 = document.createTextNode("Recipe URL: " + element.recipe_url);
        para.appendChild(node1);
        para.appendChild(document.createElement("br"));
        para.appendChild(node2);
        para.appendChild(document.createElement("br"));
        para.appendChild(node3);
        para.appendChild(document.createElement("br"));
        para.appendChild(node4);
        para.appendChild(document.createElement("br"));
        para.appendChild(node5);
        para.appendChild(document.createElement("br"));
        outer.appendChild(para)
        row.appendChild(outer);
      }
    },
  });
}