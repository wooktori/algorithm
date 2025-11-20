// function solution(s) {
//   if (s.length === 4 || s.length === 6) {
//     if (!isNaN(s)) {
//       return true;
//     } else {
//       return false;
//     }
//   } else {
//     return false;
//   }
// }

// 위 방법을 이용하면 '0x16' 같은 숫자도 인식하기 때문에 통과하지 못함.
// 아래처럼 정규표현식을 이용해야 통과.

function solution(s) {
  return /^\d{6}$|^\d{4}$/.test(s);
}
