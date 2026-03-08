function solution(progresses, speeds) {
    // 각 기능이 완료되기까지 걸리는 일수 계산
    const days = progresses.map((p, i) => Math.ceil((100 - p) / speeds[i]));

    const answer = [];
    let max = 0;   
    let count = 0; 

    for (const day of days) {
        // 현재 기능이 기준 일수보다 오래 걸리면 → 새 배포 묶음 시작
        if (day > max) {
            if (count > 0) answer.push(count); 
            max = day; 
            count = 0; 
        }
        count++; 
    }

    answer.push(count);
    
    return answer;
}
