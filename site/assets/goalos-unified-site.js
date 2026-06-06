
(function(){function ready(f){document.readyState!=="loading"?f():document.addEventListener("DOMContentLoaded",f)}
ready(function(){var input=document.querySelector("[data-unified-search]");if(!input)return;var cards=[].slice.call(document.querySelectorAll("[data-unified-card]"));input.addEventListener("input",function(){var q=input.value.toLowerCase().trim();cards.forEach(function(c){c.style.display=!q||c.textContent.toLowerCase().indexOf(q)!==-1?"":"none"})})})})();
