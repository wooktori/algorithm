function solution(price, money, count) {
  let totalCount = 0;
  for (let i = 1; i <= count; i++) totalCount += i;

  return totalCount * price - money >= 0 ? totalCount * price - money : 0;
}
