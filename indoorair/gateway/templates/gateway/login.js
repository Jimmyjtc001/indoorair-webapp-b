function onLoginClick() {
  const usernameObj = document.getElementById("username");
  const username = usernameObj.value;
  console.log(username);
  const passwordObj = document.getElementById("password");
  const password = passwordObj.value;
  console.log(password);

  var xhttp = new XMLHttpRequest();
   xhttp.onreadystatechange = function() {
       if (this.readyState == 4 && this.status == 200) {
        const loginObject = JSON.parse(this.responseText);
        if(loginObject.was_successful === true){
          window.location.href = "/dashboard";
      }
      else {
        alert(loginObject.reason);

      }
}
}
  xhttp.open("POST", "/api/login", true);
  xhttp.setRequestHeader("content-type", "application/x-www-form-urlencoded");
  xhttp.send("&username="+username+"&password="+password);
}
