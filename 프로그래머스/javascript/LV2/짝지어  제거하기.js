// s의 처음 글자부터 하나씩 스택에 넣기
// 현재 글자와 스택의 가장 위의 글자가 같으면 제거
// 다르면 삽입
function solution(s)
{
    let stack = [s[0]];
    for(let i=1;i<s.length;i++){
        let target = stack[stack.length-1];
        if(target !== s[i]) {
            stack.push(s[i]);
        }else{
            stack.pop();
        }
    }
    return stack.length===0 ? 1 : 0
}