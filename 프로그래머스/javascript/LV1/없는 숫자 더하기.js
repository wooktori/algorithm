function solution(numbers) {
  let ans = 45;
  for (let i = 0; i < numbers.length; i++) {
    ans -= numbers[i];
  }
  return ans;
}
