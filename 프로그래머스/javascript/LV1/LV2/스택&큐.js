function solution(s) {
  const stack = [];

  for (let word of s) {
    if (word === "(") {
      stack.push(word);
    } else {
      if (stack.length === 0) {
        return false;
      }
      stack.pop();
    }
  }

  return stack.length === 0;
}

// for of 문을 이용해 문자열의 한 단어씩 접근 가능.

// stack의 기본적인 원리를 이용해 "(" 일 때 배열에 추가, ")" 일 때 배열에 있는 "(" 제거.
// 단, ")" 일 때 배열에 아무런 값이 들어있지 않다면 오류이므로 바로 false 리턴.
