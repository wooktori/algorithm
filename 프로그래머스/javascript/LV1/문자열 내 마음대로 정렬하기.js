function solution(strings, n) {
  return strings.sort((s1, s2) =>
    s1[n] === s2[n] ? s1.localeCompare(s2) : s1[n].localeCompare(s2[n])
  );
}

// sort()
// 이 함수가 리턴하는 값이 0보다 작을 경우, a가 b보다 앞에 오도록 정렬.
// 이 함수가 리턴하는 값이 0보다 클 경우, b가 a보다 앞에 오도록 정렬.
// 0을 리턴하면 유지.

// localeCompare()
// 기준문자열.localeCompare(비교할 문자열) 처럼 사용.
// 기준문자열이 비교할 문자열보다 작으면 -1
// 기준문자열이 비교할 문자열보다 크면 1
// 기준문자열이 비교할 문자열보다 같으면 0

// s1[n]과 s2[n]을 비교해서 같으면 원래 문자열 비교, 다르면 n번째 인덱스의 문자를 기준으로 분자열 비교.
