document.addEventListener("DOMContentLoaded", function() {
    let buttons = document.getElementsByClassName("categories")
    for (let i = 0; i < buttons.length; i++) {
        buttons[i].addEventListener('click', handleClick);
      }
    var currentURL = window.location.href;
    function handleClick(event) {
      for (let i = 0; i < buttons.length; i++) {
        if (buttons[i].classList.contains("btn-primary")){
          buttons[i].classList.remove("btn-primary")
        }else{}
      }
      console.log(event.target)
      const clickedButton = event.target.textContent;
      var newURL = currentURL.split('?')[0] + '?' + 'category=' + clickedButton;
    window.location.href = newURL;
      }
  });