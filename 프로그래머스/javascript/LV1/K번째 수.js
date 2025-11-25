function solution(array, commands) {
  let answer = [];
  for (let n = 0; n < commands.length; n++) {
    answer.push(
      array.slice(commands[n][0] - 1, commands[n][1]).sort((a, b) => a - b)[
        commands[n][2] - 1
      ]
    );
  }
  return answer;
}

// sort()가 오름차순이지만, 명확하게 sort((a,b)=>a-b)를 사용해 풀어주기.
// sort() 는 유니코드를 기준으로 정렬한다. 숫자 정렬에서는 9가 80보다 앞에 오지만, "80"은 유니 코드 순서에서 "9"앞에 오기 때문에 명확한 조건 작성이 필요하다.
