function onLoginClick() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) { // Thisis the callback function
            // Get the string data that the server sent us.
            const resultString = this.responseText;

            var resultObject = JSON.parse(resultString);

            if (resultObject.was_logged_in === false) {
                alert(resultObject.reason);
            } else {
                window.location.href = "{% url 'i_list_page' %}";
            }
        }
    }

    xhttp.open("POST", "{% url 'instrument_create_api' %}", true);
    xhttp.setRequestHeader("content-type", "application/x-www-form-urlencoded");
    const name = document.getElementById("name").value;
    xhttp.send("name="+name);
}

function onBackClick() {
    window.location.href = "{% url 'i_list_page' %}";
}
