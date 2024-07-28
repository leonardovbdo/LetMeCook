const express = require('express');
const http = require('http');
const socketIo = require('socket.io');
const axios = require('axios');
const path = require('path');

const app = express();
const server = http.createServer(app);
const io = socketIo(server);
const port = 3000;

const URL = "http://localhost:5000/letmecook/response/";

// Serve arquivos estáticos do diretório "public"
app.use(express.static(path.join(__dirname, 'public')));

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'chat.html'));
});

const getRespostaRobo = async (msg) => {
  try {
    console.log(`Fetching response for message: ${msg}`);
    const response = await axios.get(`${URL}${encodeURIComponent(msg)}`);
    console.log(`Response received: ${JSON.stringify(response.data)}`);

    const data = response.data;
    if (data.confianca >= 0.55) {
      io.emit('chat message', `LetMeCook: ${data.response}`);
    } else {
      io.emit('chat message', "LetMeCook: ainda não sei responder esta pergunta, tente novamente mais tarde");
    }
  } catch (error) {
    console.error('Error fetching response from LetMeCook:', error.message);
    io.emit('chat message', "LetMeCook: ocorreu um erro ao buscar a resposta, tente novamente mais tarde");
  }
}

io.on('connection', (socket) => {
  socket.on('chat message', (msg) => {
    io.emit('chat message', `Você: ${msg}`);
    getRespostaRobo(msg);
  });
});

server.listen(port, () => {
  console.log(`Listening on *:${port}`);
});
