const express = require('express')
const webSocket = require('ws')
const http = require('http');
const { json } = require('stream/consumers');

// initialize application
const app = express();


// create a http server
const httpServer = http.createServer(app);

const wss = new webSocket.WebSocketServer({ server: httpServer});

// create a room
const rooms = new Map();
console.log('Socket Before: ', rooms)

wss.on('connection', (socket)=> {

    socket.send('Connection ban gya ji')

    socket.on('message', (message)=> {
        const data = JSON.parse(message.toString());

        // join
        if ( data.type === 'join') {
            // is room exits
            if (!rooms.has(data.rooms)) {
                // create room
                rooms.set(data.rooms, new Set());
            }
            // join
            rooms.get(data.rooms).add(socket);
            console.log('Socket After: ', rooms)
        }
    })

    // disconnection handler
    socket.on('close', ()=> {
        socket.send('connection hat gya ji')
    })

    // socket.on('message', (message)=> {
    //     wss.clients.forEach(client=> {
    //         if ( client.OPEN === client.readyState) {
    //             socket.send('Connection Alive')
    //         }
    //     })
    // })
});

app.get('/', (req, res)=> {
    res.end('hello from server')
})
httpServer.listen(4000, ()=> {
    console.log('server is running...')
})

