#!/usr/bin/node
const request = require('request');
const URI = 'https://swapi-api.hbtn.io/api/films';
const ID = process.argv[2];
const params = {
    url: URI + ID,
    method: 'GET'
};

request(params, function(error,_,body){
    if(error) {
        console.log('Failed, please try again!');
    }
    else {
        const characters = JSON.parse(body).characters;
        getCharacters(characters, 0)
    }
});

function getCharacters(character, id) {
    request(character[id], function(error,_,body) {
        if (error) {
            console.log("Getting characters failed!");
        }
        else {
            console.log(JSON.parse(body).name);
            if (id + 1 < character.length) {
                getCharacters(character, id + 1);
            }
        }
    })
}