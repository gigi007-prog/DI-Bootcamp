// 1
let sentence = 'The food was not that bad'


// 2
let wordNot = sentence.indexOf("not")

// 3
let wordBad = sentence.indexOf("bad")

//  4
// If the word “bad” comes after the word “not”, you should replace the whole “not…bad” substring with “good”, 
// then console.log the result. For example, the result here should be : “The movie is good, I like it”
if (wordNot !== -1 && wordBad > wordNot) {
    sentence = sentence.replace("not that bad", "good");
}

console.log(sentence);


