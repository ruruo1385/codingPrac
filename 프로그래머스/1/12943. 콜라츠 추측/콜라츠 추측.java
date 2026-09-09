class Solution {
    public long solution(long num) {
        long count = 0;
        long answer = 0;
        while (num != 1){
            if(num == 1){
                answer = 0;
            }
            if(num % 2 == 0){
                num = num /2;
            }else{
                num = (num *3) +1;
            }
            count++;
            if(count == 500 && num != 1){
                answer = -1;
                break;
            }else{
                answer = count;
            }
        }
        return answer;
    }
}