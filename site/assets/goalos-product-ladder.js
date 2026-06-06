
(function(){
  function ready(fn){document.readyState!=="loading"?fn():document.addEventListener("DOMContentLoaded",fn)}
  ready(function(){
    var input=document.querySelector("[data-product-search]");
    if(!input)return;
    var cards=[].slice.call(document.querySelectorAll("[data-product-card]"));
    input.addEventListener("input",function(){
      var q=input.value.toLowerCase().trim();
      cards.forEach(function(c){c.style.display=!q||c.textContent.toLowerCase().indexOf(q)!==-1?"":"none"});
    });
  });
})();
