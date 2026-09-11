const fs = require('fs/promises');
const path = require('path');
const { PDFLoader } = require('@langchain/community/document_loaders/fs/pdf');

const directory = '../../Data';

const LoadTheDirectory = async (directory) => {
    // read the all files in the given directory
    const files = await fs.readdir(directory)

    // read the .pdf file in the all files
    const pdfFiles = files.filter(file => path.extname(file) == '.pdf');

    // 
    // return the founded pdf files 
    return pdfFiles
};

const pdfFileRead = async (files) => {

    let data = [];
    // read the files
    for (let file of files) {
        // const readPdfFileData = await fs.readFile(file);
        const DataBuffer = new PDFLoader(file)
        const pdfData = await DataBuffer.load();

        data.push(...pdfData);
    };
    
}

const DirectoryLoader = async () => {
    const dir = await LoadTheDirectory(directory);
    const pdfLoader = await pdfFileRead(dir)
    // console.log(pdfLoader.length)
}

DirectoryLoader();

module.exports = {
    DirectoryLoader
}

