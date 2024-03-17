use std::io;

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    let s1: char = input.trim().parse().unwrap();

    input.clear();
    io::stdin().read_line(&mut input).unwrap();
    let s2: char = input.trim().parse().unwrap();

    input.clear();
    io::stdin().read_line(&mut input).unwrap();
    let s3: char = input.trim().parse().unwrap();

    input.clear();
    io::stdin().read_line(&mut input).unwrap();
    let s4: char = input.trim().parse().unwrap();

    println!("|{:<10} {:<10}|", s1, s2);
    println!("|{:<10} {:<10}|", s3, s4);
    println!("|{:>10} {:>10}|", s1, s2);
    println!("|{:>10} {:>10}|", s3, s4);
}
