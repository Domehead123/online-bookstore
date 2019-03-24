var el = document.getElementById("delete");

if(el){
  el.addEventListener("click", deleteWarning);

document.getElementById("no-delete").addEventListener("click", hideDeleteWarning);

function deleteWarning() {
  document.getElementById("delete-check").classList.remove("hidden");
}

function hideDeleteWarning() {
  document.getElementById("delete-check").classList.add("hidden");
}

}

