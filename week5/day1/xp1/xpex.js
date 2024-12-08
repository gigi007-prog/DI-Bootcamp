// ex 1 
// the output would be: inside the funcOne function 3
// if u declare a as a const it would be immutabe thus woud give out an error
// calling function three will show that a is zero calling function two means changing the value of a and fuction three will show the changed value
// if a was const it would run function three and break on function two because we cant change a const variable
// func four added a to the global window object and could be called anywhere func five would call a so will output hello
// the output will be test with both let and const cause its not a global variable its a local one
// inside if it would 5 outisde would 2 same would be with const because of the global scope

// ex 2
// const winBattle = () => true;
// const experiencePoints = winBattle() ? 10 : 1;
// console.log(experiencePoints);

// ex 3
// const maybeString = (value) => typeof value === 'string';

// console.log(maybeString("Hello, world!"));
// console.log(maybeString(123)); 

// ex 4
// const sum = (a, b) => a + b;
// console.log(sum(99,100))

// ex 5
// function convertGrams(weightInKg) {
//     return weightInKg * 1000;
// }
// console.log(convertGrams(5));
//  hoisted can be called before its defined 

// const convertGrams = function(weightInKg) {
//     return weightInKg * 1000;
// };

// console.log(convertGrams(5));
// not hoisted cannot be called before its defined


// const convertGrams = (weightInKg) => weightInKg * 1000;
// console.log(convertGrams(10)); 

//  ex 7
// (function(userName) {
//     const hiDiv = document.createElement('div');
    
//     const profilePicture = 'https://www.w3schools.com/howto/img_avatar.png';
//     const profileName = document.createElement('span');
//     profileName.textContent = `Welcome, ${userName}`;
    
//     const img = document.createElement('img');
//     img.src = profilePicture; 
//     img.alt = `${userName}'s profile picture`;

//     hiDivDiv.appendChild(profileName);
//     hiDivDiv.appendChild(img);
    
//     document.getElementById('welcomeMessage').appendChild(hiDiv);
// })('John');  


// ex 8
// part 1
