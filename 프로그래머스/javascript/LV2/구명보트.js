function solution(people, limit) {
    people.sort((a, b) => a - b);
    let left = 0;
    let right = people.length - 1;
    let boats = 0;

    while (left <= right) {
        // 가장 가벼운 사람 + 가장 무거운 사람이 같이 탈 수 있으면 함께
        if (people[left] + people[right] <= limit) {
            left++;
        }
        // 무거운 사람은 항상 보트 탑승
        right--;
        boats++;
    }

    return boats;
}