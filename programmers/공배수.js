function solution(number, n, m) {
    const gcd = (n,m) => n % m === 0 ? m : gcd(m,n % m)
    const lcm = n * m / gcd(n,m)
    return number % lcm === 0 ? 1 : 0

}

function solution2(number, n, m) {
    return number % n === 0 && number % m === 0 ? 1 : 0

}