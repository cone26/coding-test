function gcd(a,b) {
    const remainder = a % b
    if (remainder === 0) return b;
    return gcd(b, remainder)
}

function solution(numer1, denom1, numer2, denom2) {
    let denom = denom1 * denom2
    let numer = (numer1 * denom2) + (numer2 * denom1)
    let gcdAnswer

    if(denom > numer) gcdAnswer= gcd(numer, denom)
    else gcdAnswer= gcd(denom, numer)


    return [numer/gcdAnswer,denom/gcdAnswer];
}