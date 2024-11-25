// const people = ["Greg", "Mary", "Devon", "James"];
// console.log(people.splice(0,1));
// console.log(people);

// people[2]="Jason"

// people[3]="Georgia"

// console.log(people.indexOf("Mary"))

// console.log(people.slice(1,3))

// console.log(people.indexOf("Foo"))
// because it doesnt exist inside the array

// let last = people[people.length - 1];
// console.log(last)

// part 2 exercise 1
// for (i in people) {
//     console.log(people[i])
// }

// for (let i in people) {
//     if (people[i] != "Devon") {console.log(people[i]);} else if (people[i] == "Devon") {
//         break;
//     }
// }
//  Exercise 2

// let myFavColors=["mint green", "cyan", "purple", "navy"]
// for (let i = 0; i < myFavColors.length; i++) {
//     console.log(`My #${i + 1} choice is ${myFavColors[i]}`);
// }


// Exercise 3
// let numberInput = prompt("Pick a random number");
// let convertedNumber = Number(numberInput); 
// console.log(typeof convertedNumber);     

// while (convertedNumber<10) {
//     console.log(numberInput)
//     numberInput = prompt("Pick a random number again");
//     convertedNumber = Number(numberInput);
// }


// Exercise 4
// 1
// const building = {
//     numberOfFloors: 4,
//     numberOfAptByFloor: {
//         firstFloor: 3,
//         secondFloor: 4,
//         thirdFloor: 9,
//         fourthFloor: 2,
//     },
//     nameOfTenants: ["Sarah", "Dan", "David"],
//     numberOfRoomsAndRent:  {
//         sarah: [3, 990],
//         dan:  [4, 1000],
//         david: [1, 500],
//     },
// }
// 2
// console.log(building.numberOfFloors)

// 3
// console.log(building.numberOfAptByFloor.firstFloor)
// console.log(building.numberOfAptByFloor.thirdFloor)

// 4
// console.log(building.nameOfTenants[1], building.numberOfRoomsAndRent.dan[0] )

// 5
// Check if the sum of Sarah’s and David’s rent is bigger than Dan’s rent. If it is, than increase Dan’s rent to 1200.
// let sumOfRent = building.numberOfRoomsAndRent.sarah[1] + building.numberOfRoomsAndRent.david[1]
// building.numberOfRoomsAndRent.dan[1]=1200
// console.log(building.numberOfRoomsAndRent.dan)

// 5
// let family = {
//     mom:"Olga",
//     daughter:"Gigi",
//     grandma:"Tatian",
//     grandpa:"Anatoly"
// }

// for (let i in family) {
//     console.log(i)
// }

// for (let i in family) {
//     console.log(family[i])
// }

// Exercise 6
// const details = {
//     my: 'name',
//     is: 'Rudolf',
//     the: 'reindeer'
//   }

//   console.log(`My ${details.my} is ${details.is} the ${details.the}`);


//   Exercise 7
const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];

let firstLetters = ["J","P","S","A","B","K"]
firstLetters.sort()

let nameSociety = firstLetters.join("")
console.log(nameSociety)

