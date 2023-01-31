const data = require("../data");
const accounts = require("./accounts");

function getMaxId(items) {
  return Math.max(...items.map((item) => item.id));
}

module.exports = {
    add: (req, res) => {
        const loggedUser = accounts.loginRequired(req, res);
        if (!loggedUser) {
          return;
        }
        const { resultado } = req.body;
        const id = getMaxId(data.resultado) + 1;
        const newResultado = {
          id,
          resultado,
          userId: loggedUser.id,
        };
        data.resultado.push(newResultado);
        res.send(newResultado);
      },
};