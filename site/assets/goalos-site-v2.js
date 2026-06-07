(function(){
  const links=[...document.querySelectorAll('.goalos-links a[href]')];
  const path=location.pathname.replace(/index\.html$/,'');
  for(const a of links){try{const u=new URL(a.href); if(u.pathname.replace(/index\.html$/,'')===path) a.setAttribute('aria-current','page');}catch(e){}}
  const nav=document.querySelector('.goalos-nav');
  if(nav && !document.querySelector('.goalos-menu')){const btn=document.createElement('button');btn.className='goalos-menu';btn.type='button';btn.textContent='Menu';btn.setAttribute('aria-expanded','false');btn.addEventListener('click',()=>{const box=document.querySelector('.goalos-links');const open=box.classList.toggle('open');btn.setAttribute('aria-expanded',String(open));});nav.appendChild(btn);}
  document.documentElement.dataset.goalosShell='v2';
})();
