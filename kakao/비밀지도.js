function solution(n, arr1, arr2) {
    const firstMap = decimalToBinary(arr1,n);
    const secondMap = decimalToBinary(arr2,n);
    let perfectMap = []
    for (let i = 0; i < n; i++) {
        let row = ''
        for (let j = 0; j < n; j++) {
            row =  firstMap[i][j] == '1' || secondMap[i][j] == '1' ? row + '#' : row + ' ';
        }
        perfectMap.push(row);
    }
    return perfectMap;
}

function decimalToBinary(arr,n) {
    const binary = arr.map((it)=> {
        return  it.toString(2).length < n ? '0'.repeat(n - it.toString(2).length) + it.toString(2) : it.toString(2)
    })

    return binary;
}