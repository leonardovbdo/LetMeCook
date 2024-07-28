var app = require('express')();
var http = require('http');
const { url } = require('inspector');
var server = http.Server(app)
var io = require('socket.io')(server);
var port = process.env.PORT || 3000;

const URL_ROBO = "http://localhost:5000/letmecook/response/";

app.get('/', function (req, res) {
  res.sendFile(__dirname + '/index.html');
});

getRespostaRobo = (msg) => {
  let data = '';

  http.get(URL_ROBO + msg, (resposta) => {
    resposta.on("data", (pedaco) => {
      data += pedaco;
    });

    resposta.on("end", () => {
      const obj = JSON.parse(data);

      if (obj.confianca >= 0.55) {
        io.emit('chat message', "LetMeCook: " + obj.resposta);
      } else {
        io.emit('chat message', "LetMeCook: ainda não sei responder esta pergunta, tente novamente mais tarde");
      }
    });
  });
}

io.on('connection', function (socket) {
  socket.on('chat message', function (msg) {
    io.emit('chat message', "você: " + msg);
    getRespostaRobo(msg);
  });
});

server.listen(port, function () {
  console.log('listening on *:' + port);
});
