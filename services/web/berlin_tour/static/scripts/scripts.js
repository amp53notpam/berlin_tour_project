function openHotel(evt, id) {
  var i, x, tablinks;
  x = document.getElementsByClassName("albergo");
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablink");
  for (i = 0; i < x.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" w3-amber", ""); 
  }
  document.getElementById(id).style.display = "block";
  evt.currentTarget.className += " w3-amber";

  closeMenu()
}

function openLap(evt, start) {
  var i, x, tablinks;
  x = document.getElementsByClassName("tappa");
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablink");
  for (i = 0; i < x.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" w3-amber", ""); 
  }
  document.getElementById(start).style.display = "block";
  evt.currentTarget.className += " w3-amber";

  closeMenu()
}

function toggleMenu() {
  if (document.getElementById("sidebar").style.display === "block") {
    closeMenu()
  } else {
    openMenu()
  }
}

function openMenu() {
  document.getElementById("sidebar").style.width = "50%";
  document.getElementById("sidebar").style.display = "block";
}

function closeMenu() {
  document.getElementById("sidebar").style.width = "25%";
  document.getElementById("sidebar").style.display = "none";
}