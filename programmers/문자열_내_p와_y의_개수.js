function solution(s){
    const mappingCount = {
        'P' : 0,
        'Y' : 0
    }
    for (const i of s.toUpperCase()) {
        if (i == 'P') mappingCount['P'] ++
        else if(i == 'Y') mappingCount['Y'] ++
    }

    return Object.values(mappingCount)[0] === Object.values(mappingCount)[1]
}