import { spawn, Thread, Worker } from "threads"

function getRule(num, loops){
    if(loops === 0){
        return 1;
    }

    if(num == 0){
        return getRule(1, loops - 1);
    }
    else if (num.toString().length % 2 === 0){
        let str = num.toString();
        let half = Math.floor(str.length / 2);
        return getRule(parseInt(str.slice(0, half)), loops - 1) + getRule(parseInt(str.slice(half, str.length)), loops - 1);
    }else{
        return getRule(num * 2024, loops-1);
    }
}

let current = "-"
let current_split = current.split(" ");
let total = 0
for(let i = 0; i < current_split.length; i++){

    total += getRule(parseInt(current_split[i]), 75);
}
console.log(total)