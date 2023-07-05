function solution(s)
{
    let sArr = s.split('')
    let stack = []
    while(sArr.length != 0){
        stack.push(sArr.pop())
        while(sArr[sArr.length-1] == stack[stack.length-1]){
            sArr.pop()
            stack.pop()
            if(stack.length == 0) break
        }
    }
    return stack.length > 0 ? 0 : 1
}