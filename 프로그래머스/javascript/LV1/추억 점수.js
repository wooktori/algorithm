function solution(name, yearning, photo) {
  let answer = [];
  for (let i = 0; i < photo.length; i++) {
    let temp = 0;
    for (let j = 0; j < photo[i].length; j++) {
      const index = name.indexOf(photo[i][j]);
      if (name.indexOf(photo[i][j]) === -1) {
        continue;
      } else {
        temp += yearning[index];
      }
    }
    answer.push(temp);
  }
  return answer;
}

// indexOf를 사용해 해당 문자열의 인덱스를 찾고, 그 인덱스를 이용해 yearning 배열에서 점수 찾아 더하기.
