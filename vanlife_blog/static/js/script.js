// sidenav initialization
document.addEventListener('DOMContentLoaded', function () {
  let sidenav = document.querySelectorAll('.sidenav');
  M.Sidenav.init(sidenav);

  // modal trigger initialization
  document.addEventListener('DOMContentLoaded', function () {
    let elems = document.querySelectorAll('.modal');
    M.Modal.init(elems);
  });
  
});