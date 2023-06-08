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

    const characterPromises = movieData.characters.map((characterUrl) => {
      return new Promise((resolve, reject) => {
        request.get(characterUrl, (error, response, body) => {
          if (error) {
            reject(error);
            return;
          }

          if (response.statusCode !== 200) {
            reject(`Invalid request: ${response.statusCode}`);
            return;
          }

          const characterData = JSON.parse(body);
          resolve(characterData.name);
        });
      });
    });

    Promise.all(characterPromises)
      .then((characterNames) => {
        characterNames.forEach((characterName) => {
          console.log(characterName);
        });
      })
      .catch((error) => {
        console.error('An error occurred:', error);
      });
  });
}

const movieId = process.argv[2];
printCharacters(movieId);
