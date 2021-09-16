let number = 1;
let text = "";

function fizzbuzz(number) {
    let firstMultiple = 3;
    let secondMultiple = 5;
    if ((number % firstMultiple == 0) && (number  % secondMultiple == 0)) {
        return "FizzBuzz";
    } else if (number % firstMultiple == 0) {
        return "Fizz";
    } else if (number % secondMultiple ==  0) {
        return "Buzz";
    } else {
        return number;
    }
}

function printfizzbuzz() {
    text = fizzbuzz(number++) ;//+ ",   ";
    // (text.length % 80 > 71) ? (text += "<br>") : (text += " - ");
    console.log("clicked");
    document.getElementById("btn").innerHTML=text;
}

function testing() {
    text += "clicked ";
    document.getElementById("output").innerHTML=text;
}

document.getElementById("btn").addEventListener('click', printfizzbuzz);
