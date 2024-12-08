// // ex 1
// function compareToTen(num) {
//     return new Promise((resolve, reject) => {
//       if (num <= 10) {
//         resolve('The number is less than or equal to 10.');
//       } else {
//         reject('The number is greater than 10.');
//       }
//     });
//   }
  
//   // Tests
//   compareToTen(15)
//     .then(result => console.log(result))
//     .catch(error => console.log(error));  

//   compareToTen(8)
//     .then(result => console.log(result))  
//     .catch(error => console.log(error));
  
// // ex 2
// function resolveAfter4() {
//     return new Promise((resolve) => {
//       setTimeout(() => {
//         resolve("success");
//       }, 4000); 
//     });
//   }
  
// resolveAfter4()
//     .then(result => console.log(result)) 
//     .catch(error => console.log(error));
  
// ex 3
const promiseResolve = Promise.resolve(3);

const promiseReject = Promise.reject("Boo!");

promiseResolve
  .then(result => console.log(result)) 
  .catch(error => console.log(error));

promiseReject
  .then(result => console.log(result))
  .catch(error => console.log(error));  
