function solution(tickets) {
    tickets.sort((a,b)=>a[1].localeCompare(b[1])); // 목적지 기준으로 정렬

    const visited = Array(tickets.length).fill(false);
    const arr = ["ICN"]
    
    // 백트래킹과 return에 유의하여 작성
    function dfs(start){
        if(arr.length===tickets.length+1) return true;
        
        for(let i=0;i<tickets.length;i++){
            if(visited[i]) continue;
            if(tickets[i][0] !== start) continue;
            
            arr.push(tickets[i][1]);
            visited[i] = true;
            
            if(dfs(tickets[i][1])) return true;
            
            arr.pop();
            visited[i] = false
        }
    }
    
    
    dfs("ICN");
    return arr;
}