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



function edit(){
  var editButton = document.getElementsByClassName("post-editBtn");
  Array.from(editButton).forEach(function(button){
    button.addEventListener("click", function(event){
      event.stopPropagation();
      var popID = button.getAttribute("data-popup");
      var targetPop = document.getElementById(popID);
      targetPop.style.display = "block";

      var closebtn = document.getElementsByClassName("pop-closeEdit");
      Array.from(closebtn).forEach(function(sec){
        sec.addEventListener("click", function(event){
          event.stopPropagation();
          var Id = sec.getAttribute("data-popup");
          tar = document.getElementById(Id)
          tar.style.display = "none";
        })
      })
    })
  });
}


function del(){
  console.log("hello from del")
  var delButtons = document.getElementsByClassName("post-deleteBtn");

  Array.from(delButtons).forEach(function(button){
    button.addEventListener("click", function(event){
      event.stopPropagation();
      var popID = button.getAttribute("data-popup");
      var targetPop = document.getElementById(popID);
      targetPop.style.display = "block";

      var closebtn = document.getElementsByClassName("pop-close");
      Array.from(closebtn).forEach(function(sec){
        sec.addEventListener("click", function(event){
          event.stopPropagation();
          var Id = sec.getAttribute("data-popup");
          tar = document.getElementById(Id)
          tar.style.display = "none";
        });
      });
    });
  });
}
  function remove(){
    console.log("hello from remove")
    var delButtons = document.getElementsByClassName("remove-member");
    console.log(delButtons)
    Array.from(delButtons).forEach(function(button){
      button.addEventListener("click", function(event){
        event.stopPropagation();
        var popID = button.getAttribute("data-popup");
        console.log(popID)
        var targetPop = document.getElementById(popID);
        console.log(targetPop)
        targetPop.style.display = "block";
  
        var closebtn = document.getElementsByClassName("popclose");
        Array.from(closebtn).forEach(function(sec){
          sec.addEventListener("click", function(event){
            event.stopPropagation();
            var Id = sec.getAttribute("data-popup");
            tar = document.getElementById(Id)
            tar.style.display = "none";
          });
        });
      });
    });
  }

