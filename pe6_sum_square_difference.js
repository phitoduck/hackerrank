// Project Euler #6 - Sum Squared Difference

process.stdin.resume();
process.stdin.setEncoding('ascii');

var input_stdin = "";
var input_stdin_array = "";
var input_currentline = 0;

process.stdin.on('data', function (data) {
    input_stdin += data;
});

process.stdin.on('end', function () {
    input_stdin_array = input_stdin.split("\n");
    main();    
});

function readLine() {
    return input_stdin_array[input_currentline++];
}

/////////////// ignore above this line ////////////////////

function main() {
    var t = parseInt(readLine());
    for(var a0 = 0; a0 < t; a0++){
        var n = parseInt(readLine());
        
        sumRegular = n * (n + 1) / 2
        sumSquareds = (n) * (2*n + 1) * (n + 1) / 6
        
        console.log((sumRegular * sumRegular) - sumSquareds)
    }

}
