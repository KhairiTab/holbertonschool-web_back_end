const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
function getUserName() {
  rl.question('Welcome to Holberton School, what is your name? ', (answer) => {
    console.log(`Your name is: ${answer}`);
    rl.close(); // Close the readline interface
    console.log('This important software is now closing');
  });
}

module.exports = getUserName;
