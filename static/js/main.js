let entry;
if (entry.isIntersecting) {
  entry.target.style.animationPlayState = 'running';
  observer.unobserve(entry.target); // 👈 animate once only
}