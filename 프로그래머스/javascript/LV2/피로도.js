function solution(k, dungeons) {
  let answer = 0;
  const visited = Array(dungeons.length).fill(false);

  function backtracking(hp, count) {
    answer = Math.max(answer, count);

    for (let i = 0; i < dungeons.length; i++) {
      const [minimum, need] = dungeons[i];
      if (!visited[i] && hp >= minimum) {
        visited[i] = true;
        backtracking(hp - need, count + 1);
        visited[i] = false;
      }
    }
  }

  backtracking(k, 0);
  return answer;
}
