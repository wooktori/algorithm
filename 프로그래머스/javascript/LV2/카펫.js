function solution(brown, yellow) {
    for (let h = 1; h <= Math.sqrt(yellow); h++) {
        if (yellow % h === 0) {
            const w = yellow / h;
            if (2 * w + 2 * h + 4 === brown) {
                return [w + 2, h + 2];
            }
        }
    }
}
