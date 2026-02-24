function solution(k, tangerine) {
    let answer = 0;
    const obj = {};
    
    for(let i=0;i<tangerine.length;i++){
        if(obj[tangerine[i]]){
            obj[tangerine[i]]++;
        }else{
            obj[tangerine[i]] = 1;
        }        
    }
    
    const sorted = Object.entries(obj).sort((a,b)=>b[1]-a[1]);
    
    for(let i=0;i<sorted.length;i++){
        answer++;
        if(k>sorted[i][1]){
            k -= sorted[i][1];
        }else{
            break;
        }
    }
    return answer;
}

