import api from "./config.js"
import apiHelpers from "./helpers.js" 

export default {
addNewResultado: (resultado, user) => {
    return new Promise((resolve, reject) => {
    let a = JSON.stringify(user)
    api
        .post("/api/resultado/add", apiHelpers.dataToForm({ a, resultado }))
        .then((response) => {
        return resolve(response.data)
        })
        .catch((error) => {
        return reject(error)
        })
    })
},
getResultado: (user) => {
return new Promise((resolve, reject) => {
    api
    .get("/api/resultado/", user)
    .then((response) => {
        return resolve(response.data)
    })
    .catch((error) => {
        return reject(error)
    })
    })
}
}