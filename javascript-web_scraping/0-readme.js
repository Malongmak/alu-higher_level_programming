#!/usr/bin/node
const fs = require('fs');
const filePath = process.argv[2];

fs.readFile(filepath, 'utf8', (error, data) => {
	if (error) {
		console.error(error);
		return;
	}

	console.log(data);
});
