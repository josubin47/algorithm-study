function solution(participant, completion) {
  participant.sort();
  completion.sort();
  return participant.filter((p, i) => p !== completion[i])[0];
}
