const express = require('express')
const webSocket = require('ws')
const http = require('http')

// initialize application
const app = express();


// create a http server
const httpServer = http.createServer(app);

const wss = new webSocket.WebSocketServer({ server: httpServer});

wss.on('connection', (socket)=> {
    console.log('connection make')

    // socket.on('message', (message)=> {
    //     console.log(message.toString())
    // })

    socket.on('message', (message)=> {
        wss.clients.forEach(client=> {
            if ( client.OPEN === client.readyState) {
                socket.send('Connection Alive')
            }
        })
    })
});

app.get('/', (req, res)=> {
    res.end('hello from server')
})
httpServer.listen(4000, ()=> {
    console.log('server is running...')
})

