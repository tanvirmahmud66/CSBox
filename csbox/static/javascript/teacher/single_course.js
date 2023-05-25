document.getElementById("repo_button").addEventListener("click", function() {
    document.getElementById("Repo_section").style.display = "block";
    document.getElementById("Member_section").style.display = "none";
    document.querySelector("#repo_button").classList.add('active');
    document.querySelector("#member_button").classList.remove('active');
});

document.getElementById("member_button").addEventListener("click", function() {
    document.getElementById("Repo_section").style.display = "none";
    document.getElementById("Member_section").style.display = "block";
    document.querySelector(".other_info_btn").classList.remove('active');
    document.querySelector("#member_button").classList.add('active');
});

document.getElementById("popupButton").addEventListener("click", function() {
    document.getElementById("popupContainer").style.display = "block";
});

document.getElementById("closeButton").addEventListener("click", function() {
    document.getElementById("popupContainer").style.display = "none";
});



const fileInput = document.getElementById('file-input');
const fileList = document.querySelector('.file-list');

fileInput.addEventListener('change', handleFileSelect);

function handleFileSelect(event) {
  const files = event.target.files;
  for (let i = 0; i < files.length; i++) {
    const listItem = document.createElement('li');
    listItem.textContent = files[i].name;
    fileList.appendChild(listItem);
  }
}