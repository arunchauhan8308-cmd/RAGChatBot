const mongoose = require('mongoose');

exports.ConnectDatabase = async ()=> {
    try {
        mongoose.connect(process.env.DB_STR);
        console.log("Database Connected...");
    } catch (error) {
        console.log(error.message);
    };
};