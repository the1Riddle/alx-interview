#!/usr/bin/node

const request = require("request");

const movieURL = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;

const fetchMovie = (url, callback) => {
  request(url, (err, res, body) => {
    if (err) {
      console.error(`Error fetching movie data: ${err.message}`);
      process.exit(1);
    }
    if (res.statusCode !== 200) {
      console.error(
        `Failed to fetch movie data. Status code: ${res.statusCode}`,
      );
      process.exit(1);
    }
    callback(JSON.parse(body));
  });
};

const fetchCharacter = (url, callback) => {
  request(url, (err, res, body) => {
    if (err) {
      console.error(`Error fetching character data: ${err.message}`);
      process.exit(1);
    }
    if (res.statusCode !== 200) {
      console.error(
        `Failed to fetch character data. Status code: ${res.statusCode}`,
      );
      process.exit(1);
    }
    callback(JSON.parse(body));
  });
};

const logCharacters = (characters, index) => {
  if (index === characters.length) return;
  fetchCharacter(characters[index], (character) => {
    console.log(character.name);
    logCharacters(characters, index + 1);
  });
};

if (process.argv.length < 3) {
  console.error("Usage: ./script <movie_id>");
  process.exit(1);
}

fetchMovie(movieURL, (movie) => {
  logCharacters(movie.characters, 0);
});
