document.addEventListener("DOMContentLoaded", function() {

    

    function save_to_localstorage(order_list){
        localStorage.setItem("order_list", JSON.stringify(order_list));
    }
        

    



    let add_to_card_btns = document.getElementsByClassName("add-to-card")

    for (let i = 0; i < add_to_card_btns.length; i++) {
        add_to_card_btns[i].addEventListener('click', handleClick);
      }

    function create_order_list_row(foodName, foodCount, foodPrice){

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
        priceDiv.textContent = foodPrice + "T";

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
        addImg.setAttribute("alt", "add btn");
        addImg.setAttribute("width", "15px");

        addDiv.appendChild(addImg);

        // Create the inner div with the id "ocount" and set its content
        var countDiv = document.createElement("div");
        countDiv.setAttribute("id", "ocount");
        countDiv.textContent = foodCount;

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
        // console.log(order_list[foodName])
        if (order_list[foodName] === undefined){
            // console.log("food added to list")
            order_list[foodName] = {"count": 1, "price": foodPrice}
            order_list["total"] += order_list[foodName].price
            document.getElementById("totalPrice").innerText = order_list["total"]
            // console.log(order_list)
            create_order_list_row(foodName, 1, foodPrice)
        }
        else if (order_list[foodName] === foodName & order_list[foodName].count === 0){

            console.log("food recreated")
            
            order_list[foodName].count += 1
            order_list["total"] += order_list[foodName].price
            document.getElementById("totalPrice").innerText = order_list["total"]
            // console.log(order_list)
            create_order_list_row(foodName, 1, foodPrice)
        }
        else{
            list = document.getElementsByClassName("card")[0]
            
            for (let i = 0; i < list.children.length; i++) {
                if (list.children[i].children[0].children[0].innerText === foodName ){
                    list.children[i].children[1].children[1].innerText = Number(list.children[i].children[1].children[1].innerText) + 1
                    order_list[foodName].count += 1
                    order_list["total"] += order_list[foodName].price
                    document.getElementById("totalPrice").innerText = order_list["total"]
                    // console.log(order_list)
                }
              }
        }

        let add_btns = document.getElementsByClassName("add")
        let remove_btns = document.getElementsByClassName("remove")

        for (let i = 0; i < add_btns.length; i++) {
            // console.log(addButtons[i])
            add_btns[i].addEventListener('click', manageItem);
            remove_btns[i].addEventListener('click', manageItem);
          }
          save_to_localstorage(order_list)
            }

        function manageItem(event){
            
            if (event.target.className === "add"){
                food = event.target.parentNode.parentNode.children[0].children[0].innerText
                add(event, food)
            } else if (event.target.parentNode.className === "add"){
                food = event.target.parentNode.parentNode.parentNode.children[0].children[0].innerText
                add(event, food)
            }

            if (event.target.className === "remove"){
                food = event.target.parentNode.parentNode.children[0].children[0].innerText
                remove(event, food)
            }
            if (event.target.parentNode.className === "remove"){
                food = event.target.parentNode.parentNode.parentNode.children[0].children[0].innerText
                remove(event, food)
            }

            function add(event, food){
                order_list[food].count += 1
                order_list["total"] += order_list[food].price
                document.getElementById("totalPrice").innerText = order_list["total"]

                if (event.target.localName === "img" & event.target.parentNode.className === "add"){
                    event.target.parentNode.parentNode.children[1].innerText = Number(event.target.parentNode.parentNode.children[1].innerText) + 1
                }
                else if (event.target.className === "add"){
                    event.target.parentNode.children[1].innerText = Number(event.target.parentNode.children[1].innerText) + 1
                }

                
            }

            function remove(event, food){
                order_list[food].count -= 1
                order_list["total"] -= order_list[food].price
                document.getElementById("totalPrice").innerText = order_list["total"]

                if (event.target.className === "remove"){
                    if (event.target.parentNode.children[1].innerText != "1"){
                        event.target.parentNode.children[1].innerText = Number(event.target.parentNode.children[1].innerText) - 1
                    } else {
                        event.target.parentNode.parentNode.remove()
                        delete order_list[food]
                    }
                }
                else if (event.target.parentNode.className === "remove"){
                    if (event.target.parentNode.parentNode.children[1].innerText != "1"){
                        event.target.parentNode.parentNode.children[1].innerText = Number(event.target.parentNode.parentNode.children[1].innerText) - 1
                    } else {
                        event.target.parentNode.parentNode.parentNode.remove()
                    }
                }
            }

            save_to_localstorage(order_list)
        }


        document.getElementById("clear").onclick = function(){
            for (let key in order_list) {
                delete order_list[key];
              }
            order_list["total"] = 0
            document.getElementById("totalPrice").innerText = 0

            while (document.getElementsByClassName("card")[0].firstChild){
                document.getElementsByClassName("card")[0].removeChild(document.getElementsByClassName("card")[0].firstChild)
            }
            save_to_localstorage(order_list)
        }
    
        if (localStorage.getItem("order_list")) {
            // Object exists, retrieve it in a variable
            var order_list = JSON.parse(localStorage.getItem("order_list"));
            for (let key in order_list) {
                if (key === "total"){
                    document.getElementById("totalPrice").innerText = order_list[key]
                }
                else{
                    create_order_list_row(key, order_list[key].count, order_list[key].price)
                }
                
              }
        }
        else {
            var order_list = {"total": 0};
        }

        let add_btns = document.getElementsByClassName("add")
    let remove_btns = document.getElementsByClassName("remove")

    for (let i = 0; i < add_btns.length; i++) {
        // console.log(addButtons[i])
        add_btns[i].addEventListener('click', manageItem);
        remove_btns[i].addEventListener('click', manageItem);
        }

        

    function manageItem(event){
        
        if (event.target.className === "add"){
            food = event.target.parentNode.parentNode.children[0].children[0].innerText
            add(event, food)
        } else if (event.target.parentNode.className === "add"){
            food = event.target.parentNode.parentNode.parentNode.children[0].children[0].innerText
            add(event, food)
        }

        if (event.target.className === "remove"){
            food = event.target.parentNode.parentNode.children[0].children[0].innerText
            remove(event, food)
        }
        if (event.target.parentNode.className === "remove"){
            food = event.target.parentNode.parentNode.parentNode.children[0].children[0].innerText
            remove(event, food)
        }

        function add(event, food){
            order_list[food].count += 1
            order_list["total"] += order_list[food].price
            document.getElementById("totalPrice").innerText = order_list["total"]

            if (event.target.localName === "img" & event.target.parentNode.className === "add"){
                event.target.parentNode.parentNode.children[1].innerText = Number(event.target.parentNode.parentNode.children[1].innerText) + 1
            }
            else if (event.target.className === "add"){
                event.target.parentNode.children[1].innerText = Number(event.target.parentNode.children[1].innerText) + 1
            }

            
        }

        function remove(event, food){
            order_list[food].count -= 1
            order_list["total"] -= order_list[food].price
            document.getElementById("totalPrice").innerText = order_list["total"]

            if (event.target.className === "remove"){
                if (event.target.parentNode.children[1].innerText != "1"){
                    event.target.parentNode.children[1].innerText = Number(event.target.parentNode.children[1].innerText) - 1
                } else {
                    event.target.parentNode.parentNode.remove()
                    delete order_list[food]
                }
            }
            else if (event.target.parentNode.className === "remove"){
                if (event.target.parentNode.parentNode.children[1].innerText != "1"){
                    event.target.parentNode.parentNode.children[1].innerText = Number(event.target.parentNode.parentNode.children[1].innerText) - 1
                } else {
                    event.target.parentNode.parentNode.parentNode.remove()
                }
            }
        }

        save_to_localstorage(order_list)
    }

});