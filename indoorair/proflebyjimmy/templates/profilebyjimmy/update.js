function onUpdateProfileClick() {

  var xhttp = new XMLHttpRequest();
   xhttp.onreadystatechange = function() {
     if (this.readyState == 4 && this.status == 200) { // Thisis the callback function
         // Get the string data that the server sent us.
         if (this.readyState == 4 && this.status == 200) {

           document.getElementById('temp_average').innerHTML = this.responseText;

         }
       }
     }
       xhttp.open('POST', "{% url 'update_profile_api' %}", true);
       xhttp.setRequestHeader("content-type", "application/x-www-form-urlencoded");
       xhttp.send();

}
