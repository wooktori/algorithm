const solution = (n, works) => {
  works.sort((a, b) => b - a);
  let idx = 0;
  while (n > 0) {
    if (works[idx] <= works[0]) idx = 0;
    if (works[idx] === 0 || idx >= works.length) break;
    works[idx]--;
    n--;
    idx++;
    if (idx >= works.length) idx = 0;
  }
  console.log(works);
  return works.reduce((a, c) => a + c * c, 0);
};
