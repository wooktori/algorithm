function solution(n) {
   const target = n.toString(2).split('1').length-1;
   while(true){
       n++;
       if(target===n.toString(2).split('1').length-1){
           return n;
       }
   }
}