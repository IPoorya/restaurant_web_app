document.addEventListener("DOMContentLoaded", function() {
    let buttons = document.getElementsByClassName("add-to-card")

    for (let i = 0; i < buttons.length; i++) {
        buttons[i].addEventListener('click', handleClick);
      }

    function create_element(foodName, foodPrice){
        // Create the outer div element with the class "o-row"
        var outerDiv = document.createElement("div");
        outerDiv.setAttribute("class", "o-row");

        // Create the inner div with the id "odetail" and its contents
        var detailDiv = document.createElement("div");
        detailDiv.setAttribute("id", "odetail");

        // Create the inner div with the id "oname" and set its content
        var nameDiv = document.createElement("div");
        nameDiv.setAttribute("id", "oname");
        nameDiv.textContent = foodName;

        // Create the inner div with the id "oprice" and set its content
        var priceDiv = document.createElement("div");
        priceDiv.setAttribute("id", "oprice");
        priceDiv.textContent = foodPrice;

        // Append the inner divs to the "odetail" div
        detailDiv.appendChild(nameDiv);
        detailDiv.appendChild(priceDiv);

        // Create the inner div with the id "obtns" and its contents
        var btnsDiv = document.createElement("div");
        btnsDiv.setAttribute("id", "obtns");

        // Create the inner div with the class "add" and its contents
        var addDiv = document.createElement("div");
        addDiv.setAttribute("class", "add");

        var addImg = document.createElement("img");
        addImg.setAttribute("src", "static/img/plus-line-icon.webp");
        addImg.setAttribute("alt", "delete btn");
        addImg.setAttribute("width", "15px");

        addDiv.appendChild(addImg);

        // Create the inner div with the id "ocount" and set its content
        var countDiv = document.createElement("div");
        countDiv.setAttribute("id", "ocount");
        countDiv.textContent = "1";

        // Create the inner div with the class "remove" and its contents
        var removeDiv = document.createElement("div");
        removeDiv.setAttribute("class", "remove");

        var removeImg = document.createElement("img");
        removeImg.setAttribute("src", "static/img/minus-line-icon.webp");
        removeImg.setAttribute("alt", "delete btn");
        removeImg.setAttribute("width", "15px");

        removeDiv.appendChild(removeImg);

        // Append the inner divs to the "obtns" div
        btnsDiv.appendChild(addDiv);
        btnsDiv.appendChild(countDiv);
        btnsDiv.appendChild(removeDiv);

        // Append the inner divs to the outer div
        outerDiv.appendChild(detailDiv);
        outerDiv.appendChild(btnsDiv);

        var targetDiv = document.querySelector(".card");
        targetDiv.appendChild(outerDiv);
    }

    function handleClick(event) {
        var foodName = event.target.parentNode.children[2].children[0].children[0].innerText;
        var foodPrice = event.target.parentNode.children[2].children[0].children[1].innerText;
        foodPrice = parseInt(foodPrice, 10)
        // console.log(clickedButton)
        // Get the food name and price
        // var foodName = document.querySelector(".title p:first-child").textContent;
        // var foodPrice = document.getElementById("food-price").textContent;
        // console.log("foodname: " + food_name)
        // console.log("foodprice: " + food_price)

        
        create_element(foodName, foodPrice)

        
            }


    


});