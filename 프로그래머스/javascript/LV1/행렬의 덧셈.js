function solution(arr1, arr2) {
  var answer = [];
  for (let i = 0; i < arr1.length; i++) {
    let arr = new Array(arr1[0].length).fill(0);
    for (let j = 0; j < arr1[0].length; j++) {
      arr[j] = arr1[i][j] + arr2[i][j];
    }
    answer.push(arr);
  }
  return answer;
}

// new Array(x).fill(y) 배열의 원소를 x개만큼 y로 채우기.
