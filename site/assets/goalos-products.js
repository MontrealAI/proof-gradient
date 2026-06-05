(function(){
  const quiz = document.querySelector('[data-goalos-quiz]');
  if (!quiz) return;
  const resultScore = document.getElementById('goalos-score-value');
  const resultTextEn = document.getElementById('goalos-score-text-en');
  const resultTextFr = document.getElementById('goalos-score-text-fr');
  const answers = new Map();
  const ranges = [
    {min:0,max:30,en:'You are using AI as a chat box.',fr:'Vous utilisez l’IA comme une fenêtre de clavardage.'},
    {min:31,max:60,en:'You have partial AI leverage.',fr:'Vous avez un levier IA partiel.'},
    {min:61,max:80,en:'You have a working AI system.',fr:'Vous avez un système IA fonctionnel.'},
    {min:81,max:100,en:'You are operating with serious AI leverage.',fr:'Vous opérez avec un vrai levier IA.'}
  ];
  function render(){
    let score = 0;
    answers.forEach(v => { score += v; });
    resultScore.textContent = String(score);
    const range = ranges.find(r => score >= r.min && score <= r.max) || ranges[0];
    resultTextEn.textContent = range.en;
    resultTextFr.textContent = range.fr;
  }
  quiz.addEventListener('click', function(event){
    const button = event.target.closest('button[data-score]');
    if (!button) return;
    const question = button.getAttribute('data-question');
    answers.set(question, Number(button.getAttribute('data-score')));
    quiz.querySelectorAll('button[data-question="' + question + '"]').forEach(other => other.setAttribute('aria-pressed','false'));
    button.setAttribute('aria-pressed','true');
    render();
  });
  render();
})();
