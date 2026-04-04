function solution(begin, target, words) {
    const visited = Array(words.length).fill(false);
    const queue = [[begin,0]];
    let head = 0;
    
    while(queue.length>head){
        const [value, count] = queue[head++];
        if(value===target) return count;
        
        for(let i=0;i<words.length;i++){
            if(visited[i]) continue;
            if(!check(value,words[i])) continue;
            
            visited[i] = true;
            queue.push([words[i],count+1]);
        }
        
    }
    return 0;
}

function check(a,b){
    let count = 0;
    for(let i=0;i<a.length;i++){
        if(a[i]!==b[i]) count++;
    }
    
    return count===1;
}
