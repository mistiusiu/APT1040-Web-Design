const gridItems = document.querySelectorAll('.grid-item');

const observer = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('in-view');
    } else {
      entry.target.classList.remove('in-view');
    }
  });
});

gridItems.forEach((el) => observer.observe(el));
