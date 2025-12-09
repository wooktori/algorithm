function solution(n, arr1, arr2) {
  let answer = [];
  for (let i = 0; i < n; i++) {
    let temp = (arr1[i] | arr2[i]).toString(2).padStart(n, 0);
    let ans = "";
    for (let j = 0; j < temp.length; j++) {
      if (temp[j] === "0") {
        ans += " ";
      } else {
        ans += "#";
      }
    }
    answer.push(ans);
  }
  return answer;
}

// 비트연산자를 이용해 변환
// padStart를 이용해 n자리수 맞추기
// 0은 공백, 1은 #으로 변환
