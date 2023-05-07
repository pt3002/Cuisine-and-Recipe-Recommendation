// Create a "close" button and append it to each list item
var myNodelist = document.getElementsByTagName("LI");
var i;
for (i = 0; i < myNodelist.length; i++) {
  var span = document.createElement("SPAN");
  var txt = document.createTextNode("\u00D7");
  span.className = "close";
  span.appendChild(txt);
  myNodelist[i].appendChild(span);
}

// Click on a close button to hide the current list item
var close = document.getElementsByClassName("close");
var i;
for (i = 0; i < close.length; i++) {
  close[i].onclick = function () {
    var div = this.parentElement;
    div.style.display = "none";
  };
}

function generateTableHead(table, data) {
  let thead = table.createTHead();
  let row = thead.insertRow();
  for (let key of data) {
    let th = document.createElement("th");
    let text = document.createTextNode(key);
    th.appendChild(text);
    row.appendChild(th);
  }
}

function generateTable(table, data) {
  for (let element of data) {
    let row = table.insertRow();
    for (key in element) {
      let cell = row.insertCell();
      let text = document.createTextNode(element[key]);
      cell.appendChild(text);
    }
  }
}

// Click on Search Recipes button
function search() {
  var ingredients = [];

  for (i = 0; i < myNodelist.length; i++) {
    var lines = myNodelist[i].innerText;
    ingredients.push(
      lines.substring(lines.lastIndexOf("\n") + 1, -1).replace(/\n/g, "")
    );
  }
  console.log(ingredients);
  ing_str = ingredients.join("+");
  $.ajax({
    type: "POST",
    url: "/search_recipe_ingredients",
    data: { ing_array: ing_str },
    success: function (recs) {
      let recommended_recipes = [
        {
          Cuisine: recs[0][0],
          Recipe: recs[0][1],
          Ingredients: recs[0][2],
          Calories: recs[0][3],
        },
        {
          Cuisine: recs[1][0],
          Recipe: recs[1][1],
          Ingredients: recs[1][2],
          Calories: recs[1][3],
        },
        {
          Cuisine: recs[2][0],
          Recipe: recs[2][1],
          Ingredients: recs[2][2],
          Calories: recs[2][3],
        },
        {
          Cuisine: recs[3][0],
          Recipe: recs[3][1],
          Ingredients: recs[3][2],
          Calories: recs[3][3],
        },
        {
          Cuisine: recs[4][0],
          Recipe: recs[4][1],
          Ingredients: recs[4][2],
          Calories: recs[4][3],
        },
      ];

      let table = document.querySelector("table");
      let data = Object.keys(recommended_recipes[0]);
      generateTableHead(table, data);
      generateTable(table, recommended_recipes);
      console.log(recommended_recipes);
      window.scrollTo(0, document.body.scrollHeight);
    },
  });
}

// Add a "checked" symbol when clicking on a list item
var list = document.querySelector("ul");
list.addEventListener(
  "click",
  function (ev) {
    if (ev.target.tagName === "LI") {
      ev.target.classList.toggle("checked");
    }
  },
  false
);

// Create a new list item when clicking on the "Add" button
function newElement() {
  $("#table_of_items tr").remove();
  var li = document.createElement("li");
  var inputValue = document.getElementById("myInput").value;
  var t = document.createTextNode(inputValue);
  li.appendChild(t);
  if (inputValue === "") {
    alert("You must write something!");
  } else {
    document.getElementById("myUL").appendChild(li);
  }
  document.getElementById("myInput").value = "";

  var span = document.createElement("SPAN");
  var txt = document.createTextNode("\u00D7");
  span.className = "close";
  span.appendChild(txt);
  li.appendChild(span);

  for (i = 0; i < close.length; i++) {
    close[i].onclick = function () {
      var div = this.parentElement;
      div.style.display = "none";
    };
  }
}
