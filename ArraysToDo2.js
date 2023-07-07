//Reverse
function reverse(arr) {
  var first = 0;
  var last = arr.length - 1;
  while (first <= last) {
    [arr[first], arr[last]] = [arr[last], arr[first]];
    last--;
    first++;
  }
  return arr;
}
console.log(reverse([1, 4, 6, 7, 8, 9, 0, 7]));

// Rotate
function rotateArr(arr, shiftBy) {
  for (var i = 0; i < shiftBy; i++) {
    current = arr.pop();
    arr.unshift(current);
  }
  return arr;
}
console.log(rotateArr([1, 2, 3, 4, 5, 6, 7], 1));
