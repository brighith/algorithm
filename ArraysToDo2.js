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
