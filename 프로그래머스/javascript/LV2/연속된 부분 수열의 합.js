// 투 포인터 이용
function solution(sequence, k) {
  let left = 0;
  let right = 0;
  let sum = sequence[0];
  let answer = [0, sequence.length - 1];

  while (left <= right && right < sequence.length) {
    if (sum === k) {
      if (right - left < answer[1] - answer[0]) {
        answer = [left, right];
      }
      sum -= sequence[left];
      left++;
    } else if (sum < k) {
      right++;
      sum += sequence[right];
    } else {
      sum -= sequence[left];
      left++;
    }
  }

  return answer;
}
