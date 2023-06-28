function solution(arr)
{
    if(arr.length > 1000000) return
    const overValue = arr.find((it)=> 0 > it || it > 10);
    if(overValue) return

//     let answer = []
//     answer.push(arr[0])

//     for(let i = 1; i < arr.length; i++){
//         if(arr[i] != arr[i-1]) answer.push(arr[i])
//     }
    const answer = arr.filter((value, index)=> value != arr[index+1])
    return answer;
}