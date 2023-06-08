#!/usr/bin/node
const request = require('request');

function printCharacters(movieId) {
  const baseUrl = 'https://swapi.dev/api/films/';
  const movieUrl = `${baseUrl}${movieId}/`;

  request.get(movieUrl, (error, response, body) => {
    if (error) {
      console.error('An error occurred:', error);
      return;
    }

    if (response.statusCode !== 200) {
      console.error('Invalid request:', response.statusCode);
      return;
    }

    const movieData = JSON.parse(body);
    console.log(`Characters in ${movieData.title}:`);

    movieData.characters.forEach((characterUrl) => {
      request.get(characterUrl, (error, response, body) => {
        if (error) {
          console.error('An error occurred:', error);
          return;
        }

        if (response.statusCode !== 200) {
          console.error('Invalid request:', response.statusCode);
          return;
        }

        const characterData = JSON.parse(body);
        console.log(characterData.name);
      });
    });
  });
}

const movieId = process.argv[2];
printCharacters(movieId);

