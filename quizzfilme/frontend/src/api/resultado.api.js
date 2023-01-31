import api from "./config.js"
import apiHelpers from "./helpers.js" 

export default {
addNewResultado: (resultado) => {
    return new Promise((resolve, reject) => {
    api
        .post("/api/resultado/add", apiHelpers.dataToForm({ resultado }))
        .then((response) => {
        return resolve(response.data)
        })
        .catch((error) => {
        return reject(error)
        })
    })
},
}
