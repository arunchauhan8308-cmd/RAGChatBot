const express = require('express');
const { ConnectDatabase } = require('./src/config/db');
const app = express();
const dotenv = require('dotenv').config();
const dns = require('dns');
dns.setServers(['0.0.0.0','1.1.1.1']);


// use middleware
app.use(express.json())

// connect the database
ConnectDatabase();


// start the server
app.listen(process.env.PORT, ()=> {
    console.log("server is running...");
});