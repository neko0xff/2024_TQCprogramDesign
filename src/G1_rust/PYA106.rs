use std::io;

fn main(){
    let mut input: String = String::new();
    io::stdin().read_line(&mut input).unwrap();
    let mins: f64 = input.trim().parse().unwrap();
    input.clear();
    io::stdin().read_line(&mut input).unwrap();
    let secs: f64 = input.trim().parse().unwrap();
    input.clear();
    io::stdin().read_line(&mut input).unwrap();
    let km: f64 = input.trim().parse().unwrap();

    let mile: f64 = km/1.6;
    let hour_avg: f64 = (secs/60.0+mins)/60.0;
    let speed: f64 = mile/hour_avg;

    print!("Speed = {:.1}",speed);
}