
(function(){
  function ready(fn){ if(document.readyState !== "loading"){fn()} else {document.addEventListener("DOMContentLoaded",fn)} }
  ready(function(){
    var input = document.querySelector("[data-pg-search]");
    if(!input) return;
    var cards = Array.prototype.slice.call(document.querySelectorAll("[data-pg-card]"));
    input.addEventListener("input", function(){
      var q = input.value.toLowerCase().trim();
      cards.forEach(function(card){
        var text = card.textContent.toLowerCase();
        card.style.display = (!q || text.indexOf(q) !== -1) ? "" : "none";
      });
    });
  });
})();
