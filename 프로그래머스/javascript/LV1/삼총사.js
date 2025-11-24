function solution(number) {
  let answer = 0;
  for (let i = 0; i < number.length - 2; i++) {
    for (let j = i + 1; j < number.length - 1; j++) {
      for (let k = j + 1; k < number.length; k++) {
        if (number[i] + number[j] + number[k] === 2) {
          answer += 1;
        }
      }
    }
  }
  return answer;
}

// number의 길익 최대 13이기 때문에 삼중 for문을 사용해도 시간복잡도에는 문제없음.
