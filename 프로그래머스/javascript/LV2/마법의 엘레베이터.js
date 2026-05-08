function solution(storey) {
  let answer = 0;

  while (storey > 0) {
    const digit = storey % 10; // 현재 자릿수

    if (digit < 5) {
      answer += digit; // 내림 (digit번 누름)
    } else if (digit > 5) {
      answer += 10 - digit; // 올림 (10-digit번 누름)
      storey += 10 - digit; // 올림 처리
    } else {
      // digit === 5 : 윗 자릿수 보고 결정
      const nextDigit = Math.floor(storey / 10) % 10;
      if (nextDigit >= 5) {
        answer += 5;
        storey += 5; // 올림
      } else {
        answer += 5; // 내림
      }
    }

    storey = Math.floor(storey / 10);
  }

  return answer;
}
