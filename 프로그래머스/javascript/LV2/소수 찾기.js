function solution(numbers) {
  const digits = numbers.split("");
  const visited = Array(digits.length).fill(false);
  const set = new Set();

  function dfs(current) {
    if (current !== "") {
      set.add(Number(current));
    }

    for (let i = 0; i < digits.length; i++) {
      if (visited[i]) continue;

      visited[i] = true;
      dfs(current + digits[i]);
      visited[i] = false;
    }
  }

  dfs("");

  let count = 0;
  for (let num of set) {
    if (isSosu(num)) count++;
  }

  return count;
}

function isSosu(number) {
  if (number < 2) return false;

  for (let i = 2; i <= Math.sqrt(number); i++) {
    if (number % i === 0) return false;
  }

  return true;
}
