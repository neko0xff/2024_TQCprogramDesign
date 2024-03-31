use std::io;

fn main(){
    let mut input: String= String::new();
    io::stdin().read_line(&mut input).unwrap();
    let year: i32= input.trim().parse().unwrap();
    let result_false: i32= 0;

    if year%4 == result_false && year%100 != result_false || year%400 == result_false {
        println!("{} is a leap year.",year);
    }else{
        println!("{} is not a leap year.",year);
    }
}