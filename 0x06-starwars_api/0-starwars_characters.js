#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

if (!movieId) {
  console.error('Please provide a movie ID as a positional argument.');
  process.exit(1);
}

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode === 200) {
    const movie = JSON.parse(body);
    const characters = movie.characters;

    // Array of promises for fetching each character
    const characterPromises = characters.map((characterUrl) => {
      return new Promise((resolve, reject) => {
        request(characterUrl, (charError, charResponse, charBody) => {
          if (charError) {
            reject(charError);
          } else {
            const character = JSON.parse(charBody);
            resolve(character.name);
          }
        });
      });
    });

    // Execute all promises and print character names in order
    Promise.all(characterPromises)
      .then((names) => {
        names.forEach((name) => console.log(name));
      })
      .catch((err) => {
        console.error('Error fetching character names:', err);
      });
  } else {
    console.error(`Failed to retrieve movie data. Status code: ${response.statusCode}`);
  }
});
