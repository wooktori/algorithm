function solution(prices) {
    let arr = [];
    for(let i=0;i<prices.length;i++){
        let count = 0;
        for(let j=i+1;j<prices.length;j++){
            count++;
            if(prices[i]>prices[j]) break;
        }
        arr.push(count);
    }
    
    return arr;
}