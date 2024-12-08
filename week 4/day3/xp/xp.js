// Exercise 1
// let h1= document.getElementById('header')
// console.log(h1)


// let removePara= document.getElementById('lastParagraph')
// removePara.remove()

// let h2= document.getElementById('headerTwo')
// h2.addEventListener('click', function() {
//     h2.style.backgroundColor = 'red';
// });

// let h3 = document.getElementById('headerThree')
// h3.addEventListener('click', function() {
//     h3.style.display='none'
// }
// )

// let button = document.getElementById('button')
// button.addEventListener('click', function() {
//     const paragraphs = document.querySelectorAll('p');

//     paragraphs.forEach(function(paragraph) {
//         paragraph.style.fontWeight = 'bold';
//     });
// });

// Exercise 2
// let theForm = document.getElementById('form')
// console.log(theForm)

// let inputOne = document.getElementById('fname')
// let inputTwo =document.getElementById('lname')
// let inputThree =document.getElementById('submit')

// console.log(inputOne, inputTwo, inputThree)

// let inputName1 = document.getElementsByName('firstname')
// let inputName2 = document.getElementsByName('lastname')
// let inputName3 = document.getElementsByName('theSubmit')

// console.log(inputName1, inputName2, inputName3)

// let userAnswers = document.getElementById('usersAnswer')
// theForm.addEventListener(submit, function(action){
//     action.preventDefault()
//     inputOne.value.trim()
//     inputTwo.value.trim()
//     if (inputOne === '' || inputTwo === '') {
//         alert("Please fill in both the first name and last name.")
//         return;}
//     let firstName = document.createElement('li')
//     firstName.textContent = `First Name: ${firstName}`

//     let lastName = document.createElement('li')
//     lastName.textContent = `Last Name: ${lastName}`


//     userAnswers.appendChild('firstName')
//     userAnswers.appendChild('lastName')

//     theForm.reset()})

// console.log(theForm)

// Exercise 3
let allBoldItems =[]

function getBoldItems() {
    let boldElements= document.querySelectorAll('p b, p strong')
    allBoldItems = []

    boldElements.forEach(function(element) {
        allBoldItems.push(element)
    });

    console.log(allBoldItems);
    document.getElementById('getBoldButton').addEventListener('click', getBoldItems);
}
getBoldItems()