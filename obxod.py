const express = require('express');
const request = require('request');
const app = express();
const port = process.env.PORT || 3000;

app.use((req, res) => {
    const url = `https://www.youtube.com${req.url}`;
    req.pipe(request(url)).pipe(res);
});

app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});
