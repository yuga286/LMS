const rl=require("readline-sync")
	function reverseString(x) {
		return x.split('').reverse().join('');
	}
	let x=rl.question("Enter the string you want to be reversed:\n");
	cons