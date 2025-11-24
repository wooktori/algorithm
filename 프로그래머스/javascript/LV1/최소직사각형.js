function solution(sizes) {
  let x = 0;
  let y = 0;
  const changedSizes = sizes.map((e) => (e[0] < e[1] ? [e[1], e[0]] : e));
  for (let i = 0; i < changedSizes.length; i++) {
    if (changedSizes[i][0] > x) {
      x = changedSizes[i][0];
    }
    if (changedSizes[i][1] > y) {
      y = changedSizes[i][1];
    }
  }

  return x * y;
}
