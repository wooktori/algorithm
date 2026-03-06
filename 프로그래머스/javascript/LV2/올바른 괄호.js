function solution(s) {
    const stack = []

    for (let word of s) {
        if (word === "(") {
            stack.push(word);
        }
        else {
            if (stack.length === 0) {
                return false;
            }
            stack.pop();
        }
    }

    return stack.length === 0;
}