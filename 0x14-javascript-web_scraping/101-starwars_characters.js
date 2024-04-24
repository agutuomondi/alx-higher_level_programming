#!/usr/bin/node

const axios = require('axios');

// Construct the SWAPI URL based on the film ID from the command line arguments
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

// Make a request to the SWAPI URL
axios.get(apiUrl)
  .then(response => {
    // Parse the JSON response body to get the list of characters
    const characters = response.data.characters;

    // Call the function to print characters, starting from index 0
    printCharacters(characters, 0);
  })
  .catch(error => {
    console.error('Error:', error);
  });

// Function to recursively print characters
async function printCharacters(characters, index) {
  try {
    // Make a request to fetch information about the character at the given index
    const response = await axios.get(characters[index]);
    
    // Print the name of the character
    console.log(response.data.name);

    // Check if there are more characters to print
    if (index + 1 < characters.length) {
      // Recursively call the function for the next character
      await printCharacters(characters, index + 1);
    }
  } catch (error) {
    console.error('Error:', error);
  }
}

