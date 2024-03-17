use std::io;

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    let n1: f32 = input.trim().parse().unwrap();

    input.clear();
    io::stdin().read_line(&mut input).unwrap();
    let n2: f32 = input.trim().parse().unwrap();

    input.clear();
    io::stdin().read_line(&mut input).unwrap();
    let n3: f32 = input.trim().parse().unwrap();

    input.clear();
    io::stdin().read_line(&mut input).unwrap();
    let n4: f32 = input.trim().parse().unwrap();

    println!("|{:<7.2} {:<7.2}|", n1, n2);
    println!("|{:<7.2} {:<7.2}|", n3, n4);
    println!("|{:>7.2} {:>7.2}|", n1, n2);
    println!("|{:>7.2} {:>7.2}|", n3, n4);
}
