let rowNumber = 6;

for (let i = 1; i <= rowNumber; i++) {
    console.log('* '.repeat(i).trim()); }




for (let i = 1; i <= rowNumber; i++) {  // Outer loop for rows
    let star = '';  // Initialize an empty string for the stars in each row
    
        for (let j = 1; j <= i; j++) {  // Inner loop for printing stars
            star += '* ';  // Add a star followed by a space
        }
    
        console.log(star.trim());  // Print the stars for the current row, removing trailing space
    }