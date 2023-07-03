function solution(lottos, win_nums) {
    const ranking = [6,6,5,4,3,2,1]
    const erased = lottos.filter(i=>i === 0).length
    let count = 0;
    win_nums.map((it)=> {
        if(lottos.indexOf(it) != -1) count++
    })
    return [ranking[count+erased], ranking[count]];
}