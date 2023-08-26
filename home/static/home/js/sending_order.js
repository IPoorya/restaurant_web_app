document.addEventListener("DOMContentLoaded", function() {


    if (localStorage.getItem("order_list")) {
        // Object exists, retrieve it in a variable
        var order_list = JSON.parse(localStorage.getItem("order_list"));
    }
    else {
        var order_list = {"total": 0};
    }


    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== "") {
          const cookies = document.cookie.split(";");
          for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + "=")) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
            }
          }
        }
        return cookieValue;
      }

    
    document.getElementById("buy").onclick = function(){
        if (document.getElementById("page").innerText === "ثبت سفارش"){
            document.getElementsByClassName("card")[0].classList.toggle("active")
            document.getElementsByClassName("user_info")[0].classList.toggle("active")
            document.getElementById("page").innerText = "پرداخت"
            document.getElementById("clear").innerText = "بازگشت"
        }
        else if (document.getElementById("page").innerText === "پرداخت"){
            console.log(JSON.stringify(order_list))

            order_list["name"] = document.getElementsByTagName("input")[0].value 
            order_list["phone_number"] = document.getElementsByTagName("input")[1].value 
            order_list["postal_code"] = document.getElementsByTagName("input")[2].value 
            order_list["address"] = document.getElementById("address").value

            $.ajax({
                url: "/checking_order/",
                type: "POST",
                dataType: "json",
                data: JSON.parse(JSON.stringify(order_list)),
                headers: {
                "X-Requested-With": "XMLHttpRequest",
                "X-CSRFToken": getCookie("csrftoken"),  // don't forget to include the 'getCookie' function
                },
                success: (data) => {
                console.log(data);
                },
                error: (error) => {
                console.log(error);
                }
            });
        }



        

      }





});