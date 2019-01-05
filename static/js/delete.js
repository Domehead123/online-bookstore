document.getElementById("delete").addEventListener("click", deleteWarning);

document.getElementById("no-delete").addEventListener("click", hideDeleteWarning);

function deleteWarning() {
  document.getElementById("delete-check").classList.remove("hidden");
}

function hideDeleteWarning() {
  document.getElementById("delete-check").classList.add("hidden");
}

