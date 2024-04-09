const categoryMenu = document.querySelector(".category-bar"),
selectcategory = document.querySelector(".select-category"),
categories = document.querySelectorAll(".category"),
sltcattext = document.querySelector(".slt-cat-text");

const typeMenu = document.querySelector(".type-bar"),
selecttype = document.querySelector(".select-type"),
types = document.querySelectorAll(".type"),
slttypetext = document.querySelector(".slt-type-text");

selectcategory.addEventListener("click", () => categoryMenu.classList.toggle("active"));

selecttype.addEventListener("click", () => typeMenu.classList.toggle("active"));


categories.forEach(category =>{
    category.addEventListener("click", ()=>{
        let selectedCategory = category.querySelector(".category-text").innerText;
        sltcattext.innerText = selectedCategory;
    
        categoryMenu.classList.remove("active")
    })
})

types.forEach(type =>{
    type.addEventListener("click", ()=>{
        let selectedtype = type.querySelector(".type-text").innerText;
        slttypetext.innerText = selectedtype;
    
        typeMenu.classList.remove("active")
    })
})