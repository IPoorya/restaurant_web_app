document.addEventListener("DOMContentLoaded", function() {
    let buttons = document.getElementsByClassName("categories")

    for (let i = 0; i < buttons.length; i++) {
        buttons[i].addEventListener('click', handleClick);
      }

    function handleClick(event) {
      const clickedButton = event.target.textContent;
      filterByCategory(clickedButton);
      for (let i = 0; i < buttons.length; i++) {
        const btn = buttons[i];
        if (btn.innerHTML === clickedButton){
          btn.classList.remove("btn-secondary")
          btn.classList.add("btn-primary");
        }
        else if(btn.classList.contains("btn-primary")){
          btn.classList.remove("btn-primary");
          btn.classList.add("btn-secondary");
        }
    }
      // --using query parameter and reload the page to get the desired data--
      // var newURL = currentURL.split('?')[0] + '?' + 'category=' + clickedButton;
      // window.location.href = newURL;

      }


      function filterByCategory(category) {
        // Get all objects initially rendered on the page
        const items = document.getElementsByClassName('item');
        
        // Hide objects that don't match the selected category
        for (let i = 0; i < items.length; i++) {
            const item = items[i];
            if (category === 'all' || item.classList.contains(category)) {
                item.style.display = 'block';
            } else {
                item.style.display = 'none';
            }
        }
    }

    filterByCategory('پیتزا');
  });