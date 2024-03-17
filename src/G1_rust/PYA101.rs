use std::io;

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    let n1: i32 = input.trim().parse().unwrap();

    input.clear();
    io::stdin().read_line(&mut input).unwrap();
    let n2: i32 = input.trim().parse().unwrap();

    input.clear();
    io::stdin().read_line(&mut input).unwrap();
    let n3: i32 = input.trim().parse().unwrap();

    input.clear();
    io::stdin().read_line(&mut input).unwrap();
    let n4: i32 = input.trim().parse().unwrap();

    println!("|{:<5} {:<5}|", n1, n2);
    println!("|{:<5} {:<5}|", n3, n4);
    println!("|{:>5} {:>5}|", n1, n2);
    println!("|{:>5} {:>5}|", n3, n4);
}
