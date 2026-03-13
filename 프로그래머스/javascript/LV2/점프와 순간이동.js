function solution(n)
{
    let answer = 1;
    while(n!==1){
        if(n%2===0){
            n /= 2;
        }else{
            n = (n-1)/2;
            answer++;
        }
    }
    return answer
}