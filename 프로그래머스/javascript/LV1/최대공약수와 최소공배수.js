function gcd(b, a) {
  var r = b % a;
  return r ? gcd(a, r) : a;
}

function solution(n, m) {
  return [gcd(m, n), (m * n) / gcd(m, n)];
}
