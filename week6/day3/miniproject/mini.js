function getRandomCharacterId() {
    return Math.floor(Math.random() * 83) + 1; 
}

function getHomeworldName(homeworldUrl) {
    return fetch(homeworldUrl)
        .then(response => response.json())
        .then(data => {
            return data.result.properties.name; 
        })
        .catch(error => {
            console.error("Error fetching homeworld data:", error);
            return "Unknown"; 
        });
}

function getCharacterData() {
    const characterId = getRandomCharacterId();
    const url = `https://www.swapi.tech/api/people/${characterId}`;

    document.getElementById("loading").style.display = "block";
    document.getElementById("characterInfo").style.display = "none";
    document.getElementById("errorMessage").textContent = ''; // Clear previous error message

    fetch(url)
        .then(response => response.json())
        .then(data => {
            document.getElementById("loading").style.display = "none";

            if (data.result) {
                const character = data.result.properties;

                getHomeworldName(character.homeworld).then(homeworldName => {
                    document.getElementById("characterInfo").style.display = "block";

                    document.getElementById("characterName").textContent = character.name;
                    document.getElementById("characterHeight").textContent = `Height: ${character.height} cm`;
                    document.getElementById("characterGender").textContent = `Gender: ${character.gender}`;
                    document.getElementById("characterBirthYear").textContent = `Birth Year: ${character.birth_year}`;
                    document.getElementById("characterHomeworld").textContent = `Homeworld: ${homeworldName}`;
                });
            } else {
                showError("Character data not found. Try again.");
            }
        })
        .catch(error => {
            console.error("Error fetching data:", error);
            document.getElementById("loading").style.display = "none";
            showError("Failed to load data! Please try again.");
        });
}

function showError(message) {
    document.getElementById("errorMessage").textContent = message;
    document.getElementById("errorMessage").style.display = "block";
}

function setup() {
    const button = document.getElementById("getCharacterBtn");
    button.addEventListener("click", getCharacterData);
}

document.addEventListener("DOMContentLoaded", setup);
