const fs = require('fs');
const pdf_parse = require('pdf-parse');

const directory = '../../Data';

const DirectoryLoader = async (directory) => {
    const files = await fs.readFileSync(directory);
    console.log(files.length)   
}

exports.loadTheData = async (directory) => {
    console.log("Abhishek Raj");
};

DirectoryLoader(directory);