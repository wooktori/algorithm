function solution(arr) {
  if (arr.length === 1) {
    return [-1];
  } else {
    arr.splice(arr.indexOf(Math.min(...arr)), 1);
    return arr;
  }
}

// splice는 원래 배열을 변경시킴.
// slice는 원래 배열을 변경시키지 않음.
