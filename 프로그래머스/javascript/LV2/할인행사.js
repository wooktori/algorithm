function solution(want, number, discount) {
  let answer = 0; // 날짜 수를 카운트

  for (let i = 0; i <= discount.length - 10; i++) {
    const check = discount.slice(i, i + 10);
    let flag = false;
    for (let j = 0; j < want.length; j++) {
      if (check.filter((k) => k === want[j]).length !== number[j]) {
        flag = true;
        break;
      }
    }
    if (!flag) {
      answer++;
    }
  }

  return answer;
}
