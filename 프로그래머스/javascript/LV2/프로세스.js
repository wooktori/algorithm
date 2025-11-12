function solution(priorities, location) {
  const queue = priorities.map((p, index) => ({ p, index }));
  const answer = [];
  while (queue.length !== 0) {
    const current = queue.shift();
    let flag = false;
    for (let i = 0; i < queue.length; i++) {
      if (current.p < queue[i].p) {
        flag = true;
        break;
      }
    }
    if (flag === true) {
      queue.push(current);
    } else {
      answer.push(current);
    }
  }

  return answer.findIndex((ans) => ans.index === location) + 1;
}

// shift() 함수를 이용해 큐의 pop 처럼 사용 가능.
// some() 함수를 이용하면 보다 간단하게 구현 가능.
// some(조건) => 조건에 해당하는 원소가 배열에 존재한다면...
