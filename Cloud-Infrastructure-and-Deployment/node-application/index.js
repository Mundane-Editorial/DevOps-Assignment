require('dotenv').config();

const express = require('express');
const app = express();
const port = process.env.PORT || 3000;

app.get('/', (req, res) => {
    res.send('Hello World From Azure Servers!');
});

app.get('/about', (req, res) => {
    res.send('This is a simple Node.js app with Express.');
});

app.listen(port, () => {
    console.log(`server configured and is listening on ${port}`);
});
