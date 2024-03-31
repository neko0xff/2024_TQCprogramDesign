use std::io;

fn main(){
    let mut input: String = String::new();
    io::stdin().read_line(&mut input).unwrap();
    let n: i32 = input.trim().parse().unwrap();
    let result_false: i32 = 0;

    if n%3 == result_false && n%5 == result_false {
        print!("{} is a multiple of 3 and 5.",n);
    }else if n%5 == result_false {
        print!("{} is a multiple of 5.",n);
    }else if n%3 == result_false {
        print!("{} is a multiple of 3.",n);
    }else{
        print!("{} is not a multiple of 3 or 5.",n);
    }
}