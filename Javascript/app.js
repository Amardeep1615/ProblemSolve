// 1.Check a Palindrome number
// let n = Number("Enter a number:");
function isPalindrome(str){
    let reversed = str.split('').reverse().join('');
    return  str == reversed;
}
console.log(isPalindrome("madam"));

