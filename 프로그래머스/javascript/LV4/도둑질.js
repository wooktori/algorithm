// 나의 풀이는 효율성 테스트 6에서 시간초과.
// 정답 풀이와 로직이 같고, 시간복잡도 역시 동일한데 시간초과가 나는 이유는 뭘까?
// 나의 코드는 클로저를 포함하고 있어 JS 엔진이 최적화를 덜 적용.

// 나의 풀이 (시간초과)
function solution(money) {
  const n = money.length;

  function rob(start, end) {
    const dp = Array(n).fill(0);
    dp[start] = money[start];
    dp[start + 1] = Math.max(money[start], money[start + 1]);

    for (let i = start + 2; i <= end; i++) {
      dp[i] = Math.max(dp[i - 1], dp[i - 2] + money[i]);
    }
    return dp[end];
  }

  return Math.max(rob(0, n - 2), rob(1, n - 1));
}

// 정답 풀이 (통과)
function solution(money) {
  const len = money.length;

  // 첫 번째 집을 털 경우
  const steal1 = new Array(len).fill(0);
  steal1[0] = money[0];
  steal1[1] = money[0];
  for (let i = 2; i < len - 1; i++) {
    steal1[i] = Math.max(steal1[i - 1], steal1[i - 2] + money[i]);
  }

  // 첫 번째 집을 털지 않는 경우
  const steal2 = new Array(len).fill(0);
  steal2[0] = 0;
  steal2[1] = money[1];
  for (let i = 2; i < len; i++) {
    steal2[i] = Math.max(steal2[i - 1], steal2[i - 2] + money[i]);
  }

  // 마지막 집을 털지 않은 경우와 마지막 집을 털어도 되는 경우 중 최댓값 반환
  return Math.max(steal1[len - 2], steal2[len - 1]);
}
