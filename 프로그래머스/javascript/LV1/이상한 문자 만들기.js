function solution(s) {
  let answer = [];
  let arr = s.split(" ");
  for (word of arr) {
    let newWord = "";
    for (let i = 0; i < word.length; i++) {
      if (i % 2 == 0) {
        newWord += word[i].toUpperCase();
      } else {
        newWord += word[i].toLowerCase();
      }
    }
    answer.push(newWord);
  }
  return answer.join(" ");
}

// 문자.toLowerCase() , 문자.toUpperCase() => 문자 대소문자 변경.
