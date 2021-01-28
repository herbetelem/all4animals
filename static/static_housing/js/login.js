console.log(window.innerWidth);

const connection = document.querySelector(".a4_connection");
const login = document.querySelector(".a4_login_connection")
const registration = document.querySelector(".a4_registration")
let size = 0

connection.addEventListener('click',function(){
    connection.style.background = "white";
    registration.style.background = "cadetblue";
    window.innerWidth < 991 ? size = "80%" : size = "25%";
    document.querySelector(".a4_login").style.width = size;
    document.querySelector(".a4_login_connection").style.display = "block";
    document.querySelector(".a4_login_registration").style.display = "none";

})

registration.addEventListener('click',function(){
    connection.style.background = "cadetblue";
    registration.style.background = "white";
    window.innerWidth < 991 ? size = "80%" : size = "50%";
    document.querySelector(".a4_login").style.width = size;
    document.querySelector(".a4_login_connection").style.display = "none";
    document.querySelector(".a4_login_registration").style.display = "block";
})