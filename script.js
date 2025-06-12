const getEndpoint = "http://localhost:8000/users"
const postEndpoint = "http://localhost:8000/insert_user"

const getDataButton = document.querySelector(".get")
const sectiondata = document.querySelector(".data")

const postDataButton = document.querySelector(".submit")
const userData = document.querySelector(".user")
const passwordData = document.querySelector(".password")

getDataButton.addEventListener("click", function(){
    fetch(getEndpoint)
    .then(res => res.json())
    .then(res => renderGet(res))
})

postDataButton.addEventListener("click", function(e){
    e.preventDefault()
    
    console.log("sending dataaa",userData.value, passwordData.value)
    if(userData.value != "" && passwordData.value != ""){

        fetch(postEndpoint, {
            method: "POST",
            headers: {
                "Content-type": "application/json" 
            },
            body: JSON.stringify({usuario: userData.value, password: passwordData.value})
        })


    }
})

function renderGet(data){
    data.forEach(element => {
        const div = document.createElement("div")
        const usuario = document.createElement("p")
        const password = document.createElement("p")

        usuario.textContent = element.usuario
        password.textContent = element.password

        div.appendChild(usuario)
        div.appendChild(password)
        sectiondata.appendChild(div)
    });
}