function solution(answers) {
  const one = [1, 2, 3, 4, 5];
  const two = [2, 1, 2, 3, 2, 4, 2, 5];
  const three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];

  let answer = [];

  const score = [0, 0, 0];

  answers.map((a, i) => {
    if (a === one[i % one.length]) {
      score[0]++;
    }
    if (a === two[i % two.length]) {
      score[1]++;
    }
    if (a === three[i % three.length]) {
      score[2]++;
    }
  });

  const maxValue = Math.max(...score);

  score.map((val, index) => {
    if (maxValue === val) {
      answer.push(index + 1);
    }
  });

  return answer;
}
