		// document.addEventListener("DOMContentLoaded", function() {
		//   var condition = {{ condition|default(false)|lower }};
		 
	
		//   function showErrorMessage(message) {
		// 	var errorElement = document.getElementById("error-message");
		// 	if (errorElement) {
		// 		console.log("aaaader");
		// 	  	errorElement.textContent = message;
		// 	  	console.log("aaaasaader");
		// 	  	errorElement.style.display = "block";
		// 	}
		//   }
	
		//   if (condition) {
		// 	showErrorMessage("Passwords do not match!");
		//   }
		// });
	 

		// const obj={
		// 	a:1,
		// 	b:2
		// };
		// for(i in obj){
		// 	console.log(obj[i]);
		// }


		// const input=require("readline-sync")
		// let a=Input.questionInt()

// const input = require("readline-sync");
// const { questionInt } = input;

// let a = questionInt("Enter an integer: ");
// console.log(`You entered: ${a}`);


// function test(a,b){
// 	console.log(a+b);
// }



// const prompt = require("prompt-sync")();
// var c;
// c=prompt()
// console.log(c);

// const myArray = ["Hello", "JS", "World"];

// console.log("Concatenated:", myArray.join("@"));

// const obj={
// 	key: function(){
// 		console.log("sdfasf");
// 	}
// }

// obj.key()
// 	obj[obj]()

	// const a={
	// 	key:{
	// 		ab:function(){
	// 			console.log("aaaaa");
	// 		}
	// 	}
	// }

	// a.ab()


	// const rl=require("readline-sync")
	// email=rl.questionEMail()
	// Name=rl.question()
	// Number=rl.question()
	// Password=rl.question()

	// const obj={}

	// obj.email.Name=Name
	// obj.email.Number=Number
	// obj.email.Password=Password

	// obj[email]={}
	// obj[email].Name=Name
	// obj[email].Number=Number
	// obj[email].Password=Password

	// console.log(obj);


	// const rl=require("readline-sync")
	// function reverseString(x) {
	// 	return x.split('').reverse().join('');
	// }
	// let x=rl.question("Enter the string you want to be reversed:\n");
	// console.log(reverseString(x));

	// const rl=require("readline-sync")
	// // function reverseString(x) {
	// // 	return x.split('').reverse().join('');
	// // }
	// let x=rl.questionInt("Enter the length of the array:\n");
	// let arr=[];

	// for(var i=0;i<x;i++){
	// 	arr.push(rl.questionInt("Enter the array elements:\n"));
	// }
	// // console.log(arr);

	// var a=eval(arr.join("+"))
	// console.log(a);
	// for(var i=0;i<x;i++){
		
	// }


	// let x=rl.questionInt("Enter the string you want to be reversed:\n");
	// console.log(reverseString(x));


	

	// function ana(){
	// 	return function(){
	// 		console.log("hello");
	// 	}
	// }
	// k=ana();
	// function xyz(k){
	// 	k()
	// 	// console.log(k);
	// }
	

	// xyz(k)




// const mapp = array.map((element, index) => {
//     return index, element * 2;
// });

// console.log(mapp); // Output: [0, 1, 4]

// const array = [2, 4, 6,5];
// const arr=[0,1];
// const k=array.reduce((acc, element) => {
	
// 	arr[0]+=element;
// 	arr[1]*=element;
// 	return arr;
// },1)

// console.log(arr);

// const array = [2, 4, 6, 5];
// const { sum, product } = array.reduce((acc, element) => {
//     const { sum, product } = acc;
//     return {
//         sum: sum + element,
//         product: product * element
//     };
// }, { sum: 0, product: 1 });

// console.log("Sum:", sum);
// console.log("Product:", product);



// var x = new Set(['abc123', 'def', 'ghi456']);
// var y = new Set();

// x.forEach(function(item) {
//     if (!isNaN(parseInt(item))) {
//         y.add(item);
//     }
// });

// console.log(y);

// const arr = ["abc123","ghi456","dif","ghi456"]
// function x(y){
// 	return /\d/.test(y);
// }
// const s = arr.filter(x)
// console.log(s);


//  var x=[[10, 20, 30], [40, 50, 60], [70, 80, 90]]
// var a=x.map((sub,index)=>{
// 	return {
// 			index : index,
// 			value:x[sub],
// 	};
// })
// console.log(a);


var dates = ["2023-12-31", "2024-01-15", "2025-05-20"];

function make(date){
	return date.map(function doit(date){
		var x=date.split("-");
		return x[2]+"/"+x[1]+"/"+x[0];
	})
}

var c=make(dates);
console.log(c);