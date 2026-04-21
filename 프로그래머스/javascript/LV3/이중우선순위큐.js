function solution(operations) {
  let arr = [];

  for (const op of operations) {
    const [char, num] = op.split(" ");
    if (char === "I") {
      arr.push(Number(num));
      arr.sort((a, b) => a - b);
    } else {
      if (arr.length === 0) continue;
      if (num === "-1") {
        arr.shift(); // 최솟값 제거
      } else {
        arr.pop(); // 최댓값 제거
      }
    }
  }

  if (arr.length === 0) return [0, 0];
  return [arr[arr.length - 1], arr[0]];
}
