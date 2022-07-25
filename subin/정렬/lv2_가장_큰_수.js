function solution(numbers) {
  let answer = '';
  let sortArr = numbers
    .map((element) => String(element))
    .sort((a, b) => b + a - (a + b));

  if (sortArr[0] === '0') {
    return '0';
  } else {
    sortArr.map((element) => {
      answer += String(element);
    });
  }
  return answer;
}
