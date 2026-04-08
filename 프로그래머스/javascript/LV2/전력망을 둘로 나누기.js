function solution(n, wires) {
    const graph = Array.from({length:n+1}, ()=>[]);
    let answer = 1e9
    
    for(let i=0;i<wires.length;i++){ // 그래프 생성
        const [x,y] = wires[i];
        graph[x].push(y);
        graph[y].push(x);
    }
        
    function bfs(x,y){ // x-y의 간선을 자르는 것으로 간주
        const visited = Array(n+1).fill(false);
        const queue = [1];
        visited[1] = true;
        let count = 0;
        let head = 0;
        
        while(queue.length>head){
            const node = queue[head++];
            count++;
            
            for(const next of graph[node]){
                if (!visited[next] && !(node === x && next === y) && !(node === y && next === x)) { // 방문하지 않았고, x-y가 아니라면
                    visited[next] = true;
                    queue.push(next);
                }
            }
        }
        return count
    }
        
    for(let i=0;i<wires.length;i++){
            const temp = bfs(wires[i][0],wires[i][1]);
            const value = Math.abs(temp- (n-temp));
            answer = Math.min(answer, value);
        }
        
    return answer;
}