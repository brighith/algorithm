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

// Filter Range
function filterRange(arr, max, min) {
  for (i = 0; i <= arr.length - 1; i++) {
    if (arr[i] >= max) delete arr[i];
    else if (arr[i] <= min) {
      delete arr[i];
    }
  }

  return arr;
}

console.log(filterRange([1, 2, 3, 4, 5, 78, 45, 23, 12, 90, 100], 89, 2));

// Concat
function arrConcat(arr1, arr2) {
  var arr = [];
  arr = arr1.concat(arr2);
  return arr;
}

console.log(arrConcat(["c", "b"], [4, 5, 6]));
