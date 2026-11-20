#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + movieId;

const getCharacter = (charUrl) => {
  return new Promise((resolve, reject) => {
    request(charUrl, (err, res, body) => {
      if (err) {
        reject(err);
      } else {
        resolve(JSON.parse(body).name);
      }
    });
  });
};

request(url, async (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const characters = JSON.parse(body).characters;
  if (characters) {
    for (const charUrl of characters) {
      const name = await getCharacter(charUrl);
      console.log(name);
    }
  }
});
