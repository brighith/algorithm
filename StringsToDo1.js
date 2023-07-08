// Remove Blanks
function removeBlanks(input) {
  var output = "";
  for (var i = 1; i < input.length; i++) {
    if (input[i] != " ") {
      output = output + input[i];
    } else {
      continue;
    }
  }
  return output;
}
console.log(removeBlanks(" Pl ayTha tF u nkyM usi c "));

// Get Digits
function getDigits(input) {
  var digits = "";
  for (i = 1; i <= input.length; i++) {
    if (isNaN(input[i])) {
      continue;
    } else {
      digits = digits + input[i];
    }
  }
  return Number(digits);
}
console.log(getDigits("abc8c0d1ngd0j0!8"));
console.log(getDigits("0s1a3y5w7h9a2t4?6!8?0"));

// Acronyms
function acronym(input) {
  var wordsArr = input.split(" ");
  var result = "";
  for (i = 0; i < wordsArr.length; i++) {
    if (wordsArr[i] != "") {
      result = result + wordsArr[i][0].toUpperCase();
    }
  }
  return result;
}
console.log(acronym(" 4 there's no free lunch - gotta pay yer way. "));
console.log(acronym("3Live from New York, it's Saturday Night!"));

// Count Non-Spaces
function countNonSpaces(sentence) {
  var count = 0;
  var words = sentence.split("");
  for (var i = 0; i < words.length; i++) {
    if (words[i] != " ") {
      count = count + 1;
    }
  }
  return count;
}
console.log(countNonSpaces("Honey pie, you are driving me crazy"));
console.log(countNonSpaces("Hello world !"));

// Remove Shorter Strings
function removeShorterStrings(string, num) {
  var result = [];
  for (i = 0; i <= string.length - 1; i++) {
    if (string[i].length >= num) {
      result.push(string[i]);
    }
  }
  return result;
}
console.log(
  removeShorterStrings(
    ["Good morning", "sunshine", "the", "Earth", "says", "hello"],
    4
  )
);
console.log(
  removeShorterStrings(["There", "is", "a", "bug", "in", "the", "system"], 3)
);
