#!/usr/bin/node

const request = require('request');
const apiUrl = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

// Function to recursively print characters
function printCharacters (characters, index) {
  request(characters[index], function (error, response, body) {
    // Check for errors in the request
    if (!error) {
      // Print the name of the character
      console.log(JSON.parse(body).name);

      // Check if there are more characters to print
      if (index + 1 < characters.length) {
        // Recursively call the function for the next character
        printCharacters(characters, index + 1);
      }
    }
  });
}

// Make a request to the SWAPI URL
request(apiUrl, function (error, response, body) {
  // Check for errors in the request
  if (!error) {
    const characters = JSON.parse(body).characters;

    printCharacters(characters, 0);
  }
});

