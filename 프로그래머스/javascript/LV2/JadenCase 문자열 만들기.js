function solution(s) {
    let arr = s.split(' ');
    for (let i = 0; i < arr.length; i++) {
        arr[i] = arr[i].toLowerCase();
        if (arr[i].trim() === '') continue;
        arr[i] = arr[i][0].toUpperCase() + arr[i].slice(1)
    }
    return arr.join(' ');
}