function solution(array) {
    const mappingArray = {}
    array.forEach((it)=> mappingArray[it] = mappingArray[it] ? mappingArray[it] + 1 : 1)
    const maxCountNumber = Math.max(...Object.values(mappingArray))
    const answer = Object.keys(mappingArray)
        .filter((it)=> mappingArray[it] == maxCountNumber)

    return answer.length > 1 ? -1 : Number(answer[0])
}