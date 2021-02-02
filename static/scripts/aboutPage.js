var button = document.querySelector(".button");
var image = document.querySelector(".myPhoto");
var buttonWasClicked = false;

button.addEventListener("click", function() {
	if (!buttonWasClicked) {
		image.style.width = "400px";
		image.style.height = "650px";
		buttonWasClicked = true;
	} else {
		image.style.width = "200px";
		image.style.height = "325px";
		buttonWasClicked = false;
	}
}, false);