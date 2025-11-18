function solution(phone_number) {
  let point = phone_number.slice(0, -4).length;
  return "*".repeat(point) + phone_number.slice(point);
}

// 문자열을 반복하고 싶을 땐 repeat() 사용하기.
