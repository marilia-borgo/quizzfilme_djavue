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
    find: (req, res) => {
      const loggedUser = accounts.loginRequired(req, res);
      if (!loggedUser) {
        return;
      }
      const { id } = req.params;
      if (id != undefined) {
        const resultado = data.resultado.find((t) => t.id == id);
        if (!resultado || resultado.userId != loggedUser.id) {

          res.status(404).end();
          return;
        }
        res.send(resultado);
        return;
      }
      const response = {
        todos: data.resultado.filter((t) => t.userId == loggedUser.id),
      }
      res.send(response);
    },
};