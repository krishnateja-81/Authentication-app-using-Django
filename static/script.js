function validate() {
    var fname = document.getElementById("fname").value;
    var lname = document.getElementById("lname").value;
    var uname = document.getElementById("uname").value;
    var password = document.getElementById("password").value;
    var confirmpassword = document.getElementById("confirmpassword").value;

    var name = /^[A-Za-z]+$/;
    var username = /^[A-Za-z0-9]+$/;
 
    clearErrorMessages();

    var isValid = true;

    if (!name.test(fname)) {
        document.getElementById("fnameerr").innerHTML = "First name should only contain alphabets.";
        isValid = false;
    }

    if (!name.test(lname)) {
        document.getElementById("lnameerr").innerHTML = "Last name should only contain alphabets.";
        isValid = false;
    }

    if (!username.test(uname)) {
        document.getElementById("unameerr").innerHTML = "Username should only contain alphabets and numbers.";
        isValid = false;
    }

    if (password !== confirmpassword) {
        document.getElementById("passworderr1").innerHTML = "Password and Confirm Password do not match.";
        isValid = false;
    }
    if (password <6){
        document.getElementById('passworderr').innerHTML = "password is too short."
        isValid =false
    }


    return isValid;
}
function clearErrorMessages() {
    document.getElementById("fnameerr").innerHTML = "";
    document.getElementById("lnameerr").innerHTML = "";
    document.getElementById("unameerr").innerHTML = "";
    document.getElementById("passworderr").innerHTML = "";
    document.getElementById("passworderr1").innerHTML = "";
}
